from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Float
)

from backend.database.base import Base


class OrderItem(Base):

    __tablename__ = "order_items"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
        default=1
    )

    price = Column(
        Float,
        default=0
    )