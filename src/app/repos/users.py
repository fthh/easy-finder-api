import uuid

from app.entities import User
from .abstract import AbstractRepository


class UsersRepository(AbstractRepository):
    """Репозиторий для работы с юзерами"""

    def __init__(self):
        self._users = []

    async def create(self, username: str, password: str) -> User:
        assert not await self.get_user_by_username(username)

        u = User(
            uid=str(uuid.uuid4()),
            username=username,
            password=password,
        )
        self._users.append(u)
        return u

    async def get_user_by_username(self, username: str) -> User | None:
        for u in self._users:
            if u.username == username:
                return u
