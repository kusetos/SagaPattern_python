from src.models.ProductOrder import ProductOrder
from pydantic import BaseModel
from typing import List, Dict, Any


class CheckoutRequest(BaseModel):
    user_id: int
    products: List[ProductOrder]
    payment_method: str