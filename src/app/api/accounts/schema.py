from pydantic import BaseModel
from app.entities import User


class RegistrationRequest(BaseModel):
    username: str
    password: str


class RegistrationResponse(BaseModel):
    user: User


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    user: User
