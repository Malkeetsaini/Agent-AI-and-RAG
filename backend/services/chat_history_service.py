from backend.models.chat_history import (
    ChatHistory
)


def save_chat_message(
    db,
    user_id,
    role,
    message
):

    chat = ChatHistory(
        user_id=user_id,
        role=role,
        message=message
    )

    db.add(chat)

    db.commit()

    db.refresh(chat)

    return chat



def get_recent_messages(
    db,
    user_id,
    limit=10
):

    messages = db.query(
        ChatHistory
    ).filter(
        ChatHistory.user_id == user_id
    ).order_by(
        ChatHistory.id.desc()
    ).limit(limit).all()

    return list(
        reversed(messages)
    )



def build_recent_chat_context(
    messages
):

    context = ""

    for msg in messages:

        context += (
            f"{msg.role}: "
            f"{msg.message}\n"
        )

    return context


def get_message_count(
    db,
    user_id
):

    return db.query(
        ChatHistory
    ).filter(
        ChatHistory.user_id == user_id
    ).count()