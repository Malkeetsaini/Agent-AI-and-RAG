from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from jose import jwt, JWTError

from backend.database.session import SessionLocal
from backend.models.user import User

SECRET_KEY = "MY_SUPER_SECRET_KEY"
ALGORITHM = "HS256"

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = payload.get("user_id")

        if not user_id:
            raise HTTPException(
                status_code=401,
                detail="Invalid Token"
            )

        db = SessionLocal()

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        db.close()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="User Not Found"
            )

        return user

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Token Invalid or Expired"
        )