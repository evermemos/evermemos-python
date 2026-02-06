# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .metadata import Metadata
from ..._models import BaseModel

__all__ = [
    "MemorySearchResponse",
    "Result",
    "ResultMemory",
    "ResultMemoryEpisodicMemoryModel",
    "ResultMemoryEventLogModel",
    "ResultMemoryForesightModel",
    "ResultPendingMessage",
]


class ResultMemoryEpisodicMemoryModel(BaseModel):
    id: str

    episode_id: str

    user_id: str

    created_at: Optional[datetime] = None

    end_time: Optional[datetime] = None

    episode: Optional[str] = None

    extend: Optional[Dict[str, object]] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    keywords: Optional[List[str]] = None

    location: Optional[str] = None

    metadata: Optional[Metadata] = None

    parent_id: Optional[str] = None

    parent_type: Optional[str] = None

    participants: Optional[List[str]] = None

    start_time: Optional[datetime] = None

    subject: Optional[str] = None

    summary: Optional[str] = None

    timestamp: Optional[datetime] = None

    updated_at: Optional[datetime] = None


class ResultMemoryEventLogModel(BaseModel):
    id: str

    atomic_fact: str

    parent_id: str

    parent_type: str

    timestamp: datetime

    user_id: str

    created_at: Optional[datetime] = None

    event_type: Optional[str] = None

    extend: Optional[Dict[str, object]] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    metadata: Optional[Metadata] = None

    participants: Optional[List[str]] = None

    updated_at: Optional[datetime] = None

    user_name: Optional[str] = None

    vector: Optional[List[float]] = None

    vector_model: Optional[str] = None


class ResultMemoryForesightModel(BaseModel):
    id: str

    content: str

    foresight: str

    parent_id: str

    parent_type: str

    created_at: Optional[datetime] = None

    duration_days: Optional[int] = None

    end_time: Optional[str] = None

    evidence: Optional[str] = None

    extend: Optional[Dict[str, object]] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    metadata: Optional[Metadata] = None

    participants: Optional[List[str]] = None

    start_time: Optional[str] = None

    updated_at: Optional[datetime] = None

    user_id: Optional[str] = None

    user_name: Optional[str] = None

    vector: Optional[List[float]] = None

    vector_model: Optional[str] = None


ResultMemory: TypeAlias = Union[ResultMemoryEpisodicMemoryModel, ResultMemoryEventLogModel, ResultMemoryForesightModel]


class ResultPendingMessage(BaseModel):
    id: str

    request_id: str

    content: Optional[str] = None

    created_at: Optional[str] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    message_create_time: Optional[str] = None

    message_id: Optional[str] = None

    refer_list: Optional[List[str]] = None

    sender: Optional[str] = None

    sender_name: Optional[str] = None

    updated_at: Optional[str] = None

    user_id: Optional[str] = None


class Result(BaseModel):
    """Memory search result"""

    has_more: Optional[bool] = None

    memories: Optional[List[ResultMemory]] = None

    metadata: Optional[Metadata] = None

    pending_messages: Optional[List[ResultPendingMessage]] = None

    query_metadata: Optional[Metadata] = None

    total_count: Optional[int] = None


class MemorySearchResponse(BaseModel):
    result: Result
    """Memory search result"""

    message: Optional[str] = None
    """Response message"""

    status: Optional[str] = None
    """Response status"""
