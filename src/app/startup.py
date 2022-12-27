from app.services.accounts import AccountsService
from app.repos.users import UsersRepository



async def init_repositories(app):
    """Инициализирует репозитории"""
    app.state.users_repo = UsersRepository()


async def init_services(app):
    """Инициализирует репозитории"""
    app.state.accounts_s = AccountsService(app.state.users_repo)
