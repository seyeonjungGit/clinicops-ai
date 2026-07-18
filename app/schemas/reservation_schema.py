from datetime import datetime
from pydantic import BaseModel

# Post(생성)
class ReservationCreate(BaseModel):
    patient_name: str
    reserved_at: datetime

# 응답(Response)
class ReservationResponse(BaseModel):
    id: int 
    patient_name:str
    reserved_at: datetime
    status:str
    model_config = {
        "from_attributes": True
    }

# PUT(수정)
class ReservationUpdate(BaseModel):
    patient_name: str
    reserved_at: datetime



