from flask import redirect, render_template, request, url_for, session, flash

from app.models.user import User
from app.models.folder import Folder
from app.helpers.forms import FolderForm
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
    folders = User.with_id(session["id"]).folders
    if any(folder.name == form.name.data for folder in folders):
         flash("The name is alredy in use")
         return redirect(request.referrer)
    form.user_id.data = session["id"]
    if not form.validate_on_submit():
        return redirect(request.referrer)
    sanitizar_input(form)
    Folder.add(form.data)
    folders = User.with_id(session["id"]).folders
    return render_template("folder/index.html",folders=folders)


def edit(folder_id):
    if not authenticated(session):
       return redirect(url_for("home"))

    "validar que sea del usuario logeado"
    folder = Folder.with_id(folder_id)
    folders = User.with_id(session["id"]).folders
    if not folder in folders:
        return redirect(request.referrer)
    form = FolderForm()
    form.name.data = folder.name
    form.id.data = folder.id
    return render_template("folder/edit.html",form=form)


def update():
    if not authenticated(session):
       return redirect(url_for("home"))
    
    
    folders = User.with_id(session["id"]).folders
    folder = Folder.with_id(request.form["folder_id"])
    if not folder in folders:
       return redirect(request.referrer)
   
   
    if any(folder.name == request.form["name"] for folder in folders):
        flash("The name is alredy in use")
        return redirect(request.referrer)

    folder.update(request.form)
    return render_template("folder/index.html",folders=folders)


    
def delete():

    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    folder = Folder.with_id(request.form["folder_id"])
    if not folder in folders:
       return redirect(request.referrer)
   

    folder = Folder.with_id(request.form["folder_id"])
    folder.delete() 
    folders = User.with_id(session["id"]).folders
    return render_template("folder/index.html",folders=folders)

