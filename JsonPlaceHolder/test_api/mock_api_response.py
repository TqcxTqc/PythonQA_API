from unittest.mock import Mock

RESPONSE = Mock()
RESPONSE.ok = True


def mock_username_by_id(userId, userName):
    RESPONSE.json.return_value = {'id': userId, 'name': userName}
    return RESPONSE


def mock_get_all_users():
    RESPONSE.json.return_value = [item for item in range(10)]
    return RESPONSE


def mock_get_all_comments():
    RESPONSE.json.return_value = [item for item in range(500)]
    return RESPONSE


def mock_get_comment_email():
    RESPONSE.json.return_value = [{'email': 'Presley.Mueller@myrl.com'}, {'email': 'Dallas@ole.me'},
                                  {'email': 'Mallory_Kunze@marie.org'}, {'email': 'Meghan_Littel@rene.us'},
                                  {'email': 'Carmen_Keeling@caroline.name'}
                                  ]
    return RESPONSE


def mock_api_todos():
    RESPONSE.json.return_value = [{'userId': 1, 'id': 1}, {'userId': 1, 'id': 2},
                                  {'userId': 1, 'id': 3}, {'userId': 1, 'id': 4},
                                  {'userId': 1, 'id': 5}, {'userId': 1, 'id': 6}]
    return RESPONSE
