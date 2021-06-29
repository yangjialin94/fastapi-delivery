from fastapi import status
from ..sap import async_request

async def list_all():
    response = await async_request(
                method="GET",
                url="deliveries",
                params={
                    "$expand": "item",
                },
                expected_status=status.HTTP_200_OK,
            )
	
    return response
