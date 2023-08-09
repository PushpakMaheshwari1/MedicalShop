from fastapi import APIRouter,status,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm
from models import User
from schemas import Base_User,Login
from database import Session,engine
from fastapi.encoders import jsonable_encoder
from hashing import hash_password,verify_password
from tokens import create_access_token


auth_router = APIRouter(
    prefix="/auth",
    tags=['AUTHENTICATION']
)

session = Session(bind = engine)


@auth_router.post('/users',status_code = status.HTTP_201_CREATED)
async def create_user(user:Base_User):

    password = hash_password(user.password)

    new_user = User(
        username = user.username,
        email = user.email,
        password = password,
    )
    session.add(new_user)

    session.commit()

    session.refresh(new_user)

    user = {
        "username" : user.username,
        "email" : user.email 
    }

    return jsonable_encoder(user)


@auth_router.post('/login')
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = session.query(User).filter(User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Invalid Credentials")

    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Incorrect password")
    
    access_token = create_access_token(data={"sub": str(user.id)})
    return {"access_token": access_token, "token_type": "bearer"}
