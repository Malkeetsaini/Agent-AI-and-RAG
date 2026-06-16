from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):

    handle: str

    title: str

    description: Optional[str] = None

    vendor: Optional[str] = None

    product_type: Optional[str] = None

    tags: Optional[str] = None

    category: Optional[str] = None

    image_url: Optional[str] = None


class ProductResponse(ProductCreate):

    id: int

    class Config:
        from_attributes = True