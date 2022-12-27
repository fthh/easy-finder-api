from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import ALLOW_ORIGINS

from .accounts import router as accounts_router
from .health_checks import router as health_checks_router


def init_routes(app):
    """Инициализирует роуты для приложения"""

    routers = [
        accounts_router,
        health_checks_router,
    ]
    for r in routers:
        app.include_router(r)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOW_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


__all__ = [
    'init_routes',
]
