import aiohttp
from fastapi import Depends, status, HTTPException

JY_IP = "100.114.10.77"
NL_IP = "100.93.197.117"
BASE_URL = f"http://{NL_IP}:8000/sap/opu/odata/sap/ZNUVE_SRV"
AUTH = aiohttp.BasicAuth("nlara", "10xCoding!")

async def async_request(method, url, params, expected_status):
    url = BASE_URL + f"/{url}"
    headers = {
            "Accept": "application/json",
        }
    
    async with aiohttp.ClientSession() as session:
        async with session.request(method=method, url=url, params=params, headers=headers, auth=AUTH) as response:
            if response.status != expected_status:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Delivery not found"
                )
            return await response.text()
