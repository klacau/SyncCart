from fastapi import Form

from typing import Annotated

class SignInForm:
    def __init__(self, *, 
            username: Annotated[str, Form()],
            password: Annotated[str, Form()]
        ):
        self.username = username
        self.password = password

class SignUpForm:
    def __init__(self, *, 
            username: Annotated[str, Form(min_length=1, max_length=16, pattern=r"^[a-zA-Z0-9_]*$")],
            email: Annotated[str, Form(max_length=50, pattern=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")],
            password: Annotated[str, Form(min_length=8, max_length=80)]
        ):
        self.username = username
        self.email = email
        self.password = password
