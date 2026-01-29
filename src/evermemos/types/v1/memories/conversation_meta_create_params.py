# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ConversationMetaCreateParams", "UserDetails"]


class ConversationMetaCreateParams(TypedDict, total=False):
    created_at: Required[str]

    name: Required[str]

    scene: Required[str]

    scene_desc: Required[Dict[str, object]]

    default_timezone: Optional[str]

    group_id: Optional[str]

    tags: Optional[SequenceNotStr[str]]

    user_details: Optional[Dict[str, UserDetails]]


class UserDetails(TypedDict, total=False):
    custom_role: Optional[str]

    extra: Optional[Dict[str, object]]

    full_name: Optional[str]

    role: Optional[str]
