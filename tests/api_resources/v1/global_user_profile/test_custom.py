# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from evermemos import EverMemOS, AsyncEverMemOS
from tests.utils import assert_matches_type
from evermemos.types.v1.global_user_profile import CustomUpsertResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustom:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upsert(self, client: EverMemOS) -> None:
        custom = client.v1.global_user_profile.custom.upsert(
            custom_profile_data={
                "initial_profile": [
                    "User is a software engineer",
                    "User is proficient in Python programming",
                    "User is interested in AI technology",
                ]
            },
            user_id="user_id",
        )
        assert_matches_type(CustomUpsertResponse, custom, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upsert(self, client: EverMemOS) -> None:
        response = client.v1.global_user_profile.custom.with_raw_response.upsert(
            custom_profile_data={
                "initial_profile": [
                    "User is a software engineer",
                    "User is proficient in Python programming",
                    "User is interested in AI technology",
                ]
            },
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = response.parse()
        assert_matches_type(CustomUpsertResponse, custom, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upsert(self, client: EverMemOS) -> None:
        with client.v1.global_user_profile.custom.with_streaming_response.upsert(
            custom_profile_data={
                "initial_profile": [
                    "User is a software engineer",
                    "User is proficient in Python programming",
                    "User is interested in AI technology",
                ]
            },
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = response.parse()
            assert_matches_type(CustomUpsertResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCustom:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upsert(self, async_client: AsyncEverMemOS) -> None:
        custom = await async_client.v1.global_user_profile.custom.upsert(
            custom_profile_data={
                "initial_profile": [
                    "User is a software engineer",
                    "User is proficient in Python programming",
                    "User is interested in AI technology",
                ]
            },
            user_id="user_id",
        )
        assert_matches_type(CustomUpsertResponse, custom, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upsert(self, async_client: AsyncEverMemOS) -> None:
        response = await async_client.v1.global_user_profile.custom.with_raw_response.upsert(
            custom_profile_data={
                "initial_profile": [
                    "User is a software engineer",
                    "User is proficient in Python programming",
                    "User is interested in AI technology",
                ]
            },
            user_id="user_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom = await response.parse()
        assert_matches_type(CustomUpsertResponse, custom, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upsert(self, async_client: AsyncEverMemOS) -> None:
        async with async_client.v1.global_user_profile.custom.with_streaming_response.upsert(
            custom_profile_data={
                "initial_profile": [
                    "User is a software engineer",
                    "User is proficient in Python programming",
                    "User is interested in AI technology",
                ]
            },
            user_id="user_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom = await response.parse()
            assert_matches_type(CustomUpsertResponse, custom, path=["response"])

        assert cast(Any, response.is_closed) is True
