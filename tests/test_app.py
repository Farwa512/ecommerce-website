import os

os.environ["DATABASE_URL"] = "sqlite:///:memory:"
os.environ["SECRET_KEY"] = "test-secret-key"

import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home_page_loads(client):
    response = client.get("/")
    assert response.status_code == 200


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200


def test_register_page_loads(client):
    response = client.get("/register")
    assert response.status_code == 200


def test_search_with_no_match(client):
    response = client.get("/?q=zzzzzz")
    assert b"No products found" in response.data


def test_cart_requires_login(client):
    response = client.get("/cart")
    assert response.status_code in (301, 302, 401)


def test_home_page_shows_delivery_message(client):
    response = client.get("/")
    assert b"Free delivery" in response.data
