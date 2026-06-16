from fastapi import (
    APIRouter,
    Depends
)

from backend.middleware.auth_middleware import (
    get_current_user
)

from backend.models.user import User

from sqlalchemy.orm import Session

from backend.utils.dependencies import (
    get_db
)

from backend.schemas.cart import (
    AddToCartSchema
)

from backend.services.cart_service import (
    add_to_cart,
    get_cart,
    remove_from_cart
)

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]
)


@router.post("/add")
def add_cart_item(
    payload: AddToCartSchema,
    db: Session = Depends(get_db),
    current_user: User = Depends(
        get_current_user
    )
):

    return add_to_cart(
        db,
        payload.user_id,
        payload.product_id,
        payload.quantity
    )


@router.get("/{user_id}")
def get_user_cart(
    user_id: int,
    db: Session = Depends(get_db)
):

    return get_cart(
        db,
        user_id
    )


@router.delete(
    "/remove/{cart_item_id}"
)
def delete_cart_item(
    cart_item_id: int,
    db: Session = Depends(get_db)
):

    return remove_from_cart(
        db,
        cart_item_id
    )