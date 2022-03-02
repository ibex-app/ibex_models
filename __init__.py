from app.model.collect_action import CollectAction
from app.model.collect_task import CollectTask
from app.model.download_task import DownloadTask
from app.model.process_task import ProcessTask
from app.model.search_term import SearchTerm
from app.model.datasource import DataSource
from app.model.platform import Platform
from app.model.processor import Processor
from app.model.media_download_status import MediaDownloadStatus
from app.model.post import Post, Scores, Transcript, Labels
from app.model.tag import Tag
from app.model.monitor import Monitor


model_classes = [
    CollectAction,
    CollectTask,
    DataSource,
    Platform,
    Post,
    Scores,
    Transcript,
    Labels,
    SearchTerm,
    DownloadTask,
    ProcessTask,
    Processor,
    MediaDownloadStatus,
    Tag,
    Monitor
]
