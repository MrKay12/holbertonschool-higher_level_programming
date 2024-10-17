#!/bin/python3
from flask import Flask, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"}
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None
    
@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")

app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    if username in users and check_password_hash(users[username]['password'], password):
        access_token = create_access_token(identity={"username": username, "role": users[username]["role"]})
        return jsonify(access_token=access_token), 200
    return jsonify({"error": "Invalid credentials"}), 401
    
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify(message="Admin Access: Granted")
    
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401
    
if __name__ == '__main__':
    app.run()
