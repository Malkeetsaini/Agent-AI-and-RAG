from pydantic import BaseModel


class CreateOrderSchema(BaseModel):

    user_id: int