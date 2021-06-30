from typing import ItemsView
from fastapi import status
from ..sap import async_request
from ..schemas import Delivery, DeliveryList, DeliveryItem
from .common import parse_delivery_item

async def list_all():
    response = await async_request(
                method="GET",
                url="deliveries",
                params={
                    "$expand": "item",
                },
                expected_status=status.HTTP_200_OK,
            )
	
    return parse_deliveries(response)

def parse_deliveries(data: dict):
    deliveries = list(map(parse_delivery, data["d"]["results"]))
    return DeliveryList(deliveries=deliveries, deliveries_count=len(deliveries))

def parse_delivery(data: dict):
    items = {} if data["item"] is None else data["item"]
    return Delivery(
        created_by_user = "",
        delivery_document_number = "",
        estimated_delivery_date = "",
        shipping_point = "",
        sales_organization = "",
        delivery_type = "",
        goods_issue_date = "",
        loading_date = "",
        delivery_date = "",
        picking_date = "",
        sd_document_category = "",
        shipping_conditions = "",
        customer_number = "",
        sold_to_number = "",
        net_weight = "",
        weight_unit = "",
        transportation_group = "",
        proposed_billing_type = "",
        billing_date = "",
        sd_document_currency = "",
        billing_type = "",
        items = [parse_delivery_item(i) for i in items.get("result", [])]
    )
