import uuid
from fastapi import APIRouter, Request, Depends

from app.services.accounts import AccountsService

from .schema import (
    LoginRequest, LoginResponse,
    RegistrationRequest, RegistrationResponse
)


router = APIRouter()


@router.post(
    '/api/accounts/registration',
    response_model=RegistrationResponse,
    tags=['accounts']
)
async def registration(
    r: Request,
    request_data: RegistrationRequest,
) -> RegistrationResponse:
    accounts_s: AccountsService = r.app.state.accounts_s
    user = await accounts_s.registration(
        request_data.username,
        request_data.password,
    )
    return RegistrationResponse(
        user=user,
    )


@router.post(
    '/api/accounts/login',
    tags=['accounts'],
    response_model=LoginResponse,
)
async def login(r: Request, request_data: LoginRequest):
    accounts_s: AccountsService = r.app.state.accounts_s
    user = await accounts_s.login(request_data.username, request_data.password)
    return LoginResponse(
        user=user,
    )


@router.get('/api/accounts/logout', tags=['accounts'])
def logout():
    return {'status': 'ok'}
