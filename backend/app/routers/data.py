from fastapi import APIRouter
from backend.app.services.data_service import get_sample_data

router = APIRouter()

@router.get("/sample")
def read_sample():
    return get_sample_data()
