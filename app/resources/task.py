from flask import redirect, render_template, request, url_for, session, flash

from app.models.task import Task
from app.models.folder import Folder
from app.models.user import User
from app.helpers.forms import FormTask,FormTaskState
from app.helpers.auth import authenticated
from app.helpers.validates import sanitizar_input

from app import db



def index():
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    return render_template("task/index.html")

def new(folder_id):
    """
    """ 
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    folder = Folder.with_id(folder_id)
    if not folder in folders:
       return redirect(request.referrer)

    form = FormTask()
    form.folder_id.data = folder_id
    
    return render_template("task/new.html",form=form)

def create():
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    folder = Folder.with_id(request.form["folder_id"])
    if not folder in folders:
       
       return redirect(url_for("home"))


    form = FormTask()
   
    if any(task.name == form.name.data for task in folder.tasks):
         flash("The name is alredy in use")
         return redirect(request.referrer)
    
    if not form.validate_on_submit():
        return redirect(request.referrer)
    
    sanitizar_input(form)
    Task.add(form.data)
    return redirect(url_for('folder_show',folder_id = folder.id))
    
def show(task_id):
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    task = Task.with_id(task_id)
    if not task:
       return redirect(url_for("home"))

    folder = Folder.with_id(task.folder_id)
    if not folder in folders:
       return redirect(url_for("home"))


    form = FormTaskState()
    return render_template("task/show.html", task= task,form=form)

def edit(task_id):
    "validar que sea del usuario logeado"
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    task=Task.with_id(task_id)
    if not task:
       return redirect(url_for("home"))

    folder = Folder.with_id(task.folder_id)
    if not folder in folders:
       return redirect(url_for("home"))


    task = Task.with_id(task_id)
    form = FormTask()
    form.name.data = task.name
    form.id.data = task.id
    return render_template("task/edit.html", form = form)

def update():
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    task=Task.with_id(request.form["task_id"])
    if not task:
       return redirect(url_for("home"))

    folder = Folder.with_id(task.folder_id)
    if not folder in folders:
       return redirect(url_for("home"))

    form = FormTaskState()
    task.update(request.form)

    return render_template("task/show.html", task= task,form=form)

def delete():
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    task=Task.with_id(request.form["task_id"])
    if not task:
       return redirect(url_for("home"))

    folder = Folder.with_id(task.folder_id)
    if not folder in folders:
       return redirect(request.referrer)
  

    task.delete() 

    return redirect(url_for('folder_show',folder_id = folder.id))

def completed():
    """
    """ 
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    task=Task.with_id(request.form["task_id"])
    if not task:
       return redirect(url_for("home"))

    folder = Folder.with_id(task.folder_id)
    if not folder in folders:
       return redirect(request.referrer)
  
    task=Task.with_id(request.form["task_id"])
    task.completed()
    return redirect(request.referrer)


def inprogress():
    """
    """
    if not authenticated(session):
       return redirect(url_for("home"))
    
    folders = User.with_id(session["id"]).folders
    task=Task.with_id(request.form["task_id"])
    if not task:
       return redirect(url_for("home"))

    folder = Folder.with_id(task.folder_id)
    if not folder in folders:
       return redirect(request.referrer)


    task.inprogress()
    return redirect(request.referrer)


