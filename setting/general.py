import os

# GENERAL
max_latency = 1000000

# TEST CASE MANAGEMENT
api_key = os.environ.get('API_KEY_QASE')
host_test_management = "https://api.qase.io/v1/result"
test_run = 9
test_code_project = "TF"

# SLACK NOTIFICATION
slack_webhook = os.environ.get('CLIENT_SLACK')
slack_title = os.environ.get('TEST')
url_artifact = os.environ.get('RUNID')
notif_slack = "ON"
notif_slack_just_failed = "NO"
