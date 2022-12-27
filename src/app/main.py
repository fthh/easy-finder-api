from fastapi import FastAPI

from app.api import init_routes


def create_app():
    """Сздаёт инстанс приложения"""
    _app = FastAPI()
    init_routes(_app)
    return _app


app = create_app()
