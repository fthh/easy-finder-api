
from app.entities import User
from app.repos.users import UsersRepository
from app.system.exceptions import ServiceException


class AccountsService:
    def __init__(self, users_repo: UsersRepository):
        self._users_repo = users_repo

    async def registration(self, username: str, password: str) -> User:
        try:
            user = await self._users_repo.create(username, password)
        except:
            raise ServiceException('username already taken')
        return user

    async def login(self, username: str, password: str) -> User:
        user = await self._users_repo.get_user_by_username(username)
        if user and user.password == password:
            return user
        raise ServiceException('Login or password is incorrect')
