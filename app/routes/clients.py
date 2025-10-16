from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.client import Client, ClientCreate
from app.models import Client as ClientModel

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/", response_model=list[Client])
def get_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = db.query(ClientModel).offset(skip).limit(limit).all()
    return clients

@router.get("/{client_id}", response_model=Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.client_id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.post("/", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_db)):
    db_client = ClientModel(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

@router.put("/{client_id}", response_model=Client)
def update_client(client_id: int, client_data: dict, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.client_id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    for key, value in client_data.items():
        setattr(client, key, value)
    
    db.commit()
    db.refresh(client)
    return client

@router.delete("/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(ClientModel).filter(ClientModel.client_id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    
    db.delete(client)
    db.commit()
    return {"message": "Client deleted successfully"}