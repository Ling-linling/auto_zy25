
def test_changeinfo(login_fixture):
    s = login_fixture
    url = "http://49.235.92.12:9000/api/v1/userinfo"
    body = {
        "name": "test",
        "sex": "M",
        "age": 20,
        "mail": "283340479@qq.com"
}
    r = s.post(url, json=body)
    print(r.text)

