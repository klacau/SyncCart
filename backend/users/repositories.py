from motor.motor_asyncio import AsyncIOMotorDatabase

from users.models import Session, User
from key_value_store import KeyValueStore

from result import Result, Ok, Err
from typing import Optional
from uuid import uuid4

class SessionsRepository:
    def __init__(self, kvstore: KeyValueStore[str, Session]):
        self.__kvstore = kvstore

    async def create_session(self, username: str) -> str:
        session_id = f"{uuid4()}"
        self.__kvstore.set(session_id, Session(username=username))
        return session_id
    
    async def terminate_session(self, session_id: str):
        self.__kvstore.remove(session_id)

    async def get_session(self, session_id: str) -> Result[Session, str]:
        session = self.__kvstore.get(session_id)
        if session is None:
            return Err("")
        return Ok(session)

class UsersRepository:
    def __init__(self, db: AsyncIOMotorDatabase):
        self.__db = db

    async def get_user(self, username: str) -> Optional[User]:
        user_data = await self.__db.users.find_one({ "username": username })
        return User(**user_data)
    
    async def add_user(self, user: User) -> Result[User, str]:
        query_result = await self.__db.users.find_one({ "username": user.username })
        if query_result is not None:
            return Err("Username is taken")
        
        query_result = await self.__db.users.find_one({ "email": user.email })
        if query_result is not None:
            return Err("Email already used")
        
        await self.__db.users.insert_one({
            "username": user.username,
            "email": user.email,
            "hashed_password": user.hashed_password
        })
        
        return Ok(user)
