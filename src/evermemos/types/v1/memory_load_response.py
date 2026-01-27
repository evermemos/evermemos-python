# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MemoryLoadResponse"]


class MemoryLoadResponse(BaseModel):
    """Batch import response."""

    imported_meta: Optional[bool] = None
    """Whether conversation metadata was imported."""

    message: Optional[str] = None
    """Status message."""

    request_id: Optional[str] = None
    """Request ID of the last imported message."""

    status: Optional[str] = None
    """Queue status."""

    total_count: Optional[int] = None
    """Total number of messages."""
