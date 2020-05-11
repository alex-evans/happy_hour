
import os
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
DB_USER = os.getenv('DB_USER')
DB_PW = os.getenv('DB_PW')

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgres://{DB_USER}:{DB_PW}@localhost:5432/hhdb'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'User {self.username}'


class List(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('lists', lazy=True))

    def __repr__(self):
        return f'<List {self.name}>'


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250))
    completed = db.Column(db.Boolean)
    due_date = db.Column(db.Date, default=datetime.utcnow)

    list_id = db.Column(db.Integer, db.ForeignKey('list.id'), nullable=False)
    list = db.relationship('List', backref=db.backref('tasks', lazy=True))

    def __repr__(self):
        return f'<Task {self.title}>'
