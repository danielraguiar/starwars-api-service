from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime
from config import mongo
from models.planet import Planet

planets_bp = Blueprint('planets', __name__)

@planets_bp.route('/planets', methods=['GET'])
def get_planets():
    planets = list(mongo.db.planets.find())
    for planet in planets:
        planet['_id'] = str(planet['_id'])
    return jsonify(planets)

@planets_bp.route('/planets/<id>', methods=['GET'])
def get_planet(id):
    planet = mongo.db.planets.find_one_or_404({'_id': ObjectId(id)})
    planet['_id'] = str(planet['_id'])
    return jsonify(planet)

@planets_bp.route('/planets', methods=['POST'])
def create_planet():
    data = request.get_json()
    planet = Planet(**data)
    result = mongo.db.planets.insert_one(planet.to_dict())
    planet_dict = planet.to_dict()
    planet_dict['_id'] = str(result.inserted_id)
    return jsonify(planet_dict), 201

@planets_bp.route('/planets/<id>', methods=['PUT'])
def update_planet(id):
    data = request.get_json()
    data['updated_at'] = datetime.utcnow()
    mongo.db.planets.update_one(
        {'_id': ObjectId(id)},
        {'$set': data}
    )
    planet = mongo.db.planets.find_one_or_404({'_id': ObjectId(id)})
    planet['_id'] = str(planet['_id'])
    return jsonify(planet)

@planets_bp.route('/planets/<id>', methods=['DELETE'])
def delete_planet(id):
    result = mongo.db.planets.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return '', 204
    return '', 404