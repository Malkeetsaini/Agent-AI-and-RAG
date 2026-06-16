from sqlalchemy import (
    Column,
    Integer,
    ForeignKey
)

from backend.database.base import Base


class Cart(Base):

    __tablename__ = "carts"

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