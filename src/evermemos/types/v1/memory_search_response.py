# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .metadata import Metadata
from ..._models import BaseModel

__all__ = ["MemorySearchResponse", "Result", "ResultPendingMessage"]


class ResultPendingMessage(BaseModel):
    """Pending message that has not yet been extracted into memory.

    Represents a cached message waiting for boundary detection or memory extraction.
    """

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

    importance_scores: Optional[List[float]] = None

    memories: Optional[List[Dict[str, List[object]]]] = None

    metadata: Optional[Metadata] = None

    original_data: Optional[List[Dict[str, List[Dict[str, object]]]]] = None

    pending_messages: Optional[List[ResultPendingMessage]] = None

    query_metadata: Optional[Metadata] = None

    scores: Optional[List[Dict[str, List[float]]]] = None

    total_count: Optional[int] = None


class MemorySearchResponse(BaseModel):
    """Memory search API response

    Response for GET /api/v1/memories/search endpoint.
    """

    result: Result
    """Memory search result"""

    message: Optional[str] = None
    """Response message"""

    status: Optional[str] = None
    """Response status"""
