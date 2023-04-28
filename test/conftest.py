import pytest
from setting.case_management import *
from setting.notif_slack import *
from setting.endpoint import CONN_NAME_KUCOIN
from websocket import create_connection


def pytest_html_report_title(report):
    report.title = "Report Websocket Automation"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring


@pytest.fixture(scope='function', autouse=True)
def hook(request):
    get_error = request.session.testsfailed

    yield

    test_result = request.session.testsfailed - get_error
    marker = request.node.get_closest_marker("TestManagement")

    if marker is None:
        print("there is test case id")
    else:
        if test_result == 0:
            case_management_push_result(str(marker.args[0]), "passed")
        else:
            case_management_push_result(str(marker.args[0]), "failed")


@pytest.fixture(scope='session', autouse=True)
def suite(request):
    # print("\nbefore suite")

    yield
    test_success = len(request.session.items) - request.session.testsfailed
    test_failed = request.session.testsfailed
    test_all = len(request.session.items)
    success_rate = test_success / test_all * 100

    if test_failed > 0:
        color = "FF1E00"
    else:
        color = "2B7A0B"
    webhook_slack(color, test_success, test_failed, test_all, success_rate)
    # print("after suite")


@pytest.fixture()
def open_connection_kucoin():
    token = requests.post("https://api.kucoin.com/api/v1/bullet-public").json().get("data")["token"]
    param = f"?token={token}"
    ws = create_connection(CONN_NAME_KUCOIN + param)
    return ws
