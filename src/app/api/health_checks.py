import uuid
from fastapi import APIRouter, Request


router = APIRouter()


@router.get('/health/up')
def health_up():
    return {'status': 'ok'}


@router.get('/health/ready')
def health_ready():
    return {'status': 'ok'}
