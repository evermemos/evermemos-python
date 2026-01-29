# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["ConversationMetaGetResponse", "Result"]


class Result(BaseModel):
    id: str

    conversation_created_at: str

    name: str

    scene: str

    created_at: Optional[str] = None

    default_timezone: Optional[str] = None

    group_id: Optional[str] = None

    is_default: Optional[bool] = None

    scene_desc: Optional[Dict[str, object]] = None

    tags: Optional[List[str]] = None

    updated_at: Optional[str] = None

    user_details: Optional[Dict[str, Dict[str, object]]] = None


class ConversationMetaGetResponse(BaseModel):
    result: Result

    message: Optional[str] = None

    status: Optional[str] = None
