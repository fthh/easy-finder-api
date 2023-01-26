from pydantic import BaseModel
from app.entities import User, Role


class RegistrationRequest(BaseModel):
    username: str
    password: str
    role: Role


class RegistrationResponse(BaseModel):
    user: User


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    user: User
    token: str
