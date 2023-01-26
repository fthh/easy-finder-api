import enum
from pydantic import BaseModel

class Role(enum.Enum):
    EMPLOYEE = 'employee'
    HR = 'hr'

class User(BaseModel):
    uid: str
    username: str
    password: str
    roles: list[Role] = []


class Vacancy(BaseModel):
    uid: str
    title: str
    author: User
