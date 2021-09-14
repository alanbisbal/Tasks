from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, \
                    TimeField, IntegerField, SelectField, BooleanField, \
                    DateField, FloatField, DecimalField
from flask_wtf.file import FileField
from wtforms.fields.simple import HiddenField, PasswordField
from wtforms.validators import InputRequired, NumberRange, Regexp, DataRequired, Optional, EqualTo, Regexp, Email
from wtforms.fields.html5 import EmailField
from wtforms.widgets.html5 import NumberInput
import requests, time
# from flask_wtf.file import FileField, FileAllowed, FileRequired


class UserNewForm(FlaskForm):
    username = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField(label="Guardar")

class UserLoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField(label="Guardar")


class FormNewFolder(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    user_id = HiddenField(validators=[InputRequired()])
    submit = SubmitField(label="Guardar")
