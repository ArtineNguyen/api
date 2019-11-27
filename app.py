from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
CORS(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.secret_key = 'Hello World my secret is out'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://artine:12345@localhost:5432/artiendb'


class User(UserMixin, db.Model):
    __tablename__= 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)

class Score(db.Model):
    __tablename__= 'scores'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer)
    wpm = db.Column(db.Integer)
    errors = db.Column(db.Integer)
    excerpt_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)

class Excerpts(db.Model):
    __tablename__='excerpts'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)

db.create_all()

@app.route('/')
def root():
    return jsonify(['Hello', 'World'])

@app.route('/scores', methods=['POST'])
def create_score():
    dt= request.get_json()
    score = Score(user_id = 1, time = dt['time'], wpm=dt['wpm'], errors=dt['errorCount'], excerpt_id = 1)
    return jsonify(score)

@app.route('/excerpts')
def list():
    return jsonify([
        "The enormous room on the ground floor faced",
        # more excerpts
    ])

if __name__ == "__main__":
    app.run(debug=True)