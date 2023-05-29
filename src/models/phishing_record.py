from dataclasses import dataclass
from enum import Enum


class PhishingStatus(Enum):
    YES = 'yes'
    NO  = 'no'


@dataclass
class PhishingRecord:
    id: str
    url: str
    is_online: PhishingStatus
    target: str
