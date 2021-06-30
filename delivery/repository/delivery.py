from fastapi import status
from .parse import parse_deliveries, parse_delivery, parse_delivery_items, parse_delivery_item
from ..sap import async_request

async def list_deliveries():
    response = await async_request(
                method="GET",
                url="deliveries",
                params={
                    "$expand": "item",
                },
                expected_status=status.HTTP_200_OK,
            )
	
    return parse_deliveries(response)

async def get_delivery(bill_doc_num):
    response = await async_request(
                method="GET",
                url=f"deliveries('{bill_doc_num}')",
                params={
                    "$expand": "item",
                },
                expected_status=status.HTTP_200_OK,
            )
	
    return parse_delivery(response)

async def list_delivery_items(bill_doc_num):
    # response = await async_request(
    #             method="GET",
    #             url=f"deliveries('{bill_doc_num}')/item",
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

async def get_delivery_item(bill_doc_num, item_num):
    response = await async_request(
                method="GET",
                url=f"deliveries(xxx='{bill_doc_num}', xxx='{item_num}')",
                params={},
                expected_status=status.HTTP_200_OK,
            )
	
    return parse_delivery_item(response)
