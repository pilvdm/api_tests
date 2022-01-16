from config import BASE_URL, TITLE, DEFAULT_BODY
import random
import string
import pytest
import aiohttp

# Test data set with invalid userIds for getting posts
test_data_invalid_user_ids = [
    random.randint(100000, 100000000),
    random.uniform(0.1, 0.9),
    TITLE,
    -1
]

# Test data set with invalid bodies for posting
test_data_bodies = [
        ({**DEFAULT_BODY, "userId": ''}, 201, 1),
        ({}, 201, 0),
        ({**DEFAULT_BODY, "userId": 1, "title": ''.join(random.choices(string.ascii_uppercase, k=10000))}, 201, 1),
        ({**DEFAULT_BODY, "userId": random.randint(10000, 100000)}, 201, 1),
        ({**DEFAULT_BODY, "userId": random.uniform(0.1, 0.9)}, 201, 1)
    ]


# This test will check if get_posts responses are valid against invalid user IDs
@pytest.mark.parametrize("user_id", test_data_invalid_user_ids)
@pytest.mark.asyncio
async def test_get_posts_for_invalid_ids(session, user_id):

    async with aiohttp.ClientSession() as session:
        response = await session.get(f'{BASE_URL}/posts?userId={user_id}')
        response_body = await response.json()
        # response_status_code = await response.status_code
        assert (response.status == 200, 'response status code should be successful')
        assert (len(response_body) == 0, 'no data should be present in the response')


# Test to verify posting functionality for the random user with invalid bodies
@pytest.mark.parametrize("body, expected_status_code, expected_body_len", test_data_bodies)
@pytest.mark.asyncio
async def test_invalid_body_post(session, user, body, expected_status_code, expected_body_len):

    body = {
        **body,
        # If user ID is specified in the body - it will be used, otherwise it will use user_id from get_users fixture
        "userId": (body['userId'] if 'userId' in body else user),
    }

    async with aiohttp.ClientSession() as session:
        post_response = await session.post(f'{BASE_URL}/posts', data=body)
        response_body = await post_response.json()
        print(response_body)
        assert (post_response.status != expected_status_code,
                f"Response should not be {expected_status_code} for body {body}")
        assert (len(response_body) <= expected_body_len,
                f"Response body should be less than {expected_body_len}")

