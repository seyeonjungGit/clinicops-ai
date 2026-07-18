from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.services import reservation_service
from app.schemas.reservation_schema import ReservationCreate, ReservationResponse


app = FastAPI(
    title="ClinicOps AI",
    description="AI Agent 기반 한의원 업무 자동화 시스템",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "ClinicOps AI API"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
    }

@app.get("/health/db")
def health_db(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {
        "status": "ok",
        "database": "connected",
    }

@app.post("/reservations", response_model=ReservationResponse )
def create_reservation_api(
    reservation: ReservationCreate,
    db: Session = Depends(get_db)
):
    return reservation_service.create_reservation(db, reservation)

@app.get("/reservations", response_model=list[ReservationResponse])
def read_reservations(
    db: Session = Depends(get_db)
):
    return reservation_service.get_reservations(db)

@app.get("/reservations/{reservation_id}", response_model=ReservationResponse)
def get_reservation_api(
    reservation_id: int, 
    db: Session = Depends(get_db)
):
    return reservation_service.get_reservation(db,reservation_id)