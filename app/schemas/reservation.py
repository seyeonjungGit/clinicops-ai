from datetime import datetime
from pydantic import BaseModel

class ReservationCreate(BaseModel):
    patient_name: str
    reserved_at: datetime

class ReservationResponse(BaseModel):
    id: int 
    patient_name:str
    reserved_at: datetime
    status:str
    model_config = {
        "from_attributes": True
    }