import json
import pytest
from assertpy import assert_that
from jsonschema import validate as validate_json_schema
from json_schema.schema_response_kucoin import *


@pytest.mark.TestManagement(9)
def test_get_price_kucoin(open_connection_kucoin):
    msg = {
        "id": 1545910660739,
        "type": "subscribe",
        "topic": "/market/ticker:BTC-USDT",
        "privateChannel": False,
        "response": True
    }
    open_connection_kucoin.send(json.dumps(msg))

    resp_msg_1 = json.loads(open_connection_kucoin.recv())
    assert_that(resp_msg_1.get("type")).is_equal_to("welcome")

    resp_msg_2 = json.loads(open_connection_kucoin.recv())
    assert_that(resp_msg_2.get("type")).is_equal_to("ack")

    resp_msg_3 = json.loads(open_connection_kucoin.recv())
    assert_that(resp_msg_3.get("type")).is_equal_to("message")
    assert_that(resp_msg_3.get("topic")).is_equal_to("/market/ticker:BTC-USDT")
    validate_json_schema(instance=resp_msg_3, schema=get_msg_subscribe_market_normal)


@pytest.mark.TestManagement(10)
def test_get_price_kucoin_all(open_connection_kucoin):
    msg = {
        "id": 1545910660739,
        "type": "subscribe",
        "topic": "/market/ticker:all",
        "privateChannel": False,
        "response": True
    }
    open_connection_kucoin.send(json.dumps(msg))

    resp_msg_1 = json.loads(open_connection_kucoin.recv())
    assert_that(resp_msg_1.get("type")).is_equal_to("welcome")

    resp_msg_2 = json.loads(open_connection_kucoin.recv())
    assert_that(resp_msg_2.get("type")).is_equal_to("ack")

    resp_msg_3 = json.loads(open_connection_kucoin.recv())
    assert_that(resp_msg_3.get("type")).is_equal_to("message")
    assert_that(resp_msg_3.get("topic")).is_equal_to("/market/ticker:all")
    validate_json_schema(instance=resp_msg_3, schema=get_msg_subscribe_market_normal)
