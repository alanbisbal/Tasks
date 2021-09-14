from app import db
from flask import request


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

        