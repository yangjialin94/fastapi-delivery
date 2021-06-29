from fastapi import APIRouter, status
from ..schemas import DeliveryItem
from ..repository import delivery_item

router = APIRouter(prefix="/delivery_item", tags=["Delivery Item"])

@router.get("/", status_code=status.HTTP_200_OK)
# @router.get("/", status_code=status.HTTP_200_OK, response_model=List[DeliveryItem])
async def list_delivery_items():
    return await delivery_item.list_all()
