# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MemoryCreateParams"]


class MemoryCreateParams(TypedDict, total=False):
    content: Required[str]

    create_time: Required[str]

    message_id: Required[str]

    sender: Required[str]

    flush: bool

    group_id: Optional[str]

    group_name: Optional[str]

    refer_list: Optional[SequenceNotStr[str]]

    role: Optional[str]

    sender_name: Optional[str]
