from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.address import Address, AddressCreate
from app.models import Address as AddressModel

router = APIRouter(prefix="/addresses", tags=["addresses"])

@router.get("/client/{client_id}", response_model=list[Address])
def get_client_addresses(client_id: int, db: Session = Depends(get_db)):
    addresses = db.query(AddressModel).filter(AddressModel.client_id == client_id).all()
    return addresses

@router.post("/", response_model=Address)
def create_address(address: AddressCreate, db: Session = Depends(get_db)):
    db_address = AddressModel(**address.dict())
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

@router.put("/{address_id}", response_model=Address)
def update_address(address_id: int, address_data: dict, db: Session = Depends(get_db)):
    address = db.query(AddressModel).filter(AddressModel.address_id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
    for key, value in address_data.items():
        setattr(address, key, value)
    
    db.commit()
    db.refresh(address)
    return address

@router.delete("/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = db.query(AddressModel).filter(AddressModel.address_id == address_id).first()
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    
    db.delete(address)
    db.commit()
    return {"message": "Address deleted successfully"}