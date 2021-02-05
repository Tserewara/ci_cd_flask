from src.flask_app import index


def test_index_returns_html():
    assert index() == "<h1>Hello World</h1>"
