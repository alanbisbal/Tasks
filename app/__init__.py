from os import path, environ
from flask import Flask, jsonify ,render_template, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from app.db import db
from app.resources import auth,folder,user,task
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
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
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


    # Folders 

    app.add_url_rule("/index", "folder_index", folder.index)              
    app.add_url_rule("/folder/new", "folder_new", folder.new)  
    app.add_url_rule("/folder/create", "folder_create", folder.create,methods=["POST"]) 
    app.add_url_rule("/folder/show/<folder_id>", "folder_show", folder.show)                                     
    app.add_url_rule("/folder/edit/<folder_id>", "folder_edit", folder.edit)
    app.add_url_rule("/folder/update","folder_update",folder.update,methods=["POST"])
    app.add_url_rule("/folder/delete","folder_delete",folder.delete, methods=["POST"])
    @app.route("/")

    

    def home():
        return render_template("home.html")
    return app