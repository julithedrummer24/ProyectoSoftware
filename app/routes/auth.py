from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import AuthBase
from app.crud import auth as auth_crud
from app.database import get_db

router = APIRouter()

@router.post("/login")
async def login(auth: AuthBase, db: AsyncSession = Depends(get_db)):
    return await auth_crud.authenticate_user(db, auth)