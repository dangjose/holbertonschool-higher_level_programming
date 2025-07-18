#!/usr/bin/python3
"""Task 5. API Security and Authentication Techniques"""

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required


app = Flask(__name__)

auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "DntJH@k@xWDga!dKU!TcJu*w7c.YVbxv"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return False


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return f"Basic Auth: Access Granted for {auth.current_user()}"


@app.route("/login", methods=["POST"])
def login():

    if not request.is_json:
        return {"error": "Missing JSON in request"}, 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if not username or not password:
        return {"error": "Username and password are required"}, 400

    if username in users:
        if check_password_hash(users[username]["password"], password):
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200
    return {"error": "Invalid credentials"}, 401


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted"), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if isinstance(current_user, str):
        user = users.get(current_user)
        if user and user.get("role") == "admin":
            return jsonify(message="Admin Access: Granted"), 200
        return {"error": "Admin access required"}, 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
