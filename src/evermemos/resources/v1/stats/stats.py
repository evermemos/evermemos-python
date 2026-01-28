# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .request import (
    RequestResource,
    AsyncRequestResource,
    RequestResourceWithRawResponse,
    AsyncRequestResourceWithRawResponse,
    RequestResourceWithStreamingResponse,
    AsyncRequestResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["StatsResource", "AsyncStatsResource"]


class StatsResource(SyncAPIResource):
    @cached_property
    def request(self) -> RequestResource:
        return RequestResource(self._client)

    @cached_property
    def with_raw_response(self) -> StatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/evermemos-python#accessing-raw-response-data-eg-headers
        """
        return StatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/evermemos-python#with_streaming_response
        """
        return StatsResourceWithStreamingResponse(self)


class AsyncStatsResource(AsyncAPIResource):
    @cached_property
    def request(self) -> AsyncRequestResource:
        return AsyncRequestResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/evermemos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/evermemos-python#with_streaming_response
        """
        return AsyncStatsResourceWithStreamingResponse(self)


class StatsResourceWithRawResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

    @cached_property
    def request(self) -> RequestResourceWithRawResponse:
        return RequestResourceWithRawResponse(self._stats.request)


class AsyncStatsResourceWithRawResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

    @cached_property
    def request(self) -> AsyncRequestResourceWithRawResponse:
        return AsyncRequestResourceWithRawResponse(self._stats.request)


class StatsResourceWithStreamingResponse:
    def __init__(self, stats: StatsResource) -> None:
        self._stats = stats

    @cached_property
    def request(self) -> RequestResourceWithStreamingResponse:
        return RequestResourceWithStreamingResponse(self._stats.request)


class AsyncStatsResourceWithStreamingResponse:
    def __init__(self, stats: AsyncStatsResource) -> None:
        self._stats = stats

    @cached_property
    def request(self) -> AsyncRequestResourceWithStreamingResponse:
        return AsyncRequestResourceWithStreamingResponse(self._stats.request)
