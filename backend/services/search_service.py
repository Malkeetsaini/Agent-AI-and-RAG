__import__("pysqlite3")
import sys

sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")

import chromadb

from backend.embeddings.product_embedding import (
    get_product_embedding
)

client = chromadb.PersistentClient(
    path="backend/chroma_db"
)

collection = client.get_collection(
    name="products"
)


def semantic_search(
    query: str,
    top_k: int = 10
):

    query_embedding = (
        get_product_embedding(query)
    )

    results = collection.query(

        query_embeddings=[
            query_embedding
        ],

        n_results=top_k
    )

    response = []

    ids = results["ids"][0]
    metas = results["metadatas"][0]
    distances = results["distances"][0]

    for i in range(len(ids)):

        response.append({

            "product_id":
            ids[i],

            "title":
            metas[i]["title"],

            "category":
            metas[i]["category"],

            "image_url":
            metas[i]["image_url"],

            "similarity":
            round(
                1 - distances[i],
                4
            )
        })

    return response