import { addToCart }
from "../api/cartApi";

export default function ProductCard({
  product
}) {

  const handleAddToCart =
  async () => {

    try {

      await addToCart(
        product.id
      );

      alert(
        "Added To Cart"
      );

    }
    catch {

      alert(
        "Please Login"
      );

    }
  };

  return (

    <div
      style={{
        border:"1px solid #ddd",
        padding:"10px",
        margin:"10px"
      }}
    >

      <img
        src={product.image_url}
        width="200"
      />

      <h3>
        {product.title}
      </h3>

      <p>
        ₹ {product.price}
      </p>

      <button
        onClick={
          handleAddToCart
        }
      >
        Add To Cart
      </button>

    </div>
  );
}