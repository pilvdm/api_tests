import pytest
from config import BASE_URL, TITLE, DEFAULT_BODY


"""
Test data set with valid bodies
Arguments are (body, expected_status_code, expected_title, expected_body)
"""
test_data_bodies = [
        ({**DEFAULT_BODY}, 201, TITLE, "foo"),
        ({**DEFAULT_BODY}, 201, TITLE, "body with dot ."),
        ({**DEFAULT_BODY, "userId": 11}, 201, 123, 445),
        ({**DEFAULT_BODY}, 201, "", ""),
        ({**DEFAULT_BODY}, 201, "title with dot .", "1")
    ]


# This test will check if post IDs of the user are in range of 0 to 100
def test_post_ids_range(session, user):
    user_posts = session.get(f'{BASE_URL}/posts?userId={user}')
    for i in user_posts.json():
        assert (0 <= int(i['id']) <= 100, "post ID should valid (between 0 and 100)")


# Test to verify posting functionality for the random user
@pytest.mark.parametrize('body, expected_status_code, expected_title, expected_body', test_data_bodies)
def test_user_can_post(session, user, body, expected_status_code, expected_title, expected_body):

    body = {
        **body,
        # If user ID is specified in the body - it will be used, otherwise it will use user_id from get_users fixture
        "userId": (body['userId'] if 'userId' in body else user),
        "title": expected_title,
        "body": expected_body
    }

    post_response = session.post(f'{BASE_URL}/posts', data=body)

    response_json = post_response.json()
    resp_status_code = post_response.status_code
    response_title = response_json['title']
    response_body = response_json['body']
    response_user_id = response_json['userId']
    response_body_len = len(response_json)

    print(response_json)

    assert (resp_status_code == expected_status_code,
            f"status code should be {expected_status_code}, not {resp_status_code}")
    assert (response_user_id == user,
            f"title should be {response_user_id}, not {user}")
    assert (response_title == expected_title,
            f"title should be {expected_title}, not {response_title}")
    assert (response_body == expected_body,
            f"title should be {expected_body}, not {response_body}")
    assert (len(post_response.json()) == 4,
            f"response body length should be {4}, not {response_body_len}")
