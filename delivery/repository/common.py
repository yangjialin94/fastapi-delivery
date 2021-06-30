import re

from ..schemas import DeliveryItem

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
