from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import folder

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
    folder = relationship("Folder", backref="folder")
    

    def __init__(self, data):
       self.name = data['name']
       self.folder_id = data['folder_id']
       db.session.commit()
        
    @classmethod
    def __str__(self):
        return '<Task {}>'.format(self.name)


    def add(data):  
        db.session.add(Task(data))
        db.session.commit()
        