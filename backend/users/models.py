from pydantic import BaseModel

class UserPublic(BaseModel):
    username: str
    email: str

class User(UserPublic):
    hashed_password: str

class Session(BaseModel):
    username: str
