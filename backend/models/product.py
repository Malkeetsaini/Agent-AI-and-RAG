from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Boolean,
    Float
)

from backend.database.base import Base


class Product(Base):

    __tablename__ = "products"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    handle = Column(
        String(255),
        unique=True,
        nullable=False
    )

    title = Column(
        String(500),
        nullable=False
    )

    price = Column(
        Float,
        default=0
    )

    description = Column(Text)

    vendor = Column(String(255))

    product_type = Column(String(255))

    tags = Column(Text)

    category = Column(String(100))

    published = Column(
        Boolean,
        default=True
    )

    embed = Column(
        Boolean,
        default=False
    )

    image_url = Column(Text)

    image_alt_text = Column(Text)

    seo_title = Column(String(500))

    seo_description = Column(Text)

    google_category = Column(String(500))

    gender = Column(String(100))

    age_group = Column(String(100))

    condition_type = Column(String(100))