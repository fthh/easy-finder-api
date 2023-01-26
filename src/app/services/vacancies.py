
from app.entities import User, Vacancy, Role
from app.repos.vacancies import VacanciesRepository
from app.system.exceptions import ServiceException


class VacanciesService:
    """Сервис для взаимодействия с вакансиями"""

    def __init__(
        self,
        vacancies_repo: VacanciesRepository,
    ):
        self._vacancies_repo = vacancies_repo

    async def create_vacancy(self, title: str, actor: User) -> Vacancy:
        """Создаёт вакансию"""

        if Role.HR not in actor.roles:
            raise ServiceException('User must have HR role')

        return await self._vacancies_repo.create(title, actor)


    async def like_vacancy(self, vacancy: Vacancy, actor: User) -> Vacancy:
        # TODO
        return vacancy

    async def dislike_vacancy(self, vacancy: Vacancy, actor: User) -> Vacancy:
        # TODO
        return vacancy
