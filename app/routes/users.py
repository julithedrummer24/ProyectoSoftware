from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.users import User, UserCreate, UserUpdate
from app.models.User import User as UserModel

router = APIRouter(prefix="/users", tags=["Users"])

# Obtener todos los usuarios
@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserModel).all()
    return users


# Obtener usuario por ID
@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# Crear un nuevo usuario
@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = UserModel(
        name=user.name,
        email=user.email,
        phone=user.phone,
        password=user.password,
        role="client"
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Actualizar un usuario
@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user_data: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = user_data.name
    user.email = user_data.email
    user.phone = user_data.phone
    user.password = user_data.password
    user.role = user_data.role

    db.commit()
    db.refresh(user)
    return user


# Eliminar usuario
@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}
