from pydantic import BaseModel
from typing import Optional, List
from ibex_models import Account, Platform, SearchTerm
from datetime import datetime
from uuid import UUID
from pydantic import Field
from uuid import UUID, uuid4
from beanie import Document
# from __future__ import annotations

from enum import Enum

class CollectTaskStatus(str, Enum):
    initialized = "initialized"
    is_running = "is-running"
    finalized = "finalized"
    failed = "failed"


class CollectTask(Document):
    # executor: str
    id: UUID = Field(default_factory=uuid4, alias='_id')
    date_from: datetime
    date_to: datetime
    platform: Optional[Platform]
    accounts: Optional[List[Account]]
    search_terms: Optional[List[SearchTerm]]
    search_term_ids: Optional[List[UUID]]
    account_ids: Optional[List[UUID]]
    monitor_id: Optional[UUID]
    query: Optional[str]
    hits_count: Optional[int]
    status: Optional[CollectTaskStatus] = CollectTaskStatus.initialized
    env: str

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
