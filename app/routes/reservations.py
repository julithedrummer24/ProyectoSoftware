from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.reservation import Reservation, ReservationCreate
from app.models import Reservation as ReservationModel

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/", response_model=list[Reservation])
def get_reservations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    reservations = db.query(ReservationModel).offset(skip).limit(limit).all()
    return reservations

@router.get("/{reservation_id}", response_model=Reservation)
def get_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(ReservationModel).filter(ReservationModel.reservation_id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return reservation

@router.get("/client/{client_id}", response_model=list[Reservation])
def get_client_reservations(client_id: int, db: Session = Depends(get_db)):
    
    reservations = db.query(ReservationModel).join(
        ClientStaffReservationModel,
        ReservationModel.reservation_id == ClientStaffReservationModel.reservation_id
    ).filter(ClientStaffReservationModel.client_id == client_id).all()
    return reservations

@router.get("/staff/{staff_id}", response_model=list[Reservation])
def get_staff_reservations(staff_id: int, db: Session = Depends(get_db)):
    
    reservations = db.query(ReservationModel).join(
        ClientStaffReservationModel,
        ReservationModel.reservation_id == ClientStaffReservationModel.reservation_id
    ).filter(ClientStaffReservationModel.staff_id == staff_id).all()
    return reservations

@router.post("/", response_model=Reservation)
def create_reservation(reservation: ReservationCreate, db: Session = Depends(get_db)):
    db_reservation = ReservationModel(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

@router.put("/{reservation_id}", response_model=Reservation)
def update_reservation(reservation_id: int, reservation_data: dict, db: Session = Depends(get_db)):
    reservation = db.query(ReservationModel).filter(ReservationModel.reservation_id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    for key, value in reservation_data.items():
        setattr(reservation, key, value)
    
    db.commit()
    db.refresh(reservation)
    return reservation

@router.delete("/{reservation_id}")
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    reservation = db.query(ReservationModel).filter(ReservationModel.reservation_id == reservation_id).first()
    if not reservation:
        raise HTTPException(status_code=404, detail="Reservation not found")
    
    db.delete(reservation)
    db.commit()
    return {"message": "Reservation deleted successfully"}