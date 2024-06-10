from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone

from motor.motor_asyncio import AsyncIOMotorClient

from auth.models import Token, TokenData, User
from auth.passwords import PasswordContext
from auth.repositories import UsersRepository

from result import is_err

from cart.repositories import ProductListsRepository
from cart.models import ProductList

from typing import Annotated

SECRET_KEY = "dedafda6e2c3943cfcb674a8b7f5e61bcaceaa3ba1742ce6c9458be83c62271e"
SIGNING_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def create_access_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()
    to_encode["exp"] = datetime.now(timezone.utc) + expires_delta

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=SIGNING_ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credential_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            headers={ "WWW-Authenticate": "Bearer" }
        )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[SIGNING_ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    
    user = await users_repository.get_user(token_data.username)
    if user is None:
        raise credential_exception
    
    return user


db_client = AsyncIOMotorClient("mongodb://localhost:27017")
database = db_client.sync_cart

product_lists_repository = ProductListsRepository(database)
users_repository = UsersRepository(database, PasswordContext())

app = FastAPI()

allowed_origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/auth/token")
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
    user_result = await users_repository.authenticate_user(form_data.username, form_data.password)
    if is_err(user_result):
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, 
                detail=user_result.err_value,
                headers={"WWW-Authenticate": "Bearer"}
            )

    user = user_result.ok_value

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token({"sub": user.username}, access_token_expires)

    return Token(access_token=access_token, token_type="bearer")

@app.get("/product-lists")
async def get_product_lists(current_user: Annotated[User, Depends(get_current_user)]) -> list[ProductList]:
    return await product_lists_repository.get_product_lists(current_user.username)
