from fastapi import APIRouter

inventory_router = APIRouter(
    prefix="/inventory",
    tags=['Inventory']
)
