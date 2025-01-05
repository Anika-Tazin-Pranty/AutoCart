from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///autocart.db'
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
@app.route('/update_user', methods=['PUT'])
def update_user():
    data = request.json
    user_id = data.get('id')
    new_username = data.get('username')
    new_email = data.get('email')
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    try:
        if new_username:
            user.username = new_username
        if new_email:
            user.email = new_email     
        db.session.commit()
        return jsonify({"message": "User information updated successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
