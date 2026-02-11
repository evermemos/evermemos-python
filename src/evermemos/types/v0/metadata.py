# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["Metadata"]


class Metadata(BaseModel):
    memory_types: List[str]

    source: str

    user_id: str

    email: Optional[str] = None

    full_name: Optional[str] = None

    group_ids: Optional[List[str]] = None

    phone: Optional[str] = None
