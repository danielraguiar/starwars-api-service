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

def test_create_planet(client):
    planet_data = {
        "name": "Tatooine",
        "climate": "Arid",
        "diameter": "10465",
        "population": "120000"
    }
    response = client.post('/planets', json=planet_data)
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == planet_data['name']
    assert '_id' in data

def test_get_planets(client):
    response = client.get('/planets')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)