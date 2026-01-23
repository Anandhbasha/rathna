from flask import Flask,request,jsonify
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["testdb"]
collection = db["users"]
print("Db is connected")

# create
@app.route('/',methods=["POST"])
def create_user():
    data = request.json
    res = collection.insert_one(data)
    return jsonify({"message":"User Created Succesfully","id":str(res.inserted_id)}),201

if __name__=="__main__":
    app.run(debug=True)