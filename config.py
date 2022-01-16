"""
Common conf file containing variables to be used across the project
"""

import string
import random

BASE_URL = "https://jsonplaceholder.typicode.com"
TITLE = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
DEFAULT_BODY = {
        "title": TITLE,
        "body": 'bar',
        # "userId": 1,
}