from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(host="localhost", port=27017)
client = MongoClient("mongodb://localhost:27017")
db = client["rptutorials"]
@app.route("/")
def index():
    return "<p>Hello, World!</p>"

