from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.models import UserStory
from app.schemas import UserStoryCreate, UserStoryResponse

router = APIRouter()


@router.post("/stories/", response_model=UserStoryResponse)
def create_story(story: UserStoryCreate, db: Session = Depends(get_db)):
    """Create a new user story.

    Args:
        story (UserStoryCreate): The user story to create.
        db (Session): Database session.

    Returns:
        UserStoryResponse: The created story.
    """
    db_story = UserStory(**story.model_dump())
    db.add(db_story)
    db.commit()
    db.refresh(db_story)
    return db_story


@router.get("/stories/", response_model=list[UserStoryResponse])
def read_stories(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_db)
):
    """List at  most 10 user stories.

    Args:
        skip (int): The number of stories to skip.
        limit (int): The maximum number of stories to list.
        db (Session): Database session.

    Returns:
        db: Database session containing list of user stories.
    """
    return db.query(UserStory).offset(skip).limit(limit).all()


@router.get("/stories/{story_id}", response_model=UserStoryResponse)
def read_story(story_id: UUID, db: Session = Depends(get_db)):
    story = db.query(UserStory).filter(UserStory.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    return story


@router.delete("/stories/{story_id}", status_code=204)
def delete_story(story_id: UUID, db: Session = Depends(get_db)):
    story = db.query(UserStory).filter(UserStory.id == story_id).first()
    if not story:
        raise HTTPException(status_code=404, detail="Story not found")
    db.delete(story)
    db.commit()
