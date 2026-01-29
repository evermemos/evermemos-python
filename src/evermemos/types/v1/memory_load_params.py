# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MemoryLoadParams", "ConversationMeta", "ConversationList"]


class MemoryLoadParams(TypedDict, total=False):
    conversation_meta: Required[ConversationMeta]

    conversation_list: Optional[Iterable[ConversationList]]

    version: Optional[str]


class ConversationMeta(TypedDict, total=False):
    group_id: Required[str]

    created_at: Optional[str]

    default_timezone: Optional[str]

    name: Optional[str]

    scene: Optional[str]

    scene_desc: Optional[Dict[str, object]]

    tags: Optional[SequenceNotStr[str]]

    user_details: Optional[Dict[str, object]]


class ConversationList(TypedDict, total=False):
    content: Optional[str]

    create_time: Union[str, int, None]

    extra: Optional[Dict[str, object]]

    message_id: Optional[str]

    refer_list: Optional[Iterable[Dict[str, object]]]

    role: Optional[str]

    sender: Optional[str]

    sender_name: Optional[str]

    type: Optional[str]
