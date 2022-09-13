from pydantic import BaseModel
from ibex_models import Processor, Post
from uuid import UUID

class ProcessTask(BaseModel):
    post: Post
    processor: Processor
    monitor_id: UUID
