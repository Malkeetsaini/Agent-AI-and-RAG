from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    Float,
    String
)

from backend.database.base import Base


class Order(Base):

    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    total_amount = Column(
        Float,
        default=0
    )

    status = Column(
        String(50),
        default="pending"
    )