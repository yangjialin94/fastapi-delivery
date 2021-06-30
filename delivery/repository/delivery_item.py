from fastapi import status
from ..sap import async_request
from ..schemas import DeliveryItem, DeliveryItemList
from .common import parse_delivery_item

async def list_all():
    # response = await async_request(
    #             method="GET",
    #             url="delivery_items",
    #             params={},
    #             expected_status=status.HTTP_200_OK,
    #         )
    
    # return parse_delivery_items(response)

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
    delivery_items = list(map(parse_delivery_item, data["d"]["results"]))
    return DeliveryItemList(delivery_items=delivery_items, delivery_items_count=len(delivery_items))
