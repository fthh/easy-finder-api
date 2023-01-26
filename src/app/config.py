import os

ALLOW_ORIGINS = [
    "http://localhost",
    "http://localhost:3001",
]

# JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 100  # 100 days
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
JWT_ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')   # should be kept secret
if not JWT_SECRET_KEY:
    JWT_SECRET_KEY = 'secret'
JWT_REFRESH_SECRET_KEY = os.environ.get('JWT_REFRESH_SECRET_KEY')    # should be kept secret
if not JWT_REFRESH_SECRET_KEY:
    JWT_REFRESH_SECRET_KEY = 'secret'
