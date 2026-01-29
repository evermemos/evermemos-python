# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["MemoryLoadResponse"]


class MemoryLoadResponse(BaseModel):
    imported_meta: Optional[bool] = None

    message: Optional[str] = None

    request_id: Optional[str] = None

    status: Optional[str] = None

    total_count: Optional[int] = None
