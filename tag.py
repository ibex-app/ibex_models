from enum import Enum
from typing import List, Optional

from beanie import Document
# from __future__ import annotations
from pydantic import Field
from uuid import UUID, uuid4

class TagType(str, Enum):
    topic = 'topic'
    person = 'person' 
    organization = 'organization'
    object = 'object'
    location = 'location'
    hate_speech = 'hate speech'
    conciliatory = 'conciliatory'
    neutral = 'neutral'
    aggressive = 'aggressive'
    negative = 'negative'
    incitement = 'incitement'
    positive = 'positive'
    territorial_conflict = 'territorial conflict'
    historical_issue = 'historical issue'

class Tag(Document):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    type: TagType
    title: str
    alias: Optional[List[str]]
    img_url: Optional[str]
    location: Optional[object]
    related_tags:Optional[List[UUID]]
    meta_data: Optional[object]

    class Config:  
        use_enum_values = True
        validate_assignment = True
        arbitrary_types_allowed = True

    class Collection:
        name = "tags"
