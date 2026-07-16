from sqlalchemy.orm import Session
from app.models.reservation import Reservation
from app.schemas.reservation import ReservationCreate

def create_reservation(db: Session, reservation: ReservationCreate) -> Reservation:
    db_reservation = Reservation(
        patient_name=reservation.patient_name,
        reserved_at=reservation.reserved_at,
        
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation