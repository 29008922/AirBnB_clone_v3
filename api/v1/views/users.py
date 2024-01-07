#/usr/bin/python3
"""
Create a new view for User object that handles all default RESTFul API actions
"""

# Import necessary modules
from flask import abort, jsonify, request
# Import the User model
from models.user import User
from api.v1.views import app_views
from models import storage

def get_all():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

def get_one(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user.to_dict())

def delete(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    user.delete()
    return jsonify({}), 200

def create():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400

    
if
 
"email"
 
not
 
in data:
        return jsonify({"error": "Missing email"}), 400

    
if
 
"password"
 
not
 
in data:
        return jsonify({"error": "Missing password"}), 400
    user = User(**data)
    user.set_password(data["password"])  # Assuming a password hashing mechanism
    user.save()
    return jsonify(user.to_dict()), 201

def update(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Not a JSON"}), 400
    if "password" in data:
        user.set_password(data["password"])  # Update password if provided
    for key, value in data.items():
        if key not in ["id", "email", "created_at", "updated_at"]:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict()), 200
