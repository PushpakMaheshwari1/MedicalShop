from fastapi import APIRouter,status
from database import Session,engine
from schemas import Product_Category
from models import Category
from fastapi.encoders import jsonable_encoder


session = Session(bind = engine)

inventory_router = APIRouter(
    prefix="/inventory",
    tags=['Inventory']
)

## Add Category
@inventory_router.post("/category/add",status_code=status.HTTP_201_CREATED)
async def Add_Category(category : Product_Category):
    new_category = Category(
        name = category.name
    )

    session.add(new_category)

    session.commit()

    response = {
        "name" : new_category.name
    }

    return jsonable_encoder(response)

## Update Category
@inventory_router.put("/category/update/{id}",)
async def update_category(id : int , category : Product_Category):
    category_to_update = session.query(Category).filter(Category.id == id).first()

    category_to_update.name = category.name

    session.commit()

    response={
        "id":category_to_update.id,
        "name":category_to_update.name
        }
    return jsonable_encoder (response) 


## List Category
@inventory_router.get("/category/list")
async def list_Categories():
        categories = session.query(Category).all()

        return jsonable_encoder(categories)

## Delete Category
@inventory_router.delete("/category/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_an_order(id:int):
    inventory_to_delete = session.query(Category).filter(Category.id == id).first()
    
    session.delete(inventory_to_delete)

    session.commit()

    return inventory_to_delete


