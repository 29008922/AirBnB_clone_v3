#!/usr/bin/python3

"""
Create a new view for Place objects that handles all default RESTFul API actions
"""

#import all the necesary modules
from flask import abort, jsonify, request
# Import the required models
from models.city import City
from models.place import Place

def get_all_by_city(city_id):
    city = City.query.get(city_id)
    if city is None:
        return jsonify({"error": "City not found"}), 404
    places = Place.query.filter_by(city_id=city_id).all()
    return jsonify([place.to_dict() for place in places])

def get_one(place_id):
    place = Place.query.get(place_id)
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    return jsonify(place.to_dict())

def delete(place_id):
    place = Place.query.get(place_id)
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    place.delete()
    return jsonify({}), 200

def create(city_id):
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "user_id" not in data:
        return jsonify({"error": "Missing user_id"}), 400
    user = User.query.get(data["user_id"])
    if user is None:
        return jsonify({"error": "User not found"}), 404
    if "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    city = City.query.get(city_id)
    if city is None:
        return jsonify({"error": "City not found"}), 404
    place = Place(user_id=data["user_id"], city_id=city_id, **data)
    place.save()
    return jsonify(place.to_dict()), 201

def update(place_id):
    place = Place.query.get(place_id)
    if place is None:
        return jsonify({"error": "Place not found"}), 404
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    for key, value in data.items():
        if key not in ["id", "user_id", "city_id", "created_at", "updated_at"]:
            setattr(place, key, value)
    place.save()
    return jsonify(place.to_dict()), 200
