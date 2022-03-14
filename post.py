from datetime import datetime
from typing import Optional, List
from pydantic import Field
from uuid import UUID, uuid4

from beanie import Document, Indexed
from pydantic import BaseModel

from ibex_models import Platform, MediaStatus



class Labels(BaseModel):
    topics: Optional[List[str]]
    persons: Optional[List[UUID]]
    organizations: Optional[List[str]]
    locations: Optional[List[UUID]]
    


class Scores(BaseModel):
    likes: Optional[int]
    views: Optional[int]
    engagement: Optional[int]
    shares: Optional[int]
    sad: Optional[int]
    wow: Optional[int]
    love: Optional[int]
    angry: Optional[int]


class Transcript(BaseModel):
    second: int
    text: str


class Post(Document):
    # id: UUID = Field(default_factory=uuid4, alias='_id')
    title: str
    text: str
    created_at: datetime
    platform: Platform
    platform_id: str
    data_source_id: Optional[UUID]
    author_platform_id: Optional[str]
    hate_speech: Optional[float]
    sentiment: Optional[float]
    has_video: Optional[bool]
    api_dump: dict
    url:Optional[str]
    media_status: Optional[MediaStatus]
    monitor_ids: List[UUID] = []
    image_url: Optional[str]

    labels: Optional[Labels]
    scores: Optional[Scores]
    transcripts: Optional[List[Transcript]]

    class Config:
        use_enum_values = True
        validate_assignment = True

    class Collection:
        name = 'posts'  
