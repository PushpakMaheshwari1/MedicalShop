from database import Base
from sqlalchemy import Column,Integer,Text,String,Date,ForeignKey,Float,Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(50),unique=True)
    email = Column(String(75),unique=True)
    password = Column(Text,nullable=False)

    inventories = relationship('Inventory', back_populates='user')
    cashbooks = relationship('Cashbook', back_populates='user')

    def __repr__(self):
        return  f"<User {self.username}>"
    
class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer,primary_key=True)
    name = Column(String(75))

    cashbooks = relationship('Cashbook', back_populates='category')


class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer,primary_key=True)
    product_name = Column(String(75))
    quantity = Column(Integer)
    purchaseFrom = Column(String(100))
    manufacture = Column(String(100))
    expiry = Column(Date)
    amount = Column(Float)
    total = Column(Float)
    close = Column(Boolean)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='inventories')

    def __repr__(self):
        return  f"<Product {self.product_name}>"
    
class Cashbook(Base):
    __tablename__ = 'cashbook'
    id = Column(Integer,primary_key=True)
    sell_amount = Column(Float)
    date = Column(Date)
    profit_percentage = Column(Float)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='cashbooks')

    category_id = Column(Integer, ForeignKey('category.id'))
    category = relationship('Category', back_populates='cashbooks')