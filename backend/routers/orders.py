from fastapi import (
    APIRouter,
    Depends
)

from sqlalchemy.orm import Session

from backend.utils.dependencies import (
    get_db
)

from backend.schemas.order import (
    CreateOrderSchema
)

from backend.services.order_service import (
    create_order,
    get_orders
)

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.post("/")
def create_order_api(

    payload:
    CreateOrderSchema,

    db: Session = Depends(
        get_db
    )
):

    return create_order(
        db,
        payload.user_id
    )


@router.get("/{user_id}")
def get_user_orders(

    user_id: int,

    db: Session = Depends(
        get_db
    )
):

    return get_orders(
        db,
        user_id
    )