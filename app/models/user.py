from app import db
from flask import request

from sqlalchemy.orm import relationship
from sqlalchemy import Table, Column, Integer, ForeignKey
from app.models import folder

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), unique=False)


    folders = db.relationship("Folder", back_populates="user")

    
    def __init__(self, data):
       self.username = data['username']
       self.email = data['email']
       self.password = data['password']
       db.session.commit()
        
    @classmethod
    def __str__(self):
        return '<User {}>'.format(self.username)

    def add(data):  
        db.session.add(User(data))
        db.session.commit()
        

    def all():
        return db.session.query(User).all()

    def with_email(data):
        return db.session.query(User).filter_by(email=data).first()

    def with_username(data):
        return db.session.query(User).filter_by(username=data).first()

    def with_id(data):
        return db.session.query(User).get(data)

    def with_username_and_password(data):    
        return db.session.query(User).filter(User.email == data['email']).\
            filter(User.password == data['password']).first()