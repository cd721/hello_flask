
# Run the following command in the top-level project directory
# python -m pytest

def test_home(app, client):
    res = client.get("/")
    assert res.status_code == 200


def test_valid_word(app,client):
    res = client.get("/deterministic")
    assert res.status_code == 200

def test_invalid_word_with_suggestions(app,client):
    res = client.get("/meak")
    assert res.status_code == 302

def test_invalid_word_with_no_suggestions(app,client):
    res = client.get("/908o7yit")
    assert res.status_code == 404

def test_word_is_whitespace(app,client):
    res = client.get("/  ")
    assert res.status_code == 400