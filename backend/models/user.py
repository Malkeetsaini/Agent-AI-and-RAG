from sqlalchemy import (
    Column,
    BigInteger,
    String
)

from backend.database.base import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    password = Column(
        String(255),
        nullable=False
    )