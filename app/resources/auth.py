from flask import redirect, render_template, request, url_for, abort, session, flash
from app.helpers.auth import authenticated
from app.models.user import User
from app import db
from app.helpers.validates import form_user_new, exist_email, exist_username, form_user_update, exist_email_update, exist_username_update, sanitizar_input
import bleach
from app.helpers.forms import UserLoginForm, UserNewForm


def login():
    if authenticated(session):
        return redirect(url_for("home"))
    # retorna vista de creacion de usuario
    form=UserLoginForm()
    return render_template("auth/login.html",form=form)


def signin():
    if authenticated(session):
        return redirect(url_for("home"))
    # retorna vista de creacion de usuario
    form=UserNewForm()
    return render_template("user/new.html", form=form)

def authenticate():
    """
    Este método realiza la autenticación de un usuario teniendo en cuenta si los datos ingresados son correctos,

    """

    user = User.with_username_and_password(request.form)
    if not user:
        flash("Incorrect email or password", "danger")
        return redirect(url_for("auth_login"))
    session["user"] = user.email
    session["username"] = user.username
    session["id"] = user.id
    flash("Welcome!", "success")
    return redirect(url_for("home"))


def logout():
    """
    Este método verifica si el usuario esta logueado,de ser así lo desloguea

    """
    if not authenticated(session):
        return redirect(url_for("home"))
    del session["user"]
    session.clear()
    flash("Logout!.", "success")
    return redirect(url_for("auth_login"))



def register():

    """
    Este método verifica si el usuario no esta logueado y si no existe 
    un usuario con ese email creado

    """
    
    
  
    if authenticated(session) is not None:
        return redirect(url_for("home"))
    
    data = request.form
    
    if not form_user_new(data):
        return redirect(request.referrer)

    if exist_email(data['email']):
        return redirect(request.referrer)

    if exist_username(data['username']):
        return redirect(request.referrer)

    dictUser = {
        "username": bleach.clean(data['username']),
        "email": bleach.clean(data['email']),
        "password": bleach.clean(data['password'])
    }
    
    try:
        User.add(dictUser)
        user= User.with_username_and_password(data)
        session["user"] = user.email
        session["username"] = user.username
        flash("Welcome!", "success")
    except:
        return redirect(request.referrer)
    return redirect(url_for("home"))


