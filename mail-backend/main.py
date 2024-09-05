import mongodb_test_insert
from flask import Flask, request, jsonify
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def login():
    username = request.json.get('userEmail')
    password = request.json.get('userPassword')

    if username == "admin" and password == "password123": 
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Invalid credentials'})

if __name__ == "main":
    mongodb_test_insert.initilize()