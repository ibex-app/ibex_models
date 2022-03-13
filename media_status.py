from enum import Enum

class MediaStatus(str, Enum):
    to_be_downloaded = 'to_be_downloaded'
    downloaded = 'downloaded'
    no_download = 'no_download'
    processed = 'processed'