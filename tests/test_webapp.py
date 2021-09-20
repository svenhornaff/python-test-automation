import pytest
import webapp


@pytest.fixture(scope="session")
def app():
    app = webapp.create_app()
    app.debug = True
    return app.test_client()


def test_hello_world(app):
    res = app.get("/")
    # print(dir(res), res.status_code)
    assert res.status_code == 200
    assert b"Hello World" in res.data


def test_some_id(app):
    res = app.get("/foo/12345")
    assert res.status_code == 200
    assert b"12345" in res.data


@pytest.mark.xfail
def test_divide_by_zero():
    assert 1 / 0 == 1


@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...