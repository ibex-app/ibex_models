from pydantic import BaseModel
from ibex_models import Processor
from uuid import UUID

class ProcessTask(BaseModel):
    post_id: UUID
    processor: Processor