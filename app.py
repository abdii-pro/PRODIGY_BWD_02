from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
import re
import uuid

# Email validation regex
EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

# Loading environment variables from .env file
load_dotenv()

# Initializing Flask app and configurations
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking
app.config['SQLALCHEMY_ECHO'] = True  # Optional: logs SQL queries to the console

# Initializing database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model (ORM class)
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

# validating user data
def validate_user_data(data):
    if not data.get('name') or not isinstance(data['name'], str):
        return False, "Name is required and must be a string."
    if not data.get('email') or not EMAIL_REGEX.match(data['email']):
        return False, "Invalid or missing email."
    if not data.get('age') or not isinstance(data['age'], int):
        return False, "Age is required and must be an integer."
    return True, None

# Create user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    valid, error = validate_user_data(data)
    if not valid:
        return jsonify({"error": error}), 400

    user = User(
        name=data['name'],
        email=data['email'],
        age=data['age']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }), 201

# Read all users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    } for user in users]), 200

# Read single user
@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }), 200

# Update user
@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    valid, error = validate_user_data(data)
    if not valid:
        return jsonify({"error": error}), 400

    user.name = data['name']
    user.email = data['email']
    user.age = data['age']

    db.session.commit()

    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "age": user.age
    }), 200

# Delete user
@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
