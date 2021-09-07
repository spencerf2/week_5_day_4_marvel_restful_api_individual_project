from flask import Blueprint, request, jsonify
from marvel_collection.helpers import token_required
from marvel_collection.models import db, User, Marvel, marvel_schema, marvels_schema

api = Blueprint('api', __name__, url_prefix = '/api')

# CRUD = Create Retrieve Update Delete

# CREATE MARVEL ENDPOINT
@api.route('/marvels', methods = ['POST'])
@token_required
def create_marvel(current_user_token):
    name = request.json['name']
    description = request.json['description']
    height = request.json['height']
    super_power = request.json['super_power']
    flight_time = request.json['flight_time']
    max_speed = request.json['max_speed']
    comics_appeared_in = request.json['comics_appeared_in']
    weight = request.json['weight']
    series = request.json['series']
    user_token = current_user_token.token

    print(f'BIG TESTER: {current_user_token.token}')

    marvel = Marvel(name, description, height, super_power, flight_time, max_speed, comics_appeared_in, weight, series, user_token = user_token)

    db.session.add(marvel)
    db.session.commit()

    response = marvel_schema.dump(marvel)
    return jsonify(response)

# RETRIEVE ALL MARVELs ENDPOINT
@api.route('/marvels', methods = ['GET'])
@token_required
def get_marvels(current_user_token):
    owner = current_user_token.token
    marvels = Marvel.query.filter_by(user_token = owner).all()
    response = marvels_schema.dump(marvels)
    return jsonify(response)

# RETRIEVE ONE MARVEL ENDPOINT
@api.route('/marvels/<id>', methods = ['GET'])
@token_required
def get_marvel(current_user_token, id):
    owner = current_user_token.token
    if owner == current_user_token.token:
        marvel = Marvel.query.get(id)
        response = marvel_schema.dump(marvel)
        return jsonify(response)
    else:
        return jsonify({"message" : "Valid Token Required"}), 401

# UPDATE MARVEL ENDPOINT
@api.route('/marvels/<id>', methods = ['POST','PUT'])
@token_required
def update_marvel(current_user_token, id):
    marvel = Marvel.query.get(id) # GET MARVEL INSTANCE

    marvel.name = request.json['name']
    marvel.description = request.json['description']
    marvel.height = request.json['height']
    marvel.super_power = request.json['super_power']
    marvel.flight_time = request.json['flight_time']
    marvel.max_speed = request.json['max_speed']
    marvel.comics_appeared_in = request.json['comics_appeared_in']
    marvel.weight = request.json['weight']
    marvel.series = request.json['series']
    marvel.user_token = current_user_token.token

    db.session.commit()
    response = marvel_schema.dump(marvel)
    return jsonify(response)

# DELETE MARVEL ENDPOINT
@api.route('/marvels/<id>', methods = ['DELETE'])
@token_required
def delete_marvel(current_user_token, id):
    marvel = Marvel.query.get(id)
    db.session.delete(marvel)
    db.session.commit()
    response = marvel_schema.dump(marvel)
    return jsonify(response)