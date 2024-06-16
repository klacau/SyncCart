from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends, HTTPException, Request, Response, status

from motor.motor_asyncio import AsyncIOMotorClient

from cart.repositories import ProductListsRepository
from cart.models import ProductList, ProductListCreate, ProductListUpdate
from key_value_store import RAMOnlyKVStore

from users.forms import SignInForm, SignUpForm
from users.models import User
from users.passwords import PasswordContext
from users.repositories import SessionsRepository, UsersRepository

from result import is_err, Result, Ok, Err
from typing import Annotated, Optional

db_client = AsyncIOMotorClient("mongodb://localhost:27017")
database = db_client.sync_cart

password_context = PasswordContext()

product_lists_repository = ProductListsRepository(database)
users_repository = UsersRepository(database)
sessions_repository = SessionsRepository(RAMOnlyKVStore())

app = FastAPI()

allowed_origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_session_id(request: Request) -> Optional[str]:
    return request.cookies.get("session")

async def authenticate_user(username: str, password: str) -> Result[User, str]:
    user = await users_repository.get_user(username)

    if user is None:
        return Err("User does not exist")
    if not password_context.verify_password(password, user.hashed_password):
        return Err("Incorrect password")
    
    return Ok(user)

async def get_current_user(session_id: Annotated[Optional[str], Depends(get_session_id)]) -> User:
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    if session_id is None:
        raise credential_exception

    session_result = await sessions_repository.get_session(session_id)
    if is_err(session_result):
        raise credential_exception
    
    session = session_result.ok_value
    user = await users_repository.get_user(session.username)
    if user is None:
        raise credential_exception
    
    return user

@app.post("/auth/login")
async def login(form_data: Annotated[SignInForm, Depends()], response: Response):
    user_result = await authenticate_user(form_data.username, form_data.password)
    if is_err(user_result):
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail=user_result.err_value
            )

    user = user_result.ok_value
    session_id = await sessions_repository.create_session(user.username)
    response.set_cookie("session", 
            value=session_id, 
            max_age=259200,
            expires=259200,
            httponly=True,
            secure=True,
            samesite='strict'
        )

@app.post("/auth/logout")
async def logout(session_id: Annotated[Optional[str], Depends(get_session_id)], response: Response):
    if session_id is None:
        return
    
    await sessions_repository.terminate_session(session_id)
    response.delete_cookie("session", httponly="True", secure="True")

@app.post("/auth/sign-up")
async def sign_up_user(form_data: Annotated[SignUpForm, Depends()], response: Response):
    user = User(
            username=form_data.username,
            email=form_data.email,
            hashed_password=password_context.hash_password(form_data.password)
        )
    
    result = await users_repository.add_user(user)

    if is_err(result):
        raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=result.err_value
            )
    
    session_id = await sessions_repository.create_session(user.username)
    response.set_cookie("session", 
            value=session_id, 
            max_age=259200,
            expires=259200,
            httponly=True,
            secure=True,
            samesite='strict'
        )

@app.get("/product-lists")
async def get_product_lists(current_user: Annotated[User, Depends(get_current_user)]) -> list[ProductList]:
    return await product_lists_repository.get_product_lists(current_user.username)

@app.get("/product-lists/{product_list_id}")
async def get_product_list(
        product_list_id: str, 
        current_user: Annotated[User, Depends(get_current_user)]
    ) -> Optional[ProductList]:
    product_list = await product_lists_repository.get_product_list(product_list_id)
    if product_list.username != current_user.username:
        return None
    return product_list

@app.post("/product-lists/{product_list_id}")
async def create_product_list(
        product_list_id: str, 
        data: ProductListCreate, 
        current_user: Annotated[User, Depends(get_current_user)]
    ):
    product_list = ProductList(
        product_list_id=product_list_id,
        username=current_user.username,
        name=data.name,
        color=data.color,
        items=data.items
    )
    await product_lists_repository.add_product_list(product_list)

@app.put("/product-lists/{product_list_id}")
async def update_product_list(
        product_list_id: str, 
        data: ProductListUpdate, 
        current_user: Annotated[User, Depends(get_current_user)]
    ):
    product_list = await product_lists_repository.get_product_list(product_list_id)
    if product_list is None or product_list.username != current_user.username:
        return
    
    await product_lists_repository.update_product_list(product_list_id, data)

@app.delete("/product-lists/{product_list_id}")
async def delete_product_list(
        product_list_id: str, 
        current_user: Annotated[User, Depends(get_current_user)]
    ):
    product_list = await product_lists_repository.get_product_list(product_list_id)
    if product_list is None or product_list.username != current_user.username:
        return
    
    await product_lists_repository.delete_product_list(product_list_id)
