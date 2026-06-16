from sqlalchemy.orm import Session

from backend.models.user import User

from backend.schemas.auth import (
    RegisterSchema,
    LoginSchema
)

from backend.utils.hashing import (
    hash_password,
    verify_password
)

from backend.utils.jwt import (
    create_access_token
)


def register_user(
    db: Session,
    payload: RegisterSchema
):

    existing_user = (
        db.query(User)
        .filter(
            User.email == payload.email
        )
        .first()
    )

    if existing_user:

        raise Exception(
            "Email already exists"
        )

    user = User(

        name=payload.name,

        email=payload.email,

        password=hash_password(
            payload.password
        )
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message":
        "User registered successfully"
    }


def login_user(
    db: Session,
    payload: LoginSchema
):

    user = (
        db.query(User)
        .filter(
            User.email == payload.email
        )
        .first()
    )

    if not user:

        raise Exception(
            "Invalid Email"
        )

    if not verify_password(
        payload.password,
        user.password
    ):

        raise Exception(
            "Invalid Password"
        )

    token = create_access_token(
        {
            "user_id": user.id,
            "email": user.email
        }
    )

    return {

        "access_token": token,

        "token_type": "bearer"
    }