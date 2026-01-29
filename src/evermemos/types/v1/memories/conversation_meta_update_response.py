# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ConversationMetaUpdateResponse", "Result"]


class Result(BaseModel):
    id: str

    group_id: Optional[str] = None

    name: Optional[str] = None

    scene: Optional[str] = None

    updated_at: Optional[str] = None

    updated_fields: Optional[List[str]] = None


class ConversationMetaUpdateResponse(BaseModel):
    result: Result

    message: Optional[str] = None

    status: Optional[str] = None
