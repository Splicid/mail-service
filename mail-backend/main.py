import os
from flask import Flask
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def database():
    uri = f"mongodb+srv://luis1abreu11:{os.getenv("DB-PASSWORD")}@cluster0.f4werh5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

    client = MongoClient(uri)