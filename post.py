from datetime import datetime
from typing import Optional, List
from pydantic import Field
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import BaseModel

from ibex_models import Platform, MediaStatus
from ibex_models.processor import Processor

class Labels(BaseModel):
    topics: Optional[List[str]]
    persons: Optional[List[UUID]]
    organizations: Optional[List[str]]
    locations: Optional[List[UUID]]
        
class Scores(BaseModel):
    likes: Optional[int]
    dislikes: Optional[int]
    views: Optional[int]
    engagement: Optional[int]
    shares: Optional[int]
    sad: Optional[int]
    wow: Optional[int]
    love: Optional[int]
    angry: Optional[int]
    comments: Optional[int]
    other: Optional[int]
    
    total: Optional[int]


class Transcript(BaseModel):
    second: float
    text: str


class Post(Document):
    # id: UUID = Field(default_factory=uuid4, alias='_id')
    title: str
    text: str
    created_at: datetime
    platform: Platform
    platform_id: str
    account_id: Optional[UUID]
    search_term_ids: Optional[List[UUID]]
    author_platform_id: Optional[str]
    hate_speech: Optional[float]
    sentiment: Optional[float]
    has_video: Optional[bool]
    api_dump: dict
    url:Optional[str]
    media_status: Optional[MediaStatus]
    monitor_ids: List[UUID] = []
    image_url: Optional[str]
    language: Optional[str]
    process_applied: Optional[List[Processor]]
    
    tag_ids: Optional[UUID]
    scores: Optional[Scores]
    transcripts: Optional[List[Transcript]]
    
    
    def getEngagement(self):
        score = 0
        for k,v in vars(self.scores).items():
            if not v is None:
                score += v
        return score#np.sum(vars(self.scores).values())
    
    def to_dict(self):
        return vars(self)
    
    def full_string(self):
        text = f'{self.api_dump}'
        if self.transcripts and len(self.transcripts):
            text += ' '.join([transcript.text for transcript in self.transcripts])
        return text

    
    class Config:
        use_enum_values = True
        validate_assignment = True

    class Collection:
        name = 'posts'  
