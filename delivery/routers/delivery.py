from fastapi import APIRouter, status
from typing import List
from ..schemas import Delivery, DeliveryList, DeliveryItem, DeliveryItemList
from ..repository import delivery

router = APIRouter(prefix="/delivery", tags=["Delivery"])

@router.get("/", status_code=status.HTTP_200_OK, response_model=DeliveryList, name="Billing:List-Bills")
async def list_deliveries():
    return await delivery.list_deliveries()

@router.get("/{bill_doc_num}", status_code=status.HTTP_200_OK, response_model=Delivery, name="Billing:Read-Bill")
async def get_delivery(bill_doc_num):
    return await delivery.get_delivery(bill_doc_num)

@router.get("/{bill_doc_num}/items", status_code=status.HTTP_200_OK, response_model=DeliveryItemList, name="Billing:List-Bill-Items")
async def list_delivery_items(bill_doc_num):
    return await delivery.list_delivery_items(bill_doc_num)

@router.get("/{bill_doc_num}/items/{item_num}", status_code=status.HTTP_200_OK, response_model=DeliveryItem, name="Billing:Read-Bill-Item")
async def get_delivery_item(bill_doc_num, item_num):
    return await delivery.get_delivery_item(bill_doc_num, item_num)
