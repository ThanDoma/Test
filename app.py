from flask import Flask, render_template
# from pymongo import PyMongo 
#, MongoClient

app = Flask(__name__)
# myclient = PyMongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]

# app.config["MONGO_URI"] = "mongodb://172.28.0.2:27017/myDatabase"
# mongo = PyMongo(app)
# client = MongoClient('mongodb://mongodb:27017/')

# mongodb_client = PyMongo(app, uri="mongodb://172.28.0.2:27017/todo_db")
# db = mongodb_client.db
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/test')
def about():
    return "<p>Hello, World!</p>"

# @app.route("/home")
# def home_page():
#     online_users = mongo.db.users.find({"online": True})
#     return render_template("index.html",
#         online_users=online_users)

if __name__ == '__main__':
    app.run(debug=True)


# client = MongoClient(host="localhost", port=27017)
# client = MongoClient("mongodb://localhost:27017")
# db = client["rptutorials"]


