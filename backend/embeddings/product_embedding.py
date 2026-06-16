# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )


# def get_product_embedding(text: str):

#     return model.encode(text).tolist()


import os

from google import genai
from google.genai import types

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_product_embedding(text: str):

    response = client.models.embed_content(
        model="models/gemini-embedding-001",

        contents=text,

        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    return response.embeddings[0].values


def get_query_embedding(query: str):

    response = client.models.embed_content(
        model="models/gemini-embedding-001",

        contents=query,

        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    return response.embeddings[0].values