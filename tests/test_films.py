import pytest
from bson import ObjectId
from datetime import datetime
from app import app
import mongomock

@pytest.fixture
def client():
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/test'
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_film(client):
    film_data = {
        "title": "A New Hope",
        "release_date": "1977-05-25",
        "director": "George Lucas"
    }
    response = client.post('/films', json=film_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == film_data['title']
    assert '_id' in data

def test_get_films(client):
    response = client.get('/films')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)