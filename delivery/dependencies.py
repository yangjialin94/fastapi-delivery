from fastapi import Query
from .schemas import DEFAULT_SALES_LIMIT, DEFAULT_SALES_OFFSET, DeliveriesFilters

def get_deliveries_filters(limit: int = Query(DEFAULT_SALES_LIMIT, ge=1), offset: int = Query(DEFAULT_SALES_OFFSET, ge=0)):
    return DeliveriesFilters(
        limit = limit,
        offset = offset  
    )
