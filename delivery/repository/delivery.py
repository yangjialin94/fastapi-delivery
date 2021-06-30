import json
from fastapi import status
from .parse import parse_deliveries, parse_delivery, parse_delivery_items, parse_delivery_item
from ..sap import async_request

async def list_deliveries():
    # response = await async_request(
    #             method="GET",
    #             url="deliveries",
    #             params={
    #                 "$expand": "item",
    #             },
    #             expected_status=status.HTTP_200_OK,
    #         )
    response = json.loads(open ("delivery/data/deliveries.json", "r").read())
  
    return parse_deliveries(response)

async def get_delivery(bill_doc_num):
    # response = await async_request(
    #             method="GET",
    #             url=f"deliveries('{bill_doc_num}')",
    #             params={
    #                 "$expand": "item",
    #             },
    #             expected_status=status.HTTP_200_OK,
    #         )
    response = json.loads(open ("delivery/data/delivery.json", "r").read())["d"]
	
    return parse_delivery(response)

async def list_delivery_items(bill_doc_num):
    # response = await async_request(
    #             method="GET",
    #             url=f"deliveries('{bill_doc_num}')/item",
    #             params={},
    #             expected_status=status.HTTP_200_OK,
    #         )
    response = json.loads(open ("delivery/data/delivery_items.json", "r").read())
    
    return parse_delivery_items(response)

async def get_delivery_item(bill_doc_num, item_num):
    # response = await async_request(
    #             method="GET",
    #             url=f"deliveries(delivery_document_number='{bill_doc_num}', item_number='{item_num}')",
    #             params={},
    #             expected_status=status.HTTP_200_OK,
    #         )
    response = json.loads(open ("delivery/data/delivery_item.json", "r").read())["d"]
	
    return parse_delivery_item(response)
