from pydantic import BaseModel
from typing import Optional, List
from ibex_models import DataSource, Platform, SearchTerm
from datetime import datetime
from uuid import UUID
# from __future__ import annotations


class CollectTask(BaseModel):
    # executor: str
    date_from: datetime
    date_to: datetime
    platform: Optional[Platform]
    data_sources: Optional[List[DataSource]]
    search_terms: Optional[List[SearchTerm]]
    monitor_id: UUID
    query: Optional[str]

    sample: bool = False
