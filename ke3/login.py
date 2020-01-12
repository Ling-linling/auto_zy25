
def login(s, username="test", password="123456"):
    url = "http://49.235.92.12:9000/api/v1/login"
    body = {
        "username": username,
        "password": password
    }
    r = s.post(url, json=body)
    return r.json()["token"]