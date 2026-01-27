# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .custom import (
    CustomResource,
    AsyncCustomResource,
    CustomResourceWithRawResponse,
    AsyncCustomResourceWithRawResponse,
    CustomResourceWithStreamingResponse,
    AsyncCustomResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GlobalUserProfileResource", "AsyncGlobalUserProfileResource"]


class GlobalUserProfileResource(SyncAPIResource):
    @cached_property
    def custom(self) -> CustomResource:
        return CustomResource(self._client)

    @cached_property
    def with_raw_response(self) -> GlobalUserProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/evermemos-python#accessing-raw-response-data-eg-headers
        """
        return GlobalUserProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalUserProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/evermemos-python#with_streaming_response
        """
        return GlobalUserProfileResourceWithStreamingResponse(self)


class AsyncGlobalUserProfileResource(AsyncAPIResource):
    @cached_property
    def custom(self) -> AsyncCustomResource:
        return AsyncCustomResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGlobalUserProfileResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/evermemos/evermemos-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalUserProfileResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalUserProfileResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/evermemos/evermemos-python#with_streaming_response
        """
        return AsyncGlobalUserProfileResourceWithStreamingResponse(self)


class GlobalUserProfileResourceWithRawResponse:
    def __init__(self, global_user_profile: GlobalUserProfileResource) -> None:
        self._global_user_profile = global_user_profile

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._global_user_profile.custom)


class AsyncGlobalUserProfileResourceWithRawResponse:
    def __init__(self, global_user_profile: AsyncGlobalUserProfileResource) -> None:
        self._global_user_profile = global_user_profile

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._global_user_profile.custom)


class GlobalUserProfileResourceWithStreamingResponse:
    def __init__(self, global_user_profile: GlobalUserProfileResource) -> None:
        self._global_user_profile = global_user_profile

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._global_user_profile.custom)


class AsyncGlobalUserProfileResourceWithStreamingResponse:
    def __init__(self, global_user_profile: AsyncGlobalUserProfileResource) -> None:
        self._global_user_profile = global_user_profile

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._global_user_profile.custom)
