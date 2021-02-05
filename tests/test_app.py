from src.flask_app import index, page


def test_index_returns_html():
    assert index() == "<h1>Hello World</h1>"


def test_page_returns_html():
    assert page() == "<h1>Page is here</h1>"
