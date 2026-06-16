from sqlalchemy.orm import Session

from backend.models.cart import Cart
from backend.models.cart_item import CartItem

from backend.models.order import Order
from backend.models.order_item import OrderItem

from backend.models.product import Product


def create_order(
    db: Session,
    user_id: int
):

    cart = (
        db.query(Cart)
        .filter(
            Cart.user_id == user_id
        )
        .first()
    )

    if not cart:

        return {
            "message":
            "Cart Not Found"
        }

    cart_items = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id
        )
        .all()
    )

    if len(cart_items) == 0:

        return {
            "message":
            "Cart Empty"
        }

    total_amount = 0

    order = Order(
        user_id=user_id
    )

    db.add(order)

    db.commit()

    db.refresh(order)

    for item in cart_items:

        product = (
            db.query(Product)
            .filter(
                Product.id ==
                item.product_id
            )
            .first()
        )

        price = (
            product.price
            if product.price
            else 0
        )

        total_amount += (
            price *
            item.quantity
        )

        order_item = OrderItem(

            order_id=order.id,

            product_id=product.id,

            quantity=item.quantity,

            price=price
        )

        db.add(order_item)

    order.total_amount = total_amount

    db.commit()

    # Empty Cart

    for item in cart_items:
        db.delete(item)

    db.commit()

    return {

        "message":
        "Order Created",

        "order_id":
        order.id,

        "total_amount":
        total_amount
    }


def get_orders(
    db: Session,
    user_id: int
):

    orders = (
        db.query(Order)
        .filter(
            Order.user_id == user_id
        )
        .all()
    )

    response = []

    for order in orders:

        response.append({

            "order_id":
            order.id,

            "total_amount":
            order.total_amount,

            "status":
            order.status
        })

    return response