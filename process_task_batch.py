from pydantic import BaseModel
from ibex_models import Processor, Post
from uuid import UUID
from typing import List

class ProcessTaskBatch(BaseModel):
    # posts: List[Post]
    processor: Processor
    monitor_id: UUID
    env: str
