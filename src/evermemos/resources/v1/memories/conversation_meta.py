# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v1.memories import conversation_meta_create_params, conversation_meta_update_params
from ....types.v1.memories.conversation_meta_get_response import ConversationMetaGetResponse
from ....types.v1.memories.conversation_meta_create_response import ConversationMetaCreateResponse
from ....types.v1.memories.conversation_meta_update_response import ConversationMetaUpdateResponse

__all__ = ["ConversationMetaResource", "AsyncConversationMetaResource"]


class ConversationMetaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConversationMetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#accessing-raw-response-data-eg-headers
        """
        return ConversationMetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConversationMetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#with_streaming_response
        """
        return ConversationMetaResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        created_at: str,
        name: str,
        scene: str,
        scene_desc: Dict[str, object],
        default_timezone: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_details: Optional[Dict[str, conversation_meta_create_params.UserDetails]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMetaCreateResponse:
        """
        Save conversation metadata information, including scene, participants, tags,
        etc.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/conversation-meta",
            body=maybe_transform(
                {
                    "created_at": created_at,
                    "name": name,
                    "scene": scene,
                    "scene_desc": scene_desc,
                    "default_timezone": default_timezone,
                    "group_id": group_id,
                    "tags": tags,
                    "user_details": user_details,
                },
                conversation_meta_create_params.ConversationMetaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMetaCreateResponse,
        )

    def update(
        self,
        *,
        default_timezone: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        scene_desc: Optional[Dict[str, object]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_details: Optional[Dict[str, conversation_meta_update_params.UserDetails]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMetaUpdateResponse:
        """
        Partially update conversation metadata, only updating provided fields

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/api/v1/memories/conversation-meta",
            body=maybe_transform(
                {
                    "default_timezone": default_timezone,
                    "group_id": group_id,
                    "name": name,
                    "scene_desc": scene_desc,
                    "tags": tags,
                    "user_details": user_details,
                },
                conversation_meta_update_params.ConversationMetaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMetaUpdateResponse,
        )

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMetaGetResponse:
        """Retrieve conversation metadata by group_id with fallback to default config"""
        return self._get(
            "/api/v1/memories/conversation-meta",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMetaGetResponse,
        )


class AsyncConversationMetaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConversationMetaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConversationMetaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConversationMetaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#with_streaming_response
        """
        return AsyncConversationMetaResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        created_at: str,
        name: str,
        scene: str,
        scene_desc: Dict[str, object],
        default_timezone: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_details: Optional[Dict[str, conversation_meta_create_params.UserDetails]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMetaCreateResponse:
        """
        Save conversation metadata information, including scene, participants, tags,
        etc.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/conversation-meta",
            body=await async_maybe_transform(
                {
                    "created_at": created_at,
                    "name": name,
                    "scene": scene,
                    "scene_desc": scene_desc,
                    "default_timezone": default_timezone,
                    "group_id": group_id,
                    "tags": tags,
                    "user_details": user_details,
                },
                conversation_meta_create_params.ConversationMetaCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMetaCreateResponse,
        )

    async def update(
        self,
        *,
        default_timezone: Optional[str] | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        scene_desc: Optional[Dict[str, object]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        user_details: Optional[Dict[str, conversation_meta_update_params.UserDetails]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMetaUpdateResponse:
        """
        Partially update conversation metadata, only updating provided fields

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/api/v1/memories/conversation-meta",
            body=await async_maybe_transform(
                {
                    "default_timezone": default_timezone,
                    "group_id": group_id,
                    "name": name,
                    "scene_desc": scene_desc,
                    "tags": tags,
                    "user_details": user_details,
                },
                conversation_meta_update_params.ConversationMetaUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMetaUpdateResponse,
        )

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConversationMetaGetResponse:
        """Retrieve conversation metadata by group_id with fallback to default config"""
        return await self._get(
            "/api/v1/memories/conversation-meta",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConversationMetaGetResponse,
        )


class ConversationMetaResourceWithRawResponse:
    def __init__(self, conversation_meta: ConversationMetaResource) -> None:
        self._conversation_meta = conversation_meta

        self.create = to_raw_response_wrapper(
            conversation_meta.create,
        )
        self.update = to_raw_response_wrapper(
            conversation_meta.update,
        )
        self.get = to_raw_response_wrapper(
            conversation_meta.get,
        )


class AsyncConversationMetaResourceWithRawResponse:
    def __init__(self, conversation_meta: AsyncConversationMetaResource) -> None:
        self._conversation_meta = conversation_meta

        self.create = async_to_raw_response_wrapper(
            conversation_meta.create,
        )
        self.update = async_to_raw_response_wrapper(
            conversation_meta.update,
        )
        self.get = async_to_raw_response_wrapper(
            conversation_meta.get,
        )


class ConversationMetaResourceWithStreamingResponse:
    def __init__(self, conversation_meta: ConversationMetaResource) -> None:
        self._conversation_meta = conversation_meta

        self.create = to_streamed_response_wrapper(
            conversation_meta.create,
        )
        self.update = to_streamed_response_wrapper(
            conversation_meta.update,
        )
        self.get = to_streamed_response_wrapper(
            conversation_meta.get,
        )


class AsyncConversationMetaResourceWithStreamingResponse:
    def __init__(self, conversation_meta: AsyncConversationMetaResource) -> None:
        self._conversation_meta = conversation_meta

        self.create = async_to_streamed_response_wrapper(
            conversation_meta.create,
        )
        self.update = async_to_streamed_response_wrapper(
            conversation_meta.update,
        )
        self.get = async_to_streamed_response_wrapper(
            conversation_meta.get,
        )
