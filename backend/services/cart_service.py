from sqlalchemy.orm import Session

from backend.models.cart import Cart
from backend.models.cart_item import CartItem
from backend.models.product import Product


def add_to_cart(
    db: Session,
    user_id: int,
    product_id: int,
    quantity: int
):

    cart = (
        db.query(Cart)
        .filter(
            Cart.user_id == user_id
        )
        .first()
    )

    if not cart:

        cart = Cart(
            user_id=user_id
        )

        db.add(cart)

        db.commit()

        db.refresh(cart)

    existing_item = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id,
            CartItem.product_id == product_id
        )
        .first()
    )

    if existing_item:

        existing_item.quantity += quantity

        db.commit()

        return {
            "message":
            "Cart Updated"
        }

    item = CartItem(
        cart_id=cart.id,
        product_id=product_id,
        quantity=quantity
    )

    db.add(item)

    db.commit()

    return {
        "message":
        "Added To Cart"
    }


def get_cart(
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

        return []

    items = (
        db.query(CartItem)
        .filter(
            CartItem.cart_id == cart.id
        )
        .all()
    )

    result = []

    for item in items:

        product = (
            db.query(Product)
            .filter(
                Product.id ==
                item.product_id
            )
            .first()
        )

        result.append({
            "cart_item_id":
            item.id,

            "product_id":
            product.id,

            "title":
            product.title,

            "price":
            getattr(
                product,
                "price",
                None
            ),

            "quantity":
            item.quantity
        })

    return result


def remove_from_cart(
    db: Session,
    cart_item_id: int
):

    item = (
        db.query(CartItem)
        .filter(
            CartItem.id ==
            cart_item_id
        )
        .first()
    )

    if not item:

        return {
            "message":
            "Item Not Found"
        }

    db.delete(item)

    db.commit()

    return {
        "message":
        "Removed Successfully"
    }