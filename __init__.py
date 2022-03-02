from ibex_models.collect_action import CollectAction
from ibex_models.collect_task import CollectTask
from ibex_models.download_task import DownloadTask
from ibex_models.process_task import ProcessTask
from ibex_models.search_term import SearchTerm
from ibex_models.datasource import DataSource
from ibex_models.platform import Platform
from ibex_models.processor import Processor
from ibex_models.media_download_status import MediaDownloadStatus
from ibex_models.post import Post, Scores, Transcript, Labels
from ibex_models.tag import Tag
from ibex_models.monitor import Monitor

from ibex_models.annotation import TextForAnnotation, Annotation, Annotations
from ibex_models.monitor import Monitor



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
    Monitor,
    TextForAnnotation, 
    Annotation, 
    Annotations
]