"""
File for pytest fixtures for proper setup and teardown functions
"""

import pytest
import requests
import random


# Creating common session to be reused further
@pytest.fixture
def session():
    s = requests.Session()
    yield s
    s.close()


# Finding random user IDs and email
@pytest.fixture
def user(session):
    users = session.get('https://jsonplaceholder.typicode.com/users')
    random_user = random.choice(users.json())
    random_user_id, email = random_user['id'], random_user['email']
    print(email)
    return random_user_id

