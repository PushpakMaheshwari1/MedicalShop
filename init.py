from database import engine,Base
from models import User,Category,Inventory,Cashbook

Base.metadata.create_all(bind=engine) 