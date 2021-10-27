import json

import pytest

from web import app


@pytest.fixture
def api():
    test_api = app.app
    api = test_api.test_client()

    return api


def test_index(api):
    response = api.get("/")

    print(f"response data: {response.data}")
    assert response.data == b"Hello Justin!"


def test_user(api):
    new_user = {
        "email": "hsuk@thecommerce.co.kr",
        "name": "justin",
        "role": "A"
    }

    response = api.post(
        "/sign-up",
        data=json.dumps(new_user),
        content_type="application/json"
    )

    print(f"response: {response}")
    print(f"response status code: {response.status_code}")
    print(f"response data: {response.data}")
    assert response.status_code == 200
