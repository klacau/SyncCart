from motor.motor_asyncio import AsyncIOMotorDatabase

from auth.models import User

from result import Result, Ok, Err
from typing import Optional

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
