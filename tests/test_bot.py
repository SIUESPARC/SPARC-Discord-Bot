import os

from bot.integrations import send_groupme


def test_send_groupme():
    GROUPME=os.getenv('TEST_GROUPME')
    assert send_groupme(GROUPME, "Hello") is None


