from fastapi import FastAPI
from auth_routes import auth_router
from inventory_routes import inventory_router
from fastapi_pagination import add_pagination


app = FastAPI()

add_pagination(app)
app.include_router(auth_router)
app.include_router(inventory_router)