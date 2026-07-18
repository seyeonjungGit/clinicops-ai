from sqlalchemy.orm import Session
from app.repositories import reservation_repository as repository
from app.schemas.reservation_schema import ReservationCreate

from fastapi import HTTPException

def create_reservation(db: Session, reservation: ReservationCreate,):
    return repository.create_reservation(db,reservation)

def get_reservations(db: Session):
    return repository.get_reservations(db)

def get_reservation(db: Session, reservation_id:int):
    reservation = repository.get_reservation(db,reservation_id)
    if reservation is None:
        raise HTTPException(status_code=404, detail="reservation not found")
    return reservation