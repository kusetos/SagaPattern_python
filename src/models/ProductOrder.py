from pydantic import BaseModel

class ProductOrder(BaseModel):
    id: int
    quantity: int
