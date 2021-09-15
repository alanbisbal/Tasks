from flask import redirect, render_template, request, url_for, abort, session, flash

from app import db



def index():
    """
    """
    return render_template("task/index.html")

def new(folder_id):
    """
    """
    
    return render_template("task/new.html")

def create():
    """
    """
    return render_template("task/index.html")
    
def show():
    """
    """
    return render_template("task/index.html")

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


