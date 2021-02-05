import requests


def test_module(base_url, base_status_code):
    response = requests.get(base_url)

    assert response.status_code == base_status_code
