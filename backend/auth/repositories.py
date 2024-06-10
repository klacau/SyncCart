from motor.motor_asyncio import AsyncIOMotorDatabase

from auth.models import User
from auth.passwords import PasswordContext

from result import Result, Ok, Err
from typing import Optional

class UsersRepository:
    def __init__(self, db: AsyncIOMotorDatabase, password_context: PasswordContext):
        self.__db = db
        self.__password_context = password_context

    async def get_user(self, username: str) -> Optional[User]:
        return User(**(await self.__db.users.find_one({ "username": username })))
    
    async def authenticate_user(self, username: str, password: str) -> Result[User, str]:
        user = await self.get_user(username)

        if user is None:
            return Err("User does not exist")
        if not self.__password_context.verify_password(password, user.hashed_password):
            return Err("Incorrect password")
        
        return Ok(user)
