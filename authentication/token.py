import jwt
from datetime import datetime as dt
from datetime import timedelta, timezone
from django.conf import settings


def access_token(userId):
    expiration_time = dt.now(timezone.utc) + timedelta(hours=1)
    payload = {
        "user_id": userId,
        "exp": expiration_time,  # Expiration time
        "iat": dt.now(timezone.utc),
    }

    token = jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return token


def refresh_token(userId):
    expiration_time = dt.now(timezone.utc) + timedelta(days=3)
    payload = {
        "user_id": userId,
        "exp": expiration_time,  # Expiration time
        "iat": dt.now(timezone.utc),
    }
    token = jwt.encode(
        payload, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )
    return token
