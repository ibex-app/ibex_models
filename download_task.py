from pydantic import BaseModel
from ibex_models import Platform, Post
from uuid import UUID
from typing import Optional, List

class DownloadTask(BaseModel):
    post_ids: List[UUID]
    platform: Platform
    meida_url: Optional[str]