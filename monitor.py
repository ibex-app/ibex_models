from typing import List

from beanie import Document
from pydantic import Field
from uuid import UUID, uuid4
from ibex_models import CollectAction

class Monitor(Document):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    title: str
    descr: str
    collect_actions: List[UUID]

    class Collection:
        name = "monitors"
