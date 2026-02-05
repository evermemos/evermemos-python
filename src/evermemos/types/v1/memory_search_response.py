# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .metadata import Metadata
from ..._models import BaseModel
from .memory_type import MemoryType

__all__ = [
    "MemorySearchResponse",
    "Result",
    "ResultMemory",
    "ResultMemoryEpisodeMemory",
    "ResultMemoryEventLog",
    "ResultMemoryForesight",
    "ResultPendingMessage",
]


class ResultMemoryEpisodeMemory(BaseModel):
    memory_type: Union[MemoryType, str]

    timestamp: datetime

    user_id: str

    id: Optional[str] = None

    episode: Optional[str] = None

    extend: Optional[Dict[str, object]] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    keywords: Optional[List[str]] = None

    linked_entities: Optional[List[str]] = None

    ori_event_id_list: Optional[List[str]] = None

    original_data: Optional[List[Dict[str, object]]] = None

    parent_id: Optional[str] = None

    parent_type: Optional[str] = None

    participants: Optional[List[str]] = None

    score: Optional[float] = None

    subject: Optional[str] = None

    summary: Optional[str] = None

    type: Optional[Literal["Conversation"]] = None

    user_name: Optional[str] = None

    vector: Optional[List[float]] = None

    vector_model: Optional[str] = None


class ResultMemoryEventLog(BaseModel):
    memory_type: Union[MemoryType, str]

    timestamp: datetime

    user_id: str

    id: Optional[str] = None

    atomic_fact: Union[str, List[str], None] = None

    extend: Optional[Dict[str, object]] = None

    fact_embeddings: Optional[List[List[float]]] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    keywords: Optional[List[str]] = None

    linked_entities: Optional[List[str]] = None

    ori_event_id_list: Optional[List[str]] = None

    original_data: Optional[List[Dict[str, object]]] = None

    parent_id: Optional[str] = None

    parent_type: Optional[str] = None

    participants: Optional[List[str]] = None

    score: Optional[float] = None

    time: Optional[str] = None

    type: Optional[Literal["Conversation"]] = None

    user_name: Optional[str] = None

    vector: Optional[List[float]] = None

    vector_model: Optional[str] = None


class ResultMemoryForesight(BaseModel):
    memory_type: Union[MemoryType, str]

    timestamp: datetime

    user_id: str

    id: Optional[str] = None

    duration_days: Optional[int] = None

    end_time: Optional[str] = None

    evidence: Optional[str] = None

    extend: Optional[Dict[str, object]] = None

    foresight: Optional[str] = None

    group_id: Optional[str] = None

    group_name: Optional[str] = None

    keywords: Optional[List[str]] = None

    linked_entities: Optional[List[str]] = None

    ori_event_id_list: Optional[List[str]] = None

    original_data: Optional[List[Dict[str, object]]] = None

    parent_id: Optional[str] = None

    parent_type: Optional[str] = None

    participants: Optional[List[str]] = None

    score: Optional[float] = None

    start_time: Optional[str] = None

    type: Optional[Literal["Conversation"]] = None

    user_name: Optional[str] = None

    vector: Optional[List[float]] = None

    vector_model: Optional[str] = None


ResultMemory: TypeAlias = Union[ResultMemoryEpisodeMemory, ResultMemoryEventLog, ResultMemoryForesight]


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
