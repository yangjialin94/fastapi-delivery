import re
from ..schemas import Delivery, DeliveryList, DeliveryItem, DeliveryItemList

def parse_sap_date(date: str):
    regex = re.compile("/Date[(]([0-9]+)[)]/$")
    match = regex.match(date)

    if match is None:
        raise Exception(f"Bad date: {date}")

    try:
        date = int(match.groups()[0])
    except TypeError:
        raise Exception(f"Bad date: {date}")
        
    return date


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

def parse_delivery_items(data: dict):
    delivery_items = list(map(parse_delivery_item, data["d"]["results"]))
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
