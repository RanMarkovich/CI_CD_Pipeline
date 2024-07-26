from requests import get


def test_demo_app():
    r = get('http://localhost:5000/')
    assert r.status_code == 200, r.text
    assert r.text == 'Hello World!'
