from sqlalchemy.orm import Session

from backend.models.product import Product

from backend.schemas.product import ProductCreate


def create_product(
    db: Session,
    payload: ProductCreate
):

    product = Product(**payload.model_dump())

    db.add(product)

    db.commit()

    db.refresh(product)

    return product


def get_products(db: Session):

    return db.query(Product).all()


def get_product_by_id(
    db: Session,
    product_id: int
):

    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )