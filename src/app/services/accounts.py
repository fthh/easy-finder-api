import json
import jwt
from datetime import datetime, timedelta

from app.entities import User, Role
from app.repos.users import UsersRepository
from app.system.exceptions import ServiceException

from app.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
)


class AccountsService:
    def __init__(self, users_repo: UsersRepository):
        self._users_repo = users_repo

    async def add_role(self, user: User, role: Role) -> User:
        user = await self._users_repo.add_role(user, role)
        return user

    async def registration(self, username: str, password: str, role: Role) -> User:
        try:
            user = await self._users_repo.create(username, password)
        except:
            raise ServiceException('username already taken')
        user = await self.add_role(user, role)
        return user

    async def login(self, username: str, password: str) -> tuple[User, str]:
        user = await self._users_repo.get_user_by_username(username)
        if user and user.password == password:
            token = self._get_token(user)
            return user, token
        raise ServiceException('Login or password is incorrect')

    def _get_token(self, user: User, expires_delta: int = None) -> str:
        """Создаёт JWT токен"""
        if expires_delta is not None:
            expires_delta = datetime.utcnow() + expires_delta
        else:
            expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = {'exp': expires_delta, 'sub': json.dumps({
            'uid': user.uid,
            'username': user.username,
        })}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, JWT_ALGORITHM)
        return encoded_jwt

    async def decode_token(self, token: str) -> User | None:
        payload = jwt.decode(
            token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )
        payload = json.loads(payload['sub'])
        return await self._users_repo.get_user_by_username(payload['username'])
