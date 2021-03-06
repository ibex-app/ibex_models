from pydantic import BaseModel
from ibex_models import Platform, Post
from uuid import UUID
from typing import Optional

class DownloadTask(BaseModel):
    post: Post
    platform: Platform
    meida_url: Optional[str]