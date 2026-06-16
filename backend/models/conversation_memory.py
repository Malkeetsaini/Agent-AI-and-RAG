from sqlalchemy import *

from backend.database.base import Base


class ConversationMemory(Base):

    __tablename__ = "conversation_memory"

    id = Column(
        Integer,
        primary_key=True
    )

    user_id = Column(
        Integer,
        unique=True
    )

    summary = Column(
        Text
    )