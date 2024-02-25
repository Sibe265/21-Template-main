import os
import pytest

os.environ['DATABASE_URL'] = "sqlite:///:memory:"

from main import app, db

@pytest.fixture
def client():
    with app.app_context():
        client = app.test_client
        cleanup()
        db.create_all()
        yield client

def cleanup():
    with app.app_context():
        db.drop_all()

def test_index_not_logged_in(client):
    response = client.get("/")
    assert b'Enter your name' in response.data