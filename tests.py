from tick_tick import TickAPI
import pytest


@pytest.fixture()
def authenticated_session():
    api = TickAPI('gipofe2520@asfalio.com', '123456789')
    return api


@pytest.fixture()
def wrong_login_info():
    return ['TestLogin', 'TestPassword']


@pytest.fixture()
def successful_login_info():
    return ['gipofe2520@asfalio.com', '123456789']


def test_fail_tick_authorization(wrong_login_info):
    with pytest.raises(AttributeError):
        TickAPI(wrong_login_info[0], wrong_login_info[1])


def test_successful_tick_authorization(successful_login_info):
    TickAPI(successful_login_info[0], successful_login_info[1])
