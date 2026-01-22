from flask import Flask,jsonify,request

app = Flask(__name__)

users = [{
    "id":1,"name":"arun","course":"Python"
}]

@app.route('/',methods=["GET"])
def index():
    return jsonify(users),200

@app.route("/",methods=["POST"])
def createNew():
    data = request.json
    users.append(data)
    return jsonify(users,"Added Succesfully"),201

@app.route('/updateUser/<int:id>',methods=["PUT"])
def update(id):
    data = request.json
    for user in users:
        if user['id'] ==id:
            user.update(data)
            return jsonify({'message':"user Upadated Succesfully"}),207
        
@app.route('/deleteuser/<int:id>',methods=["DELETE"])
def delete(id):
    for user in users:
        if user['id'] ==id:
            users.remove(user)
            return jsonify({'message':"user Deleted Succesfully"}),206
if __name__ =="__main__":
    app.run(debug=True)