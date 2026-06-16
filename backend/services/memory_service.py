from backend.models.conversation_memory import (
    ConversationMemory
)

from backend.services.chat_history_service import (
    get_recent_messages,
    get_message_count
)

from backend.services.summary_service import (
    generate_summary
)


def get_memory(
    db,
    user_id
):

    memory = db.query(
        ConversationMemory
    ).filter(
        ConversationMemory.user_id == user_id
    ).first()

    return memory


def save_memory(
    db,
    user_id,
    summary
):

    memory = db.query(
        ConversationMemory
    ).filter(
        ConversationMemory.user_id == user_id
    ).first()

    if memory:

        memory.summary = summary

    else:

        memory = ConversationMemory(
            user_id=user_id,
            summary=summary
        )

        db.add(memory)

    db.commit()



def update_memory_if_needed(
    db,
    user_id
):

    count = get_message_count(
        db,
        user_id
    )

    # every 20 messages
    if count % 20 != 0:
        return

    memory = get_memory(
        db,
        user_id
    )

    old_summary = ""

    if memory:
        old_summary = memory.summary

    recent_messages = get_recent_messages(
        db,
        user_id,
        limit=20
    )

    conversation_text = ""

    for msg in recent_messages:

        conversation_text += (
            f"{msg.role}: "
            f"{msg.message}\n"
        )

    new_summary = generate_summary(
        old_summary,
        conversation_text
    )

    save_memory(
        db,
        user_id,
        new_summary
    )