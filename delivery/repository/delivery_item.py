import re

from fastapi import status
from ..sap import async_request
from ..schemas import DeliveryItem, DeliveryItemList

async def list_all():
    response = {
        "d": {
            "results": [
                {
                    "__metadata": {
                        "id": "http://100.114.10.77:8000/sap/opu/odata/sap/ZNUVE_SRV/delivery_items(delivery_document_number='80000000',item_number='000010')",
                        "uri": "http://100.114.10.77:8000/sap/opu/odata/sap/ZNUVE_SRV/delivery_items(delivery_document_number='80000000',item_number='000010')",
                        "type": "ZNUVE_SRV.delivery_item"
                    },
                    "delivery_document_number": "80000000",
                    "item_number": "000010",
                    "product_number": "2",
                    "delivery_uom": "EA",
                    "gross_weight": "1.000",
                    "gross_weight_unit": "KG",
                    "created_by_user": "NLARA",
                    "created_date": "/Date(1612504799000)/",
                    "alert": ""
                },
                {
                    "__metadata": {
                        "id": "http://100.114.10.77:8000/sap/opu/odata/sap/ZNUVE_SRV/delivery_items(delivery_document_number='80000002',item_number='000010')",
                        "uri": "http://100.114.10.77:8000/sap/opu/odata/sap/ZNUVE_SRV/delivery_items(delivery_document_number='80000002',item_number='000010')",
                        "type": "ZNUVE_SRV.delivery_item"
                    },
                    "delivery_document_number": "80000002",
                    "item_number": "000010",
                    "product_number": "2",
                    "delivery_uom": "EA",
                    "gross_weight": "15.000",
                    "gross_weight_unit": "KG",
                    "created_by_user": "NLARA",
                    "created_date": "/Date(1612504799000)/",
                    "alert": ""
                },
                {
                    "__metadata": {
                        "id": "http://100.114.10.77:8000/sap/opu/odata/sap/ZNUVE_SRV/delivery_items(delivery_document_number='80000003',item_number='000010')",
                        "uri": "http://100.114.10.77:8000/sap/opu/odata/sap/ZNUVE_SRV/delivery_items(delivery_document_number='80000003',item_number='000010')",
                        "type": "ZNUVE_SRV.delivery_item"
                    },
                    "delivery_document_number": "80000003",
                    "item_number": "000010",
                    "product_number": "2",
                    "delivery_uom": "EA",
                    "gross_weight": "9.000",
                    "gross_weight_unit": "KG",
                    "created_by_user": "NLARA",
                    "created_date": "/Date(1612504799000)/",
                    "alert": ""
                }
            ]
        }
    }
	
    return parse_delivery_items(response)

def parse_delivery_items(data: dict):
    data = data["d"]["results"]
    delivery_items = list(map(parse_delivery_item, data))
    return DeliveryItemList(delivery_items=delivery_items, delivery_items_count=len(delivery_items))

def parse_delivery_item(data: dict):
    return DeliveryItem(
        delivery_document_number=int(data["delivery_document_number"]),
        item_number=data["item_number"],
        product_number=data["product_number"],
        delivery_uom=data["delivery_uom"],
        gross_weight=float(data["gross_weight"]),
        gross_weight_unit=data["gross_weight_unit"],
        created_by_user=data["created_by_user"],
        created_date=parse_sap_date(data["created_date"]),
        alert=data["alert"]
    )

def parse_sap_date(date: str):
    regex = re.compile('/Date[(]([0-9]+)[)]/$')
    match = regex.match(date)

    if match is None:
        raise Exception('Bad date: "%s"' %(date))
    try:
        date = int(match.groups()[0])
    except TypeError:
        raise Exception('Bade date: "%s"' %(date))
    return date