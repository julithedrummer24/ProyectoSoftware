from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import BusinessStaff, BusinessStaffCreate
from app.models import BusinessStaff as BusinessStaffModel

router = APIRouter(prefix="/staff", tags=["staff"])

@router.get("/", response_model=list[BusinessStaff])
def get_all_staff(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    staff = db.query(BusinessStaffModel).offset(skip).limit(limit).all()
    return staff

@router.get("/business/{business_id}", response_model=list[BusinessStaff])
def get_business_staff(business_id: int, db: Session = Depends(get_db)):
    staff = db.query(BusinessStaffModel).filter(BusinessStaffModel.business_id == business_id).all()
    return staff

@router.post("/", response_model=BusinessStaff)
def create_staff(staff: BusinessStaffCreate, db: Session = Depends(get_db)):
    db_staff = BusinessStaffModel(**staff.dict())
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

@router.put("/{staff_id}", response_model=BusinessStaff)
def update_staff(staff_id: int, staff_data: dict, db: Session = Depends(get_db)):
    staff = db.query(BusinessStaffModel).filter(BusinessStaffModel.staff_id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    
    for key, value in staff_data.items():
        setattr(staff, key, value)
    
    db.commit()
    db.refresh(staff)
    return staff

@router.delete("/{staff_id}")
def delete_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = db.query(BusinessStaffModel).filter(BusinessStaffModel.staff_id == staff_id).first()
    if not staff:
        raise HTTPException(status_code=404, detail="Staff member not found")
    
    db.delete(staff)
    db.commit()
    return {"message": "Staff member deleted successfully"}