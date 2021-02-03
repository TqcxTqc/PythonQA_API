import pytest
import requests


def test_module(base_url,base_status_code):
    response = requests.get(base_url)
    print(response.status_code)

    assert response.status_code == base_status_code