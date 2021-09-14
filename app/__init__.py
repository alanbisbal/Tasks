from os import path, environ
from flask import Flask, jsonify ,render_template, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from app.db import db
from app.resources import auth
from app.helpers import auth as helper_auth
from flask_bootstrap import Bootstrap




db = SQLAlchemy()

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    
    Bootstrap(app)

    app.config['SECRET_KEY'] = 'ThisIsAVerySecretKey'
    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/tasks'
   
   
    db.init_app(app)

     # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    
    # Autenticación   
    app.add_url_rule("/register", "auth_signin", auth.signin)
    app.add_url_rule("/login", "auth_login", auth.login)
    app.add_url_rule("/logout", "auth_logout", auth.logout)
    app.add_url_rule("/authenticate",
                     "auth_authenticate",
                     auth.authenticate,
                     methods=["POST"])
    app.add_url_rule("/register",
                    "auth_register",
                    auth.register,
                    methods=["POST"])                

    @app.route("/")

    

    def home():
        return render_template("home.html")
    return app