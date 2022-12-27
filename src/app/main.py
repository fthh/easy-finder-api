from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse

from app.api import init_routes
from app.startup import init_repositories, init_services
from app.system.exceptions import ServiceException


def create_app():
    """Создаёт инстанс приложения"""
    _app = FastAPI(
        title='IgorEasyJobApp',
    )
    init_routes(_app)
    return _app


app = create_app()


@app.on_event('startup')
async def startup_init_repositories():
    """Инициализирует репозитории"""
    await init_repositories(app)


@app.on_event('startup')
async def startup_init_services():
    """Инициализирует сервисы"""
    await init_services(app)


@app.exception_handler(ServiceException)
async def validation_exception_handler(request, err):
    return JSONResponse(
        status_code=400,
        content={
            'error_message': str(err),
        })
