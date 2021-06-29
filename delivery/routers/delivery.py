from fastapi import APIRouter, status
from typing import List
from ..schemas import Delivery
from ..repository import delivery

router = APIRouter(prefix="/delivery", tags=["Delivery"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Delivery])
def all():
    return delivery.get_all()
