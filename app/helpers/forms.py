from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.simple import HiddenField, PasswordField
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField

# from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserNewForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField(label="Guardar")

class UserLoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField(label="Guardar")


class FormNewFolder(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    user_id = HiddenField()


class FolderForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    user_id = HiddenField()
    id = HiddenField()
    
  
