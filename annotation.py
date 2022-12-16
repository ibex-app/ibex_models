from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import Field, BaseModel
from uuid import UUID, uuid4
from beanie import Document


class TextForAnnotation(Document):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    post_id: Optional[UUID]
    words: List[str]

    class Collection:
        name = 'text_for_annotation'

class Annotation(BaseModel):
    tag_id: int
    label: str
    words: List[int]
    relation: Optional[str]
    labelGrup: str


class Annotations(Document):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    text_id: UUID
    user_mail: str
    created_at: Optional[datetime] = datetime.now()
    annotations: Optional[List[Annotation]]

    class Collection:
        name = 'annotations'
