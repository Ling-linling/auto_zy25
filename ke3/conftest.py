import pytest
import requests

from ke3.login import login


@pytest.fixture(scope="session")
def login_fixture():
    username = "test"
    password = "123456"
    s = requests.session()
    token = login(s, username, password)
    s.headers.update({"Authorization": "Token %s" % token})
    return s