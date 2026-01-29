# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.v1 import memory_load_params, memory_create_params, memory_delete_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from .conversation_meta import (
    ConversationMetaResource,
    AsyncConversationMetaResource,
    ConversationMetaResourceWithRawResponse,
    AsyncConversationMetaResourceWithRawResponse,
    ConversationMetaResourceWithStreamingResponse,
    AsyncConversationMetaResourceWithStreamingResponse,
)
from ....types.v1.memory_get_response import MemoryGetResponse
from ....types.v1.memory_load_response import MemoryLoadResponse
from ....types.v1.memory_create_response import MemoryCreateResponse
from ....types.v1.memory_delete_response import MemoryDeleteResponse
from ....types.v1.memory_search_response import MemorySearchResponse

__all__ = ["MemoriesResource", "AsyncMemoriesResource"]


class MemoriesResource(SyncAPIResource):
    @cached_property
    def conversation_meta(self) -> ConversationMetaResource:
        return ConversationMetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> MemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#accessing-raw-response-data-eg-headers
        """
        return MemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#with_streaming_response
        """
        return MemoriesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        content: str,
        create_time: str,
        message_id: str,
        sender: str,
        flush: bool | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        group_name: Optional[str] | Omit = omit,
        refer_list: Optional[SequenceNotStr[str]] | Omit = omit,
        role: Optional[str] | Omit = omit,
        sender_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateResponse:
        """
        Store a single message into memory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories",
            body=maybe_transform(
                {
                    "content": content,
                    "create_time": create_time,
                    "message_id": message_id,
                    "sender": sender,
                    "flush": flush,
                    "group_id": group_id,
                    "group_name": group_name,
                    "refer_list": refer_list,
                    "role": role,
                    "sender_name": sender_name,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryCreateResponse,
        )

    def delete(
        self,
        *,
        group_id: Optional[str] | Omit = omit,
        memory_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete memory records based on combined filter criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/api/v1/memories",
            body=maybe_transform(
                {
                    "group_id": group_id,
                    "memory_id": memory_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryDeleteResponse,
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
    ) -> MemoryGetResponse:
        """Retrieve memory records by memory_type with optional filters"""
        return self._get(
            "/api/v1/memories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryGetResponse,
        )

    def load(
        self,
        *,
        conversation_meta: memory_load_params.ConversationMeta,
        conversation_list: Optional[Iterable[memory_load_params.ConversationList]] | Omit = omit,
        version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryLoadResponse:
        """Import conversation metadata and message list in one request.

        Messages are
        queued for processing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/memories/import",
            body=maybe_transform(
                {
                    "conversation_meta": conversation_meta,
                    "conversation_list": conversation_list,
                    "version": version,
                },
                memory_load_params.MemoryLoadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLoadResponse,
        )

    def search(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Retrieve relevant memory data based on query text using multiple retrieval
        methods
        """
        return self._get(
            "/api/v1/memories/search",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchResponse,
        )


class AsyncMemoriesResource(AsyncAPIResource):
    @cached_property
    def conversation_meta(self) -> AsyncConversationMetaResource:
        return AsyncConversationMetaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMemoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMemoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMemoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/EverMemOS-python#with_streaming_response
        """
        return AsyncMemoriesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        content: str,
        create_time: str,
        message_id: str,
        sender: str,
        flush: bool | Omit = omit,
        group_id: Optional[str] | Omit = omit,
        group_name: Optional[str] | Omit = omit,
        refer_list: Optional[SequenceNotStr[str]] | Omit = omit,
        role: Optional[str] | Omit = omit,
        sender_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryCreateResponse:
        """
        Store a single message into memory.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories",
            body=await async_maybe_transform(
                {
                    "content": content,
                    "create_time": create_time,
                    "message_id": message_id,
                    "sender": sender,
                    "flush": flush,
                    "group_id": group_id,
                    "group_name": group_name,
                    "refer_list": refer_list,
                    "role": role,
                    "sender_name": sender_name,
                },
                memory_create_params.MemoryCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryCreateResponse,
        )

    async def delete(
        self,
        *,
        group_id: Optional[str] | Omit = omit,
        memory_id: Optional[str] | Omit = omit,
        user_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryDeleteResponse:
        """
        Delete memory records based on combined filter criteria

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/api/v1/memories",
            body=await async_maybe_transform(
                {
                    "group_id": group_id,
                    "memory_id": memory_id,
                    "user_id": user_id,
                },
                memory_delete_params.MemoryDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryDeleteResponse,
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
    ) -> MemoryGetResponse:
        """Retrieve memory records by memory_type with optional filters"""
        return await self._get(
            "/api/v1/memories",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryGetResponse,
        )

    async def load(
        self,
        *,
        conversation_meta: memory_load_params.ConversationMeta,
        conversation_list: Optional[Iterable[memory_load_params.ConversationList]] | Omit = omit,
        version: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemoryLoadResponse:
        """Import conversation metadata and message list in one request.

        Messages are
        queued for processing.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/memories/import",
            body=await async_maybe_transform(
                {
                    "conversation_meta": conversation_meta,
                    "conversation_list": conversation_list,
                    "version": version,
                },
                memory_load_params.MemoryLoadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemoryLoadResponse,
        )

    async def search(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> MemorySearchResponse:
        """
        Retrieve relevant memory data based on query text using multiple retrieval
        methods
        """
        return await self._get(
            "/api/v1/memories/search",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MemorySearchResponse,
        )


class MemoriesResourceWithRawResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_raw_response_wrapper(
            memories.create,
        )
        self.delete = to_raw_response_wrapper(
            memories.delete,
        )
        self.get = to_raw_response_wrapper(
            memories.get,
        )
        self.load = to_raw_response_wrapper(
            memories.load,
        )
        self.search = to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> ConversationMetaResourceWithRawResponse:
        return ConversationMetaResourceWithRawResponse(self._memories.conversation_meta)


class AsyncMemoriesResourceWithRawResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_raw_response_wrapper(
            memories.create,
        )
        self.delete = async_to_raw_response_wrapper(
            memories.delete,
        )
        self.get = async_to_raw_response_wrapper(
            memories.get,
        )
        self.load = async_to_raw_response_wrapper(
            memories.load,
        )
        self.search = async_to_raw_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> AsyncConversationMetaResourceWithRawResponse:
        return AsyncConversationMetaResourceWithRawResponse(self._memories.conversation_meta)


class MemoriesResourceWithStreamingResponse:
    def __init__(self, memories: MemoriesResource) -> None:
        self._memories = memories

        self.create = to_streamed_response_wrapper(
            memories.create,
        )
        self.delete = to_streamed_response_wrapper(
            memories.delete,
        )
        self.get = to_streamed_response_wrapper(
            memories.get,
        )
        self.load = to_streamed_response_wrapper(
            memories.load,
        )
        self.search = to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> ConversationMetaResourceWithStreamingResponse:
        return ConversationMetaResourceWithStreamingResponse(self._memories.conversation_meta)


class AsyncMemoriesResourceWithStreamingResponse:
    def __init__(self, memories: AsyncMemoriesResource) -> None:
        self._memories = memories

        self.create = async_to_streamed_response_wrapper(
            memories.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            memories.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            memories.get,
        )
        self.load = async_to_streamed_response_wrapper(
            memories.load,
        )
        self.search = async_to_streamed_response_wrapper(
            memories.search,
        )

    @cached_property
    def conversation_meta(self) -> AsyncConversationMetaResourceWithStreamingResponse:
        return AsyncConversationMetaResourceWithStreamingResponse(self._memories.conversation_meta)
