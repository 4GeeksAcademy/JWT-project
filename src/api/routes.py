"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Manager
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, decode_token
from sqlalchemy.exc import SQLAlchemyError
import sqlalchemy 

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)

# --------------User-----------------------------------
@api.route('/user/signup', methods=['POST'])
def user_signup():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')
        

        if not email or not password or not phone_number:
            return jsonify({"Error": "email, password, phone number are required"}), 400
        
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

@api.route('/user/login', methods=['POST'])
def user_login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({"msg": "email and password are requiered"})

        user_login = User.query.filter_by(email=email).first()
        if not user_login:
            return jsonify({"msg": "invalid email"}), 400
        
        password_from_db = user_login.password  # se obtiene la contraseña desde la base de datos

        user_access = check_password_hash(password_from_db, password)  # se verifica la contraseña

        if user_access: 
            expires = timedelta(hours=3)
            user_id = user_login.id
            access_token = create_access_token(identity=user_id, expires_delta=expires)
            return jsonify({"access_token": access_token, "message": "login successfully"}), 200
        else:
            return jsonify({"Error": "Invalid password"}), 400

    except sqlalchemy.exc.SQLAlchemyError as e:
        # Manejar errores de la base de datos de manera específica
        return jsonify({"Error": "Database error", "message": str(e)}), 500 
    except Exception as e:
        return jsonify({"Error", str(e)})
        
# ---------------------- Manager ----------------------
@api.route('/manager/signup', methods=['POST'])
def manager_signup():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        phone_number = request.json.get('phone_number')

        if not email or not password or not phone_number:
            return jsonify({"Error": "email, password and phone number are required"}), 400
        
        existing_manager = Manager.query.filter_by(email=email).first()
        
        if existing_manager:
            return jsonify({"msg": "this email is already registered"}), 409
        
        password_hash = generate_password_hash(password)
        new_manager = Manager(
            email=email,
            password=password_hash,
            phone_number=phone_number
        )
        db.session.add(new_manager)
        db.session.commit()
        return jsonify({"success": "Manager has been created successfully"})
    except Exception as e:
        return jsonify({"Error": "Problems creating manager profile " + str(e)}), 500

@api.route('/manager/login', methods=['POST'])
def manager_login():
    try:
        email = request.json.get('email')
        password = request.json.get('password')

        if not email or not password:
            return jsonify({"error": "email and password are requiered"}), 400
        
        manager_profile = Manager.query.filter_by(email=email).first()
        if not manager_profile:
            return jsonify({"Error": "Invalid email"}), 400
        
        password_from_db = manager_profile.password

        manager_access = check_password_hash(password_from_db, password)

        if manager_access:
            expires = timedelta(hours=3)
            manager_id = manager_profile.id
            access_token = create_access_token(identity=manager_id, expires_delta=expires)
            return jsonify({"access to token": access_token, "message": "login successfully"}), 200
        else:
            return jsonify({"Error": "incorrect password"}),400
        
    except sqlalchemy.exc.SQLAlchemyError as e:
        return jsonify({"Error": "Database error", "message": str(e)}),500
    except Exception as e:
        return jsonify({"Error": str(e)}),500