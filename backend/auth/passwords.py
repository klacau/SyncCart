from passlib.context import CryptContext

class PasswordContext:
    def __init__(self):
        self.crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.crypt_context.verify(plain_password, hashed_password)

    def hash_password(self, password) -> str:
        return self.crypt_context.hash(password)
