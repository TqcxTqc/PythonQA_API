import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="Request URL"
    )

    parser.addoption(
        "--status_code",
        default=200,
        choices=[200, 201, 302, 400, 404],
        type=int,
        help="Status codes"
    )


@pytest.fixture()
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def base_status_code(request):
    return request.config.getoption("--status_code")
