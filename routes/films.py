from flask import Blueprint, request, jsonify
from bson import ObjectId
from datetime import datetime
from config import mongo
from models.film import Film

films_bp = Blueprint('films', __name__)

@films_bp.route('/films', methods=['GET'])
def get_films():
    films = list(mongo.db.films.find())
    for film in films:
        film['_id'] = str(film['_id'])
    return jsonify(films)

@films_bp.route('/films/<id>', methods=['GET'])
def get_film(id):
    film = mongo.db.films.find_one_or_404({'_id': ObjectId(id)})
    film['_id'] = str(film['_id'])
    return jsonify(film)

@films_bp.route('/films', methods=['POST'])
def create_film():
    data = request.get_json()
    film = Film(**data)
    result = mongo.db.films.insert_one(film.to_dict())
    film_dict = film.to_dict()
    film_dict['_id'] = str(result.inserted_id)
    return jsonify(film_dict), 201

@films_bp.route('/films/<id>', methods=['PUT'])
def update_film(id):
    data = request.get_json()
    data['updated_at'] = datetime.utcnow()
    mongo.db.films.update_one(
        {'_id': ObjectId(id)},
        {'$set': data}
    )
    film = mongo.db.films.find_one_or_404({'_id': ObjectId(id)})
    film['_id'] = str(film['_id'])
    return jsonify(film)

@films_bp.route('/films/<id>', methods=['DELETE'])
def delete_film(id):
    result = mongo.db.films.delete_one({'_id': ObjectId(id)})
    if result.deleted_count:
        return '', 204
    return '', 404