from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..models import user_model
from ..schemas import user as user_schema
from ..utilities.schemas import get_db

router = APIRouter(prefix="/user",tags=['Users'])

# Creating User
@router.post("/", status_code = status.HTTP_201_CREATED)
def create_user(request: user_schema.CreateUser, db: Session = Depends(get_db)):
    user = user_model.User(name=request.name,birth_date=request.birth_date,gender=request.gender)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Dispalying all users
@router.get("/users", response_model=List[user_schema.ShowUser])
def get_users(db: Session = Depends(get_db)):
    users = db.query(user_model.User).all()
    return users

# Displaying specific user based on id
@router.get("/{user_id}", response_model=user_schema.ShowUser)
def get_user(user_id, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id).first()

# Showing error if user doesn't exist
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {user_id} doesn't exist")
    return user


# Updating user
@router.put("/{user_id}", response_model=user_schema.ShowUser)
def update_user(user_id, request: user_schema.UpdateUser, db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == user_id)
    user.name = request.name
    user.birth_date = request.birth_date

# Showing error if user doesn't exist

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    user.update(request.dict())
    db.commit()
    return "updated user"


# Deleting user
@router.delete("/{user_id}")
def delete_user(id:int,db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.id == id)

# Showing error if user doesn't exist

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} not found")

    user.delete(synchronize_session = 'fetch')
    db.commit()
    return "deleted user"
