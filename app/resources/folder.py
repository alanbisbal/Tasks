from flask import redirect, render_template, request, url_for, abort, session, flash

from app import db



def index():
    """
    """
    return render_template("folder/index.html")

