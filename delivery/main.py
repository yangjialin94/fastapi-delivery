import os
from fastapi import FastAPI
# from fastapi.openapi.utils import get_openapi
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.staticfiles import StaticFiles
from .routers import delivery


app = FastAPI(docs_url=None, redoc_url=None)
parent_dir_path = os.path.dirname(os.path.realpath(__file__))
app.mount("/static", StaticFiles(directory=parent_dir_path + "/static"), name="static")

app.include_router(delivery.router)

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title="Delivery API Doc",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_favicon_url="/static/favicon.ico"
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title="Delivery API Redoc",
        redoc_js_url="/static/redoc.standalone.js",
    )

# def custom_openapi():
#     if app.openapi_schema:
#         return app.openapi_schema

#     openapi_schema = get_openapi(
#         title="Delivery API",
#         version="2.5.0",
#         description="This is a very custom OpenAPI schema",
#         routes=app.routes,
#     )
#     openapi_schema["info"]["x-logo"] = {
#         "url": "https://nuvecommerce.com/favicons/favicon.ico"
#     }
#     app.openapi_schema = openapi_schema

#     return app.openapi_schema


# app.openapi = custom_openapi
