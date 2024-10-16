#!/usr/bin/python3
""" put description here"""
from flask import Flask, jsonify, request, json


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """ put description here"""
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """ put description here"""
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """ put description here"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """ put description here"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """ put description here"""
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400
    else:
        users[username] = data
        return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    """ put description here"""
    app.run(debug=True)
