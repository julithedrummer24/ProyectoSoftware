from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas import ClientStaffReservation, ClientStaffReservationCreate
from app.models import ClientStaffReservation as ClientStaffReservationModel

router = APIRouter(prefix="/reservation-assignments", tags=["reservation-assignments"])

@router.post("/", response_model=ClientStaffReservation)
def assign_reservation(assignment: ClientStaffReservationCreate, db: Session = Depends(get_db)):
    db_assignment = ClientStaffReservationModel(**assignment.dict())
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

@router.put("/{csr_id}", response_model=ClientStaffReservation)
def update_assignment(csr_id: int, assignment_data: dict, db: Session = Depends(get_db)):
    assignment = db.query(ClientStaffReservationModel).filter(ClientStaffReservationModel.csr_id == csr_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    
    for key, value in assignment_data.items():
        setattr(assignment, key, value)
    
    db.commit()
    db.refresh(assignment)
    return assignment

@router.delete("/{csr_id}")
def delete_assignment(csr_id: int, db: Session = Depends(get_db)):
    assignment = db.query(ClientStaffReservationModel).filter(ClientStaffReservationModel.csr_id == csr_id).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Assignment not found")
    
    db.delete(assignment)
    db.commit()
    return {"message": "Assignment deleted successfully"}