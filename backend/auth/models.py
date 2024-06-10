from pydantic import BaseModel

class UserPublic(BaseModel):
    username: str
    email: str

class User(UserPublic):
    hashed_password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str
