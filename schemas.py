from pydantic import BaseModel
from datetime import date


class Cash_book(BaseModel):
    sell_amount: float
    date: date
    profit_percentage: float
    category_id : int

    class Config:
        from_attributes = True

class Product_Category(BaseModel):
    name:str

    class Config:
        from_attributes = True

class Invent(BaseModel):
    product_name :str
    quantity :int
    purchaseFrom :str
    manufacture :str
    expiry :date
    amount :float
    total :float
    close :bool
    
    class Config:
        from_attributes = True