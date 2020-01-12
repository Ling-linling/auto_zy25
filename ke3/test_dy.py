import requests
import pytest
from ke3.login import login

@pytest.fixture(scope="session")
def login_fixture():
    username = "test"
    password = "123456"
    s = requests.session()
    token = login(s, username, password)
    s.headers.update({"Authorization": "Token %s" % token})
    return s

def test_user_info(login_fixture):
    s = login_fixture
    url2 = "http://49.235.92.12:9000/api/v1/userinfo"
    r2 = s.get(url2)
    assert r2.json()["msg"] == "sucess!"
    assert r2.json()["code"] == 0


