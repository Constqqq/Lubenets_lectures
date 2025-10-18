from uuid import uuid4
from pydantic import BaseModel, Field, EmailStr, AnyHttpUrl, SecretStr, UUID4
class User(BaseModel, Field, EmailStr, AnyHttpUrl, SecretStr):
    # id : UUID4 = Field(default_factory=uuid4, description="User ID")
    email: EmailStr = Field(default=...,description='email srting')
    name:str = Field(default=..., description="username")
    age:int = Field(default=..., description="age")
    personal_website: AnyHttpUrl  = Field(default=..., description="personal website")
    password: SecretStr = Field(default=..., description="password")
if __name__ == "__main__":
    user: User= User(
        email="useremail@example.com",
        name = "wafledron",
        age = 20,
        personal_website = "https://www.example.com",
        password = SecretStr(secret_value="password"),
        
            )
class random_user_factory():
    def __init__(self):
        self.user = User(
            email="useremail@example.com",
            name = "wafledron",
            age = 20,
            personal_website = "https://www.example.com",
            password = SecretStr(secret_value="password"),
        )
        return self.user