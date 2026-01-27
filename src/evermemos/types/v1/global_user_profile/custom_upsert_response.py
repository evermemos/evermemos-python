# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["CustomUpsertResponse"]


class CustomUpsertResponse(BaseModel):
    """Upsert custom profile response

    Response for upsert custom profile API.
    """

    success: bool
    """Whether the operation was successful"""

    data: Optional[Dict[str, object]] = None
    """Created/updated profile data"""

    message: Optional[str] = None
    """Message"""
