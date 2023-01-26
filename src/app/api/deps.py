from typing import Union, Any
from datetime import datetime
from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from app.entities import User, Role
from app.services.accounts import AccountsService

from app.config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY,
    JWT_ALGORITHM,
)


reuseable_oauth = OAuth2PasswordBearer(
    tokenUrl='/api/accounts/login',
    scheme_name='JWT'
)

async def get_current_user(r: Request, token: str = Depends(reuseable_oauth)) -> User:
    accounts_service: AccountsService = r.app.state.accounts_s
    user = await accounts_service.decode_token(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Could not find user',
        )
    return user
