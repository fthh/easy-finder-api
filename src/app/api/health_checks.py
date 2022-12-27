import uuid
from fastapi import APIRouter, Request


router = APIRouter()


@router.get('/health/up', tags=['system'])
def health_up():
    return {'status': 'ok'}


@router.get('/health/ready', tags=['system'])
def health_ready():
    return {'status': 'ok'}
