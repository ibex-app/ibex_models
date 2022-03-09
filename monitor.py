from typing import List, Optional

from beanie import Document
from pydantic import Field
from uuid import UUID, uuid4
from datetime import datetime

class Monitor(Document):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    title: str
    descr: str
    collect_actions: List[UUID]
    date_from: datetime
    date_to: Optional[datetime]

    class Collection:
        name = "monitors"
