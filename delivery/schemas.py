from pydantic import BaseModel

class Delivery(BaseModel):
    created_by_user: str
    delivery_document_number: str
    estimated_delivery_date: str
    shipping_point: str
    sales_organization: str
    delivery_type: str
    goods_issue_date: str
    loading_date: str
    delivery_date: str
    picking_date: str
    sd_document_category: str
    shipping_conditions: str
    customer_number: str
    sold_to_number: str
    net_weight: str
    weight_unit: str
    transportation_group: str
    proposed_billing_type: str
    billing_date: str
    sd_document_currency: str
    billing_type: str
