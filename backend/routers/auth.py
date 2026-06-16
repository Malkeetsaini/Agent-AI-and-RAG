from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from backend.utils.dependencies import (
    get_db
)

from backend.schemas.auth import (
    RegisterSchema,
    LoginSchema
)

from backend.services.auth_service import (
    register_user,
    login_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(

    payload: RegisterSchema,

    db: Session = Depends(
        get_db
    )
):

    try:

        return register_user(
            db,
            payload
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post("/login")
def login(

    payload: LoginSchema,

    db: Session = Depends(
        get_db
    )
):

    try:

        return login_user(
            db,
            payload
        )

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )