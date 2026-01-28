# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MemoryCreateResponse"]


class MemoryCreateResponse(BaseModel):
    message: str

    request_id: str

    status: str
