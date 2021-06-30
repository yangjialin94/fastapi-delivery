from fastapi import status
from ..sap import async_request
from ..schemas import Delivery, DeliveryList
from .utils import parse_sap_date

async def list_all():
    response = await async_request(
                method="GET",
                url="deliveries",
                params={
                    "$expand": "item",
                },
                expected_status=status.HTTP_200_OK,
            )
	
    return parse_deliveries(response.json())

def parse_deliveries(data: dict):
    deliveries = list(map(parse_delivery, data["d"]["results"]))
    return DeliveryList(deliveries=deliveries, deliveries_count=len(deliveries))

def parse_delivery(data: dict):
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
        items = []
    )

