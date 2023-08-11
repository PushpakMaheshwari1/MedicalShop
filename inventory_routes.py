from fastapi import APIRouter,status,Depends,HTTPException
from sqlalchemy import and_,or_
from database import Session,engine
from schemas import Product_Category,Cash_book,Invent
from models import Category,Cashbook,Inventory,User
from fastapi.encoders import jsonable_encoder
from oauth2 import get_current_user
from datetime import datetime,date
from typing import Annotated

session = Session(bind = engine)

inventory_router = APIRouter(
    prefix="/inventory",
    tags=['Inventory']
)

## Add Category
@inventory_router.post("/category/add",status_code=status.HTTP_201_CREATED)
async def Add_Category(category : Product_Category,current_user : int = Depends(get_current_user)):
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
@inventory_router.put("/category/update/{id}")
async def update_category(id : int , category : Product_Category,current_user : int = Depends(get_current_user)):
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
async def list_Categories(current_user : int = Depends(get_current_user)):
        categories = session.query(Category).all()

        return jsonable_encoder(categories)

## Delete Category
@inventory_router.delete("/category/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_category(id:int,current_user : int = Depends(get_current_user)):
    category_to_delete = session.query(Category).filter(Category.id == id).first()
    
    session.delete(category_to_delete)

    session.commit()

    return category_to_delete


## Add CashBook

@inventory_router.post("/cashbook/add",status_code=status.HTTP_201_CREATED)
async def create_cashbook(cashbook: Cash_book,current_user : int = Depends(get_current_user)):
    new_cashbook  = Cashbook(
        sell_amount = cashbook.sell_amount,
        date = cashbook.date,
        profit_percentage = cashbook.profit_percentage,
        category_id = cashbook.category_id,
        user_id = current_user.id
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
async def list_cashbook(current_user : str = Depends(get_current_user)):

        cashbook = session.query(Cashbook).filter(Cashbook.user_id == current_user.id).all()

        print(cashbook)
        
        return jsonable_encoder(cashbook)

## Update CashBook 

@inventory_router.put("/cashbook/update/{id}")
async def update_cashbook(id : int , cashbook : Cash_book,current_user : int = Depends(get_current_user)):
    cashbook_to_update = session.query(Cashbook).filter(and_(Cashbook.id == id,Cashbook.user_id == current_user.id)).first()
    cashbook_to_update.sell_amount = cashbook.sell_amount
    cashbook_to_update.date = cashbook.date
    cashbook_to_update.profit_percentage = cashbook.profit_percentage
    cashbook_to_update.category_id = cashbook.category_id
    

    session.commit()

    response={
    "sell_amount" : cashbook.sell_amount,
    "date" : cashbook.date,
    "profit_percentage" : cashbook.profit_percentage,
    "category_id" : cashbook.category_id,
        }
    
    return jsonable_encoder (response)


## Delete CashBook Entries
@inventory_router.delete("/cashbook/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_cashbook(id:int,current_user : int = Depends(get_current_user)):
    cashbook_to_delete = session.query(Cashbook).filter(and_(Cashbook.id == id, Cashbook.user_id == current_user.id)).first()
    
    session.delete(cashbook_to_delete)

    session.commit()

    return cashbook_to_delete


## Add Product

@inventory_router.post("/invent/add",status_code=status.HTTP_201_CREATED)
async def create_inventory(invent: Invent,current_user : int = Depends(get_current_user)):

    new_invent  = Inventory(
        product_name = invent.product_name,
        quantity = invent.quantity,
        purchaseFrom = invent.purchaseFrom,
        manufacture = invent.manufacture,
        expiry = invent.expiry,
        amount = invent.amount,
        total = invent.total,
        close = invent.close,
        user_id = current_user.id
    )
    session.add(new_invent)

    session.commit()    

    session.refresh(new_invent)


    response = {
        "product_name" : new_invent.product_name,
        "quantity" : new_invent.quantity,
        "purchaseFrom" : new_invent.purchaseFrom,
        "manufacture" : new_invent.manufacture,
        "expiry" : new_invent.expiry,
        "amount" : new_invent.amount,
        "total" : new_invent.total,
        "close" : new_invent.close
    }

    return jsonable_encoder(response)

## Show Inventory

@inventory_router.get("/invent/list")
async def list_inventory(current_user: User = Depends(get_current_user)):

        inventories = session.query(Inventory).filter(Inventory.user_id == current_user.id).all()

        return jsonable_encoder(inventories)


## Update Inventory

@inventory_router.put("/invent/update/{id}")
async def update_inventory(id : int , invent : Invent,current_user : int = Depends(get_current_user)):
    inventory_to_update = session.query(Inventory).filter(and_(Inventory.id == id,Inventory.user_id == current_user.id)).first()

    inventory_to_update.product_name = invent.product_name
    inventory_to_update.quantity = invent.quantity
    inventory_to_update.purchaseFrom = invent.purchaseFrom
    inventory_to_update.manufacture = invent.manufacture
    inventory_to_update.expiry = invent.expiry
    inventory_to_update.amount = invent.amount
    inventory_to_update.total = invent.total
    inventory_to_update.close = invent.close

    session.commit()

    response={
    "product_name" : invent.product_name,
    "quantity" : invent.quantity,
    "purchaseFrom" : invent.purchaseFrom,
    "manufacture" : invent.manufacture,
    "expiry" : invent.expiry,
    "amount" : invent.amount,
    "total" : invent.total,
    "close" : invent.close,
        }
    
    return jsonable_encoder (response)


## Delete Inventory

@inventory_router.delete("/invent/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_inventory(id:int,current_user: User = Depends(get_current_user)):
    inventory_to_delete = session.query(Inventory).filter(and_(Inventory.id == id, Inventory.user_id == current_user.id)).first()
    
    session.delete(inventory_to_delete)

    session.commit()

    return inventory_to_delete


## List expiry product

@inventory_router.get("/invent/expiry", status_code=status.HTTP_200_OK)
async def search_expiry(product_name : str | None = None,
                        current_user: User = Depends(get_current_user)):
    
    products = session.query(Inventory).filter(and_((Inventory.expiry - date.today()) <= 120  
                                                    ,Inventory.user_id == current_user.id,
                                                    or_(
                                                    Inventory.product_name == product_name if product_name is not None else True,
                                                        )    
                                                    )).all()
    return jsonable_encoder(products)