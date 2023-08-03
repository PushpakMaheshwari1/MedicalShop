from fastapi import APIRouter,status
from database import Session,engine
from schemas import Product_Category,Cash_book
from models import Category,Cashbook
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
    categorycashbook_to_update = session.query(Category).filter(Category.id == id).first()

    categorycashbook_to_update.name = category.name

    session.commit()

    response={
        "id":categorycashbook_to_update.id,
        "name":categorycashbook_to_update.name
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




## Add Daily CashBook

@inventory_router.post("/cashbook/add",status_code=status.HTTP_201_CREATED)
async def create_cashbook(cashbook: Cash_book):
    new_cashbook  = Cashbook(
        sell_amount = cashbook.sell_amount,
        date = cashbook.date,
        profit_percentage = cashbook.profit_percentage,
        category_id = cashbook.category_id

    )
    session.add(new_cashbook )

    session.commit()    

    response = {
        "sell_amount" : new_cashbook .sell_amount,
        "date" : new_cashbook .date,
        "percentage" : new_cashbook .profit_percentage,
        "category_id" : cashbook.category_id
    }

    return jsonable_encoder(response)

## List Cashbook

@inventory_router.get("/cashbook/list")
async def list_entries():
        cashbook = session.query(Cashbook).all()
        
        return jsonable_encoder(cashbook)

## Update CashBook 

@inventory_router.put("/inventory/update/{id}",)
async def update_category(id : int , cashbook : Cash_book):
    cashbook_to_update = session.query(Cashbook).filter(Cashbook.id == id).first()

    cashbook_to_update.sell_amount = cashbook.sell_amount
    cashbook_to_update.date = cashbook.date
    cashbook_to_update.profit_percentage = cashbook.profit_percentage
    cashbook_to_update.category_id = cashbook.category_id
    

    session.commit()

    response={
    "ell_amount" : cashbook.sell_amount,
    "date" : cashbook.date,
    "profit_percentage" : cashbook.profit_percentage,
    "category_id" : cashbook.category_id,
        }
    
    return jsonable_encoder (response)

## Delete CashBook Entries
@inventory_router.delete("/cashbook/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_an_order(id:int):
    cashbook_to_delete = session.query(Cashbook).filter(Cashbook.id == id).first()
    
    session.delete(cashbook_to_delete)

    session.commit()

    return cashbook_to_delete
 

