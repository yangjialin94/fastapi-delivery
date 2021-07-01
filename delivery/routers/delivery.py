from fastapi import APIRouter, Depends, status
from typing import List
from ..schemas import Delivery, DeliveryList, DeliveryItem, DeliveryItemList, DeliveriesFilters
from ..repository import delivery
from ..dependencies import get_deliveries_filters

router = APIRouter(prefix="/deliveries", tags=["Delivery"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=DeliveryList, name="Billing:List-Bills")
async def list_deliveries(deliveries_filters: DeliveriesFilters = Depends(get_deliveries_filters)):
    return await delivery.list_deliveries(deliveries_filters)

@router.get("/{bill_doc_num}", status_code=status.HTTP_200_OK, response_model=Delivery, name="Billing:Read-Bill")
async def get_delivery(bill_doc_num):
    return await delivery.get_delivery(bill_doc_num)

@router.get("/{bill_doc_num}/items", status_code=status.HTTP_200_OK, response_model=DeliveryItemList, name="Billing:List-Bill-Items")
async def list_delivery_items(bill_doc_num):
    return await delivery.list_delivery_items(bill_doc_num)

@router.get("/{bill_doc_num}/items/{item_num}", status_code=status.HTTP_200_OK, response_model=DeliveryItem, name="Billing:Read-Bill-Item")
async def get_delivery_item(bill_doc_num, item_num):
    return await delivery.get_delivery_item(bill_doc_num, item_num)
