from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.business import Business, BusinessCreate
from app.models import Business as BusinessModel

router = APIRouter(prefix="/businesses", tags=["businesses"])

@router.get("/", response_model=list[Business])
def get_businesses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    businesses = db.query(BusinessModel).offset(skip).limit(limit).all()
    return businesses

@router.get("/{business_id}", response_model=Business)
def get_business(business_id: int, db: Session = Depends(get_db)):
    business = db.query(BusinessModel).filter(BusinessModel.business_id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business

@router.post("/", response_model=Business)
def create_business(business: BusinessCreate, db: Session = Depends(get_db)):
    db_business = BusinessModel(**business.dict())
    db.add(db_business)
    db.commit()
    db.refresh(db_business)
    return db_business

@router.put("/{business_id}", response_model=Business)
def update_business(business_id: int, business_data: dict, db: Session = Depends(get_db)):
    business = db.query(BusinessModel).filter(BusinessModel.business_id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    for key, value in business_data.items():
        setattr(business, key, value)
    
    db.commit()
    db.refresh(business)
    return business

@router.delete("/{business_id}")
def delete_business(business_id: int, db: Session = Depends(get_db)):
    business = db.query(BusinessModel).filter(BusinessModel.business_id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    
    db.delete(business)
    db.commit()
    return {"message": "Business deleted successfully"}