from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import folder

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    state = db.Column(db.Boolean, nullable=False)
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'))
    folder = relationship("Folder", back_populates="tasks")


    def __init__(self, data):
       self.name = data['name']
       self.folder_id = data['folder_id']
       self.state = 0
       db.session.commit()
        
    @classmethod
    def __str__(self):
        return '<Task {}>'.format(self.name)


    def add(data):  
        db.session.add(Task(data))
        db.session.commit()

    def with_id(data):
        return db.session.query(Task).get(data)
    
    def completed(self):
        
        print("asd")
        self.state = 1
        db.session.commit()

    def inprogress(self):
        self.state = 0
        db.session.commit()


    def update(self, data):
        if self.name != data['name']:
           self.name = data['name']
        db.session.commit()
    
    def delete(self):
        print("asd")
        db.session.delete(self)
        db.session.commit()
        