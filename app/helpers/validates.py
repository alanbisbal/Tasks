from flask import flash
import bleach
from app.models.user import User

def form_user_new(data):
    ok = True
    if not data['username']:
        flash('The name cant be empty', "danger")
        ok = False
    if not data['email']:
        flash('The email cant be empty', "danger")
        ok = False
    if not data['password']:
        flash('The password cant be empty', "danger")
        ok = False
    if ok:
        return True
    else:
        return False


def exist_email(data):
    user = User.with_email(data)
    if user:
        flash("The email alredy exist, please select another", "danger")
        return True
    else:
        return False


def exist_username(data):
    user = User.with_username(data)
    if user:
        flash("The username alredy exist, please select another", "danger")
        return True
    else:
        return False


def exist_email_update(data, email):
    if data != email:
        user = User.with_email(data)
        if user:
            flash("The email alredy exist, please select another", "danger")
            return True
        else:
            return False
    return False


def exist_username_update(data, username):
    if data != username:
        user = User.with_username(data)
        if user:
            flash("The username alredy exist, please select another.", "danger")
            return True
        else:
            return False
    return False


def form_user_update(data):
    ok = True
    if not data['username']:
        flash('The username cant be empty', "danger")
        ok = False
    if not data['email']:
        flash('The email cant be empty', "danger")
        ok = False
    if not data['password']:
        flash('The password cant be empty', "danger")
        ok = False
    if ok:
        return True
    else:
        return False

def sanitizar_input(form):
    for i in form.data:
        if not isinstance(form[i].data, (int, str, float, datetime.time)):
            continue
        else:
            if form[i].data is None:
                continue
        form[i].data= bleach.clean(str(form[i].data))
