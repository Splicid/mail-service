import mongodb_test_insert
from flask import Flask



app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


if __name__ == "main":
    mongodb_test_insert.initilize()