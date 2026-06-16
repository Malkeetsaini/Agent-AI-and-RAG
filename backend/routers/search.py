from fastapi import APIRouter

from backend.schemas.search import (
    SearchRequest
)

from backend.services.search_service import (
    semantic_search
)

router = APIRouter(
    prefix="/search",
    tags=["Semantic Search"]
)


@router.post("/")
def search(
    payload: SearchRequest
):

    return semantic_search(
        payload.query,
        payload.top_k
    )