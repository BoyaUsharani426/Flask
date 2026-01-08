from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/users"
mongo = PyMongo(app)

@app.route('/add', methods=['POST'])
def add_user():
    _json = request.get_json()
    _name = _json.get('name')
    _email = _json.get('email')
    _password = _json.get('pwd')

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        mongo.db.student.insert_one({
            'name': _name,
            'email': _email,
            'pwd': _hashed_password
        })

        return jsonify({"message":"User added successfully"}), 200
    else:
        return not_found()
@app.route('/users')
def users():
    users=mongo.db.student.find()
    resp=dumps(users)
    return resp
@app.route('/student/<id>',methods=['GET'])
def get_student(id):
    student=mongo.db.student.find_one({'_id':ObjectId(id)})
    resp=dumps(student)
    return resp
@app.route('/delete/<id>',methods=['DELETE'])
def delete_student(id):
    mongo.db.student.delete_one({'_id':ObjectId(id)})
    return jsonify({"message": "User delete successfully"}), 200
@app.route('/update/<id>',methods=['PUT'])
def update_student(id):
    _json = request.get_json()
    _name = _json.get('name')
    _email = _json.get('email')
    _password = _json.get('pwd')
    if _name and _email and _password:
        _hashed_password = generate_password_hash(_password)
        mongo.db.student.update_one(
            {'_id': ObjectId(id)},
    {'$set': {
        'name': _name,
        'email': _email,
        'pwd': _hashed_password
    }}
        )
        return jsonify("User updated successfully"), 200
    else:
        return not_found()

@app.errorhandler(404)
def not_found():
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url
    }
    return jsonify(message), 404

if __name__ == '__main__':
    app.run(debug=True)
