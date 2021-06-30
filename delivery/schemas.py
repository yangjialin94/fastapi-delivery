from pydantic import BaseModel, PositiveInt
from typing import List, Optional

class DeliveryItem(BaseModel):
    delivery_document_number: PositiveInt
    item_number: str
    product_number: str
    delivery_uom: str
    gross_weight: float
    gross_weight_unit: str
    created_by_user: str
    created_date: int
    alert: str

class DeliveryItemList(BaseModel):
    delivery_items: List[DeliveryItem]
    delivery_items_count: int

class Delivery(BaseModel):
    created_by_user: str
    delivery_document_number: PositiveInt
    estimated_delivery_date: int
    shipping_point: str
    sales_organization: str
    delivery_type: str
    goods_issue_date: str
    loading_date: str
    delivery_date: Optional[int]
    picking_date: Optional[int]
    sd_document_category: str
    shipping_conditions: str
    customer_number: str
    sold_to_number: str
    net_weight: float
    weight_unit: str
    transportation_group: str
    proposed_billing_type: str
    billing_date: Optional[int]
    sd_document_currency: str
    billing_type: str
    items: List[DeliveryItem]

class DeliveryList(BaseModel):
    deliveries: List[Delivery]
    deliveries_count: int
