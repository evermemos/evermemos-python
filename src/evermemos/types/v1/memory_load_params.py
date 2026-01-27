# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["MemoryLoadParams", "ConversationMeta", "ConversationList"]


class MemoryLoadParams(TypedDict, total=False):
    conversation_meta: Required[ConversationMeta]
    """Conversation metadata for batch import."""

    conversation_list: Optional[Iterable[ConversationList]]
    """Message list."""

    version: Optional[str]
    """Format version."""


class ConversationMeta(TypedDict, total=False):
    """Conversation metadata for batch import."""

    group_id: Required[str]
    """Conversation group ID (unique)."""

    created_at: Optional[str]
    """Conversation creation time (ISO 8601)."""

    default_timezone: Optional[str]
    """Default timezone."""

    description: Optional[str]
    """Conversation description."""

    name: Optional[str]
    """Conversation name."""

    scene: Optional[str]
    """Scene type (e.g., assistant, group_chat)."""

    scene_desc: Optional[Dict[str, object]]
    """Scene description object."""

    tags: Optional[SequenceNotStr[str]]
    """Tags for the conversation."""

    user_details: Optional[Dict[str, object]]
    """User details map keyed by user ID."""


class ConversationList(TypedDict, total=False):
    """Message item for batch import."""

    content: Optional[str]
    """Message content."""

    create_time: Union[str, int, None]
    """Creation time (ISO 8601 or timestamp)."""

    extra: Optional[Dict[str, object]]
    """Additional data."""

    message_id: Optional[str]
    """Message ID."""

    refer_list: Optional[Iterable[Dict[str, object]]]
    """Referenced messages."""

    role: Optional[str]
    """Role (e.g., user, assistant)."""

    sender: Optional[str]
    """Sender ID."""

    sender_name: Optional[str]
    """Sender name."""

    type: Optional[str]
    """Message type (e.g., text, image)."""
