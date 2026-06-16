from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.utils.dependencies import get_db

from backend.schemas.product import (
    ProductCreate
)

from backend.services.product_service import (
    create_product,
    get_products,
    get_product_by_id
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post("/")
def create_product_api(
    payload: ProductCreate,
    db: Session = Depends(get_db)
):
    return create_product(
        db,
        payload
    )


@router.get("/")
def get_all_products(
    db: Session = Depends(get_db)
):
    return get_products(db)


@router.get("/{product_id}")
def get_single_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return get_product_by_id(
        db,
        product_id
    )