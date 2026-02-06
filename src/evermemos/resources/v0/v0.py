# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .status.status import (
    StatusResource,
    AsyncStatusResource,
    StatusResourceWithRawResponse,
    AsyncStatusResourceWithRawResponse,
    StatusResourceWithStreamingResponse,
    AsyncStatusResourceWithStreamingResponse,
)
from .memories.memories import (
    MemoriesResource,
    AsyncMemoriesResource,
    MemoriesResourceWithRawResponse,
    AsyncMemoriesResourceWithRawResponse,
    MemoriesResourceWithStreamingResponse,
    AsyncMemoriesResourceWithStreamingResponse,
)

__all__ = ["V0Resource", "AsyncV0Resource"]


class V0Resource(SyncAPIResource):
    @cached_property
    def memories(self) -> MemoriesResource:
        return MemoriesResource(self._client)

    @cached_property
    def status(self) -> StatusResource:
        return StatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> V0ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/evermemos-python#accessing-raw-response-data-eg-headers
        """
        return V0ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V0ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/evermemos-python#with_streaming_response
        """
        return V0ResourceWithStreamingResponse(self)


class AsyncV0Resource(AsyncAPIResource):
    @cached_property
    def memories(self) -> AsyncMemoriesResource:
        return AsyncMemoriesResource(self._client)

    @cached_property
    def status(self) -> AsyncStatusResource:
        return AsyncStatusResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV0ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/evermemos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV0ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV0ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/evermemos-python#with_streaming_response
        """
        return AsyncV0ResourceWithStreamingResponse(self)


class V0ResourceWithRawResponse:
    def __init__(self, v0: V0Resource) -> None:
        self._v0 = v0

    @cached_property
    def memories(self) -> MemoriesResourceWithRawResponse:
        return MemoriesResourceWithRawResponse(self._v0.memories)

    @cached_property
    def status(self) -> StatusResourceWithRawResponse:
        return StatusResourceWithRawResponse(self._v0.status)


class AsyncV0ResourceWithRawResponse:
    def __init__(self, v0: AsyncV0Resource) -> None:
        self._v0 = v0

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithRawResponse:
        return AsyncMemoriesResourceWithRawResponse(self._v0.memories)

    @cached_property
    def status(self) -> AsyncStatusResourceWithRawResponse:
        return AsyncStatusResourceWithRawResponse(self._v0.status)


class V0ResourceWithStreamingResponse:
    def __init__(self, v0: V0Resource) -> None:
        self._v0 = v0

    @cached_property
    def memories(self) -> MemoriesResourceWithStreamingResponse:
        return MemoriesResourceWithStreamingResponse(self._v0.memories)

    @cached_property
    def status(self) -> StatusResourceWithStreamingResponse:
        return StatusResourceWithStreamingResponse(self._v0.status)


class AsyncV0ResourceWithStreamingResponse:
    def __init__(self, v0: AsyncV0Resource) -> None:
        self._v0 = v0

    @cached_property
    def memories(self) -> AsyncMemoriesResourceWithStreamingResponse:
        return AsyncMemoriesResourceWithStreamingResponse(self._v0.memories)

    @cached_property
    def status(self) -> AsyncStatusResourceWithStreamingResponse:
        return AsyncStatusResourceWithStreamingResponse(self._v0.status)
