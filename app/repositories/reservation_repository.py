from sqlalchemy.orm import Session
from app.models.reservation_model import Reservation
from app.schemas.reservation_schema import ReservationCreate, ReservationUpdate

def create_reservation(db: Session, reservation: ReservationCreate) -> Reservation:
    db_reservation = Reservation(
        patient_name=reservation.patient_name,
        reserved_at=reservation.reserved_at,
        
    )
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation

def get_reservations(db: Session):
    return db.query(Reservation).all()

def get_reservation(db: Session, reservation_id: int):
    return (db.query(Reservation)
            .filter(Reservation.id == reservation_id)
            .first()
    )

def update_reservation(
    db: Session,
    reservation_id: int,
    reservation_update: ReservationUpdate
):
    reservation = (
    db.query(Reservation)
      .filter(Reservation.id == reservation_id)
      .first()
)

