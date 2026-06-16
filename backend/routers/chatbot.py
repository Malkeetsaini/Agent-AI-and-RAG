from fastapi import (APIRouter, Depends)

from backend.schemas.chatbot import (
    ChatRequest
)

from sqlalchemy.orm import Session

from backend.middleware.auth_middleware import (
    get_current_user
)

from backend.utils.dependencies import (
    get_db
)

from backend.services.chatbot_service import (
    chat_agent
)

router = APIRouter(
    prefix="/chat",
    tags=["AI Agent"]
)


@router.post("/")
def chat(
    payload: ChatRequest,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    return chat_agent(
        db=db,
        user_id=current_user.id,
        message=payload.message
    )