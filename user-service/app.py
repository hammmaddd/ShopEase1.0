from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    # Placeholder for user registration logic
    return jsonify({"message": "User registered!"}), 201

@app.route('/login', methods=['POST'])
def login():
    # Placeholder for user login logic
    return jsonify({"message": "User logged in!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))