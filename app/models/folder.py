from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import user,task

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="folders")
    
    tasks = db.relationship("Task",cascade="all,delete", back_populates="folder")


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
        
    def all():
        return db.session.query(Folder).all()

    def with_id(data):
        return db.session.query(Folder).get(data)
    

    def update(self, data):
        if self.name != data['name']:
           self.name = data['name']
        db.session.commit()

    
    def delete(self):
        db.session.delete(self)
        db.session.commit()