from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.repositories.reservation import create_reservation
from app.schemas.reservation import ReservationCreate, ReservationResponse


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
    return create_reservation(db, reservation)
