from flask import redirect, render_template, request, url_for, abort, session, flash

from app import db
from app.models.user import User
from app.models.folder import Folder
from app.helpers.forms import FormNewFolder
from app.helpers.auth import authenticated
import bleach


def index():
    if not authenticated(session):
        return redirect(url_for("home"))

    folders = User.with_username(session["username"]).folders
   
    return render_template("folder/index.html",folders=folders)


def new():
    if not authenticated(session):
        return redirect(url_for("home"))
    form = FormNewFolder()
    return render_template("folder/new.html",form=form)

def create():
    if not authenticated(session):
        return redirect(url_for("home"))
    user = User.with_username(session["username"])
    
    data = request.form

    dictFolder = {
        "name": bleach.clean(data['name']),
        "user_id": user.id,
    }
    
    try:
        Folder.add(dictFolder)
    except:
        return redirect(request.referrer)

    folders = User.with_username(session["username"]).folders
    return render_template("folder/index.html",folders=folders)
