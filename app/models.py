import uuid

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.db import Base


class UserStory(Base):
    __tablename__ = "user_stories"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False)
