from fastapi import APIRouter,status
from database import Session,engine
from schemas import Product_Category,Cash_book,Invent
from models import Category,Cashbook,Inventory
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
async def delete_category(id:int):
    category_to_delete = session.query(Category).filter(Category.id == id).first()
    
    session.delete(category_to_delete)

    session.commit()

    return category_to_delete


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
async def list_cashbook():
        cashbook = session.query(Cashbook).all()
        
        return jsonable_encoder(cashbook)

## Update CashBook 

@inventory_router.put("/inventory/update/{id}",)
async def update_cashbook(id : int , cashbook : Cash_book):
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

## Update CashBook 

@inventory_router.put("/inventory/update/{id}",)
async def update_cashbook(id : int , cashbook : Cash_book):
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
async def delete_cashbook(id:int):
    cashbook_to_delete = session.query(Cashbook).filter(Cashbook.id == id).first()
    
    session.delete(cashbook_to_delete)

    session.commit()

    return cashbook_to_delete
 


## Add Product

@inventory_router.post("/invent/add",status_code=status.HTTP_201_CREATED)
async def create_inventory(invent: Invent):
    new_invent  = Inventory(
        product_name = invent.product_name,
        quantity = invent.quantity,
        purchaseFrom = invent.purchaseFrom,
        manufacture = invent.manufacture,
        expiry = invent.expiry,
        amount = invent.amount,
        total = invent.total,
        close = invent.close
    )
    session.add(new_invent)

    session.commit()    

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
async def list_inventory():
        inventories = session.query(Inventory).all()

        return jsonable_encoder(inventories)


## Update Inventory

@inventory_router.put("/invent/update/{id}")
async def update_inventory(id : int , cashbook : Cash_book):
    inventory_to_update = session.query(Cashbook).filter(Cashbook.id == id).first()

    inventory_to_update.product_name = cashbook.product_name
    inventory_to_update.quantity = cashbook.quantity
    inventory_to_update.purchaseFrom = cashbook.purchaseFrom
    inventory_to_update.manufacture = cashbook.manufacture
    inventory_to_update.expiry = cashbook.expiry
    inventory_to_update.amount = cashbook.amount
    inventory_to_update.total = cashbook.total
    inventory_to_update.close = cashbook.close

    session.commit()

    response={
    "product_name" : cashbook.product_name,
    "quantity" : cashbook.quantity,
    "purchaseFrom" : cashbook.purchaseFrom,
    "manufacture" : cashbook.manufacture,
    "expiry" : cashbook.expiry,
    "amount" : cashbook.amount,
    "total" : cashbook.total,
    "close" : cashbook.close,
        }
    
    return jsonable_encoder (response)



## Delete Inventory

@inventory_router.delete("/invent/delete/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_inventory(id:int):
    inventory_to_delete = session.query(Inventory).filter(Inventory.id == id).first()
    
    session.delete(inventory_to_delete)

    session.commit()

    return inventory_to_delete
