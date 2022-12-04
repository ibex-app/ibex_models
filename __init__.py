from ibex_models.platform import Platform
from ibex_models.collect_action import CollectAction
from ibex_models.account import Account
from ibex_models.search_term import SearchTerm
from ibex_models.media_status import MediaStatus
from ibex_models.post import Post, Scores, Transcript, Labels
from ibex_models.tag import Tag, TagType
from ibex_models.annotation import TextForAnnotation, Annotation, Annotations
from ibex_models.monitor import Monitor, MonitorStatus
from ibex_models.collect_task import CollectTask, CollectTaskStatus
from ibex_models.download_task import DownloadTask
from ibex_models.processor import Processor
from ibex_models.process_task import ProcessTask
from ibex_models.process_task_batch import ProcessTaskBatch




model_classes = [
    CollectAction,
    CollectTask,
    Account,
    Platform,
    Processor,
    Post,
    Scores,
    Transcript,
    Labels,
    SearchTerm,
    DownloadTask,
    ProcessTask,
    ProcessTaskBatch,
    MediaStatus,
    Tag,
    TagType,
    MonitorStatus,
    Monitor,
    TextForAnnotation,
    Annotation,
    Annotations,
    CollectTaskStatus
]
