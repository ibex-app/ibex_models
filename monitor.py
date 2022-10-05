from typing import List, Optional

from beanie import Document
from pydantic import Field
from uuid import UUID, uuid4
from datetime import datetime

from enum import Enum

class MonitorStatus(int, Enum):
    initialized = 0
    sampling = 1
    sampled = 2
    live = 3
    collecting = 4
    collected = 5
    finalized = 6


class Monitor(Document):
    id: UUID = Field(default_factory=uuid4, alias='_id')
    title: str
    descr: str
    collect_actions: List[UUID]
    date_from: datetime
    date_to: Optional[datetime]
    status: MonitorStatus = MonitorStatus.initialized

    class Collection:
        name = "monitors"
