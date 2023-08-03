from pydantic import BaseModel
from datetime import date


class Cash_book(BaseModel):
    id:int = None
    sell_amount: float
    date: date
    profit_percentage: float
    category_id : int

    class Config:
        from_attributes = True

class Product_Category(BaseModel):
    id:int
    name:str

    class Config:
        from_attributes = True