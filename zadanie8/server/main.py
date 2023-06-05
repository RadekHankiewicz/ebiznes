from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']


    if username == 'admin' and password == 'password':
        return jsonify({'message': 'Logowanie udane!'}), 200
    else:
        return jsonify({'error': 'Niepoprawne dane logowania!'}), 401

if __name__ == '__main__':
    app.run()
