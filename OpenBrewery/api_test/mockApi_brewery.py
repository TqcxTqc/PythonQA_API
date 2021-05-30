from unittest.mock import Mock

REQUESTS = Mock()
REQUESTS.ok = True


def mock_get_list_breweries():
    return REQUESTS


def mock_get_list_by_city(by_city):
    REQUESTS.json.return_value = [{'city': by_city}]
    return REQUESTS


def mock_get_breweries_by_type(by_type):
    REQUESTS.json.return_value = [{'brewery_type': by_type}]
    return REQUESTS


def mock_get_single_brewery(brewery_id):
    REQUESTS.json.return_value = {'id': brewery_id}
    return REQUESTS


def mock_autocomplete_brewery(query):
    REQUESTS.json.return_value = [{'id': query}]
    return REQUESTS
