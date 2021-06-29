from fastapi import FastAPI
from .routers import delivery

app = FastAPI()

app.include_router(delivery.router)
