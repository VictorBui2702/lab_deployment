from app import db
from datetime import datetime

class UserVisit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow) 
    name = db.Column(db.String)