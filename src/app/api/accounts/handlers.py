import uuid
from fastapi import APIRouter, Request, Depends

from app.services.accounts import AccountsService
from app.api.deps import get_current_user
from app.entities import User, Role


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
        request_data.role,
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
    user, token = await accounts_s.login(request_data.username, request_data.password)
    return LoginResponse(
        token=token,
        user=user,
    )


@router.get(
    '/api/accounts/me',
    tags=['accounts'],
    response_model=User,
)
async def me(actor: User = Depends(get_current_user)):
    return actor



@router.get('/api/accounts/logout', tags=['accounts'])
def logout():
    return {'status': 'ok'}
