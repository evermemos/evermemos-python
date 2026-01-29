# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import TypedDict

from ...._types import SequenceNotStr

__all__ = ["ConversationMetaUpdateParams", "UserDetails"]


class ConversationMetaUpdateParams(TypedDict, total=False):
    default_timezone: Optional[str]

    group_id: Optional[str]

    name: Optional[str]

    scene_desc: Optional[Dict[str, object]]

    tags: Optional[SequenceNotStr[str]]

    user_details: Optional[Dict[str, UserDetails]]


class UserDetails(TypedDict, total=False):
    custom_role: Optional[str]

    extra: Optional[Dict[str, object]]

    full_name: Optional[str]

    role: Optional[str]
