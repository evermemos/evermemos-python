# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MemoryDeleteResponse", "Result"]


class Result(BaseModel):
    count: Optional[int] = None

    filters: Optional[List[str]] = None


class MemoryDeleteResponse(BaseModel):
    result: Result

    message: Optional[str] = None

    status: Optional[str] = None
