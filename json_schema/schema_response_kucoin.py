get_msg_subscribe_market_normal = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "type": {
            "type": "string"
        },
        "topic": {
            "type": "string"
        },
        "subject": {
            "type": "string"
        },
        "data": {
            "type": "object",
            "properties": {
                "bestAsk": {
                    "type": "string"
                },
                "bestAskSize": {
                    "type": "string"
                },
                "bestBid": {
                    "type": "string"
                },
                "bestBidSize": {
                    "type": "string"
                },
                "price": {
                    "type": "string"
                },
                "sequence": {
                    "type": "string"
                },
                "size": {
                    "type": "string"
                },
                "time": {
                    "type": "integer"
                }
            },
            "required": [
                "bestAsk",
                "bestAskSize",
                "bestBid",
                "bestBidSize",
                "price",
                "sequence",
                "size",
                "time"
            ]
        }
    },
    "required": [
        "type",
        "topic",
        "subject",
        "data"
    ]
}
