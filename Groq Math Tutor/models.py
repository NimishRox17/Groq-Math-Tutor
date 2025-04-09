from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class MathProblem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text, nullable=False)
    input_type = db.Column(db.String(10), nullable=False)  # 'image' or 'voice'
    image_path = db.Column(db.String(255))  # Only for image inputs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)