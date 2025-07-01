#!/usr/bin/python3
"""Task 4. Develop a Simple API using Python with Flask"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def show_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return {"error": "User not found"}, 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    username = data.get("username")

    if not username:
        return ({"error": "Username is required"}), 400

    users[username] = data

    return ({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
