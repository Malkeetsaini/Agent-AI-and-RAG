__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import chromadb

from backend.database.session import SessionLocal

from backend.models.product import Product

from backend.embeddings.product_embedding import (
    get_product_embedding
)

client = chromadb.PersistentClient(
    path="backend/chroma_db"
)

collection = client.get_or_create_collection(
    name="products"
)


def generate_product_embeddings():

    db = SessionLocal()

    #products = db.query(Product).all()
    products = db.query(Product).filter(Product.embed == 0).limit(900).all()


    print(
        f"Found {len(products)} products"
    )

    for product in products:

        if product.image_url is None:
            product.image_url = "";
            print('wrong data')
            print(product.id)

        text = f"""
        {product.title}
        {product.description}
        {product.tags}
        {product.category}
        """
        print(product.id);
        # embedding = get_product_embedding(
        #     text
        # )

        embedding = list(
            get_product_embedding(text)
        )

        collection.add(

            ids=[str(product.id)],

            embeddings=[embedding],

            documents=[text],

            metadatas=[
                {
                    "product_id":
                    product.id,

                    "title":
                    product.title,

                    "category":
                    product.category,

                    "image_url":
                    product.image_url
                }
            ]
        )

        db.query(Product).filter(Product.id == product.id).update({Product.embed: 1})
        db.commit()

    db.close()

    print(
        "Embeddings Generated Successfully"
    )


if __name__ == "__main__":

    generate_product_embeddings()