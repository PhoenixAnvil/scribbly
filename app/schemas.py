from uuid import UUID

from pydantic import BaseModel, ConfigDict


# Request schema for creating a user story
class UserStoryCreate(BaseModel):
    title: str
    description: str


# Response schema for sending a story back to the client
class UserStoryResponse(UserStoryCreate):
    id: UUID

    model_config = ConfigDict(from_attributes=True)
