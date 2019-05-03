from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)
@app.route('/')
def home():
    return 'hello world!'

# ... later ... 
DATABASE_URL = "postgres://gubotprsqzqsxq:9f535a5d7d191b9a145a2e50910d814fe7afdf9faf321f962a78c934932e7964@ec2-174-129-10-235.compute-1.amazonaws.com:5432/db8jcps7q9hrkf"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

migrate = Migrate(app,db) 