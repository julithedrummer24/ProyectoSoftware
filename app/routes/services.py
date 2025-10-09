from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import Service, ServiceCreate
from app.models import Service as ServiceModel

router = APIRouter(prefix="/services", tags=["services"])

@router.get("/", response_model=list[Service])
def get_services(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    services = db.query(ServiceModel).offset(skip).limit(limit).all()
    return services

@router.get("/business/{business_id}", response_model=list[Service])
def get_business_services(business_id: int, db: Session = Depends(get_db)):
    services = db.query(ServiceModel).filter(ServiceModel.business_id == business_id).all()
    return services

@router.get("/{service_id}", response_model=Service)
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(ServiceModel).filter(ServiceModel.service_id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service

@router.post("/", response_model=Service)
def create_service(service: ServiceCreate, db: Session = Depends(get_db)):
    db_service = ServiceModel(**service.dict())
    db.add(db_service)
    db.commit()
    db.refresh(db_service)
    return db_service

@router.put("/{service_id}", response_model=Service)
def update_service(service_id: int, service_data: dict, db: Session = Depends(get_db)):
    service = db.query(ServiceModel).filter(ServiceModel.service_id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    for key, value in service_data.items():
        setattr(service, key, value)
    
    db.commit()
    db.refresh(service)
    return service

@router.delete("/{service_id}")
def delete_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(ServiceModel).filter(ServiceModel.service_id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    
    db.delete(service)
    db.commit()
    return {"message": "Service deleted successfully"}