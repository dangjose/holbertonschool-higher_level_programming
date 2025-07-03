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

users = {}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return False


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    if auth.current_user():
        return f"Basic Auth: Access Granted for {auth.current_user()}"
    return {"error": "Invalid credentials"}, 401


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username in users:
        if check_password_hash(users[username]["password"], password):
            identity = {
                "username": username,
                "role": users["role"]
            }
            access_token = create_access_token(identity=identity)
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
    if current_user.get("role") == "admin":
        return jsonify(message="Admin Access: Granted"), 200
    return {"error": "Admin access required"}, 403


if __name__ == "__main__":
    app.run()
