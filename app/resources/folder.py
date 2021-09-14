from flask import redirect, render_template, request, url_for, abort, session, flash

from app import db
from app.models.user import User
from app.models.folder import Folder
from app.helpers.forms import FormNewFolder, FolderForm
from app.helpers.auth import authenticated
from app.helpers.validates import sanitizar_input

def index():
    if not authenticated(session):
        return redirect(url_for("home"))
    folders = User.with_id(session["id"]).folders
    return render_template("folder/index.html",folders=folders)


def show(folder_id):
    if not authenticated(session):
        return redirect(url_for("home"))
    folder = Folder.with_id(folder_id)
    return render_template("folder/show.html",folder=folder)


def new():
    if not authenticated(session):
        return redirect(url_for("home"))
    form = FolderForm()
    return render_template("folder/new.html",form=form)

def create():
    form = FolderForm()
    form.user_id.data = session["id"]
    if not form.validate_on_submit():
        print(form.data)
        return redirect(request.referrer)
    sanitizar_input(form)
    print(form.data)
    Folder.add(form.data)
    
    folders = User.with_id(session["id"]).folders
    return render_template("folder/index.html",folders=folders)


def update(folder_id):
    if not authenticated(session):
       return redirect(url_for("home"))
    
    "validar que sea del usuario logeado"

    folder = Folder.get(folder_id)
    form = FolderForm()
    folders = Folder.all()
    return render_template("folder/index.html",folders=folders)


def update_new():
    if not authenticated(session):
       return redirect(url_for("home"))
    
    

    folders = Folder.all()
    return render_template("folder/index.html",folders=folders)

    
def delete():
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    
    return render_template("folder/index.html",folders=folders)

