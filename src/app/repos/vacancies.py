import uuid

from app.entities import User, Vacancy
from .abstract import AbstractRepository


class VacanciesRepository(AbstractRepository):
    """Репозиторий для работы с вакансиями"""

    def __init__(self):
        self._vacancies = [
            Vacancy(
                uid=str(uuid.uuid4()),
                title='Ищем пацана уровня не ниже senior или junior',
            ),
            Vacancy(
                uid=str(uuid.uuid4()),
                title='Требуется писатель реп текстов',
            ),
        ]

    async def create(self, title: str, author: User) -> Vacancy:
        v = Vacancy(
            uid=str(uuid.uuid4()),
            title=title,
            author=author,
        )
        self._vacancies.append(v)
        return v

    # async def get_user_by_username(self, username: str) -> User | None:
    #     for u in self._users:
    #         if u.username == username:
    #             return u
