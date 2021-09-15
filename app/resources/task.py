from flask import redirect, render_template, request, url_for, session, flash

from app.models.task import Task
from app.models.folder import Folder
from app.helpers.forms import FormTask,FormTaskState
from app.helpers.auth import authenticated
from app.helpers.validates import sanitizar_input

from app import db



def index():
    """
    """
    return render_template("task/index.html")

def new(folder_id):
    """
    """
    if not authenticated(session):
      return redirect(url_for("home"))
    form = FormTask()
    form.folder_id.data = folder_id
    
    return render_template("task/new.html",form=form)

def create():
    """
    """
    form = FormTask()
    folder = Folder.with_id(request.form["folder_id"])
    if any(task.name == form.name.data for task in folder.tasks):
         flash("The name is alredy in use")
         return redirect(request.referrer)
    
    if not form.validate_on_submit():
        print(form.errors)
        return redirect(request.referrer)
    
    sanitizar_input(form)
    Task.add(form.data)
    return redirect(url_for('folder_show',folder_id = folder.id))
    
def show(task_id):
    """
    """

    task = Task.with_id(task_id)
    form = FormTaskState()
    return render_template("task/show.html", task= task,form=form)

def edit():
    """
    """
    return render_template("task/index.html")

def update():
    """
    """
    return render_template("task/index.html")

def delete():
    """
    """
    return render_template("task/index.html")

def completed():
    """
    """ 
    task=Task.with_id(request.form["task_id"])
    task.completed()
    return redirect(request.referrer)


def inprogress():
    """
    """
    task=Task.with_id(request.form["task_id"])
    task.inprogress()
    return redirect(request.referrer)


