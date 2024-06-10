from pydantic import BaseModel, Field

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

class SignUpForm(BaseModel):
    username: str = Field(min_length=1, max_length=16, pattern=r"^[a-zA-Z0-9_]*$")
    email: str = Field(max_length=50, pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    password: str = Field(min_length=8, max_length=80)
