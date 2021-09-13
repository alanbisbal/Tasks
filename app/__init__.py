from os import path, environ
from flask import Flask, jsonify ,render_template, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from app.db import db
from app.models.user import User




db = SQLAlchemy()

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    
    
    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tasks'
   
   
    db.init_app(app)

    @app.route("/")

    






    def home():
        return render_template("home.html")
    return app