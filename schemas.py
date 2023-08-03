from pydantic import BaseModel


class Product_Category(BaseModel):
    id:int
    name:str