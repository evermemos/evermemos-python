# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["CustomUpsertParams", "CustomProfileData"]


class CustomUpsertParams(TypedDict, total=False):
    custom_profile_data: Required[CustomProfileData]
    """Custom profile data to upsert"""

    user_id: Required[str]
    """User ID"""


class CustomProfileData(TypedDict, total=False):
    """Custom profile data to upsert"""

    initial_profile: Required[SequenceNotStr[str]]
    """List of profile sentences describing the user"""
