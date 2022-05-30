import pytest


@pytest.fixture()
def some_data():
    return 0


@pytest.fixture()
def user():
    return {
        "id": 1,
        "username": "l.l.vinni",
        "email": "turupuru8@gmail.com",
    }
