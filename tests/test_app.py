
# Run the following command in the top-level project directory
# python -m pytest

import logging

LOGGER = logging.getLogger(__name__)

def test_home(app, client):
    res = client.get("/")
    LOGGER.info(res)
    assert res.status_code == 200


def test_valid_word(app,client):
    res = client.get("/deterministic")
    LOGGER.info(res)
    assert res.status_code == 200

def test_invalid_word_with_suggestions(app,client):
    res = client.get("/meak")
    LOGGER.info(res)
    assert res.status_code == 302

def test_invalid_word_with_no_suggestions(app,client):
    res = client.get("/908o7yit")
    LOGGER.info(res)
    assert res.status_code == 404

def test_word_is_whitespace(app,client):
    res = client.get("/  ")
    LOGGER.info(res)
    assert res.status_code == 400