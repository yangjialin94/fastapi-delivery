from fastapi import FastAPI
from .routers import delivery, delivery_item

app = FastAPI()

app.include_router(delivery.router)
app.include_router(delivery_item.router)
