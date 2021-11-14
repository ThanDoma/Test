from flask import Flask, render_template
from flask_pymongo import PyMongo
import flask


app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb://devroot:devroot@localhost:27017/?authSource=admin&readPreference=primary&ssl=false"
app.config["MONGO_URI"] = "mongodb://devroot:devroot@localhost:27017/admin"
mongodb_client = PyMongo(app)
db = mongodb_client.db


# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/")
# def home_page():
#     online_users = mongo.db.users.find({"online": True})
#     return render_template(online_users=online_users)

@app.route("/add_one")
def add_one():
    db.to.insert_one({'title': "todo title", 'body': "todo body"})
    return flask.jsonify(message="success")

# @app.route("/add_one")
# def add_one():
#     one = mongo.db.collection.find()
#     # one = mongo.mydb.insert_one({'title': "todo title", 'body': "todo body"})
#     return one

if __name__ == '__main__':
    app.run(debug=True)