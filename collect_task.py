from pydantic import BaseModel
from typing import Optional, List
from ibex_models import Account, Platform, SearchTerm
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
    accounts: Optional[List[Account]]
    search_terms: Optional[List[SearchTerm]]
    monitor_id: UUID
    query: Optional[str]
    hits_count: Optional[int]

    # Sample attribute indicates how much posts are collected for the specific query
    # if the value is True, only the fraction of all avaliable posts are collected
    sample: bool = False
    # if the get_hits_count attrcibute value is True, only hits count would be fetched, w/o posts 
    get_hits_count: Optional[bool] 

    class Config:  
        use_enum_values = True
        validate_assignment = True

    class Collection:
        name = "collect_tasks"
