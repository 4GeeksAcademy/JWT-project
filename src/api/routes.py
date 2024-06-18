"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Manager
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from werkzeug.security import generate_password_hash

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200

@api.route('/User/login', methods=['GET'])
def user_login():
    response_body={
        "message": "This route is working, go ahead an create an user"
    }

    return jsonify(response_body), 200

@api.route('/user/signup', methods=['POST'])
def user_signup():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        

        if not email or not password or not phone_number:
            return jsonify({"Error": "email, password, phone number and is active are required"}), 400
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"msg": "This email is alredy registered"}), 409
        
        password_hash = generate_password_hash(password)

        new_user= User(
            email = email,
            password = password_hash,
            phone_number = phone_number
        )
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"Success": "user created successfully"}), 201
    
    except Exception as e:
        return jsonify({"msg": str(e)}), 500
