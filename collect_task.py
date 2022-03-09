from pydantic import BaseModel
from typing import Optional, List
from ibex_models import DataSource, Platform, SearchTerm
from datetime import datetime
from uuid import UUID
from pydantic import Field
from uuid import UUID, uuid4
from beanie import Document
# from __future__ import annotations


class CollectTask(Document):
    # executor: str
    id: UUID = Field(default_factory=uuid4, alias='_id')
    date_from: datetime
    date_to: datetime
    platform: Optional[Platform]
    data_sources: Optional[List[DataSource]]
    search_terms: Optional[List[SearchTerm]]
    monitor_id: UUID
    query: Optional[str]
    hits_count: Optional[int]

    sample: bool = False

    class Config:  
        use_enum_values = True
        validate_assignment = True

    class Collection:
        name = "collect_tasks"
