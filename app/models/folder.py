from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import user,task

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    tasks = db.relationship("Task", backref="tasks")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = relationship("User", backref="user")
    tasks = db.relationship("Task", backref="tasks")



    def __init__(self, data):
       self.name = data['name']
       self.user_id = data['user_id']
       db.session.commit()
        
    @classmethod
    def __str__(self):
        return '<Folder {}>'.format(self.name)

    def add(data):  
        db.session.add(Folder(data))
        db.session.commit()
        