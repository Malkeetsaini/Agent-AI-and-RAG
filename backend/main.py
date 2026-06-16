from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database.base import Base
from backend.database.connection import engine
from backend.models.user import User

from backend.routers.products import router as product_router

from backend.routers.auth import (
    router as auth_router
)

from backend.models.cart import Cart
from backend.models.cart_item import CartItem

from backend.models.order import Order
from backend.models.order_item import OrderItem

from backend.routers.cart import (
    router as cart_router
)

from backend.routers.orders import (
    router as order_router
)

from backend.middleware.logging_middleware import (
    log_requests
)

from backend.routers.search import (
    router as search_router
)

from backend.routers.chatbot import (
    router as chatbot_router
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Shopping API"
)

app.include_router(product_router)
app.include_router(
    auth_router
)

app.include_router(
    cart_router
)

app.include_router(
    order_router
)

app.middleware("http")(
    log_requests
)

app.include_router(
    search_router
)

app.include_router(
    chatbot_router
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health_check():

    return {
        "message": "API Running"
    }