from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignupForm(FlaskForm):

    email = StringField('Correo electrónico', validators=[Email(message='Correo electrónico inválido'), DataRequired()])
    username = StringField('Alias', validators=[DataRequired(), Length(min=4, max=80)])
    password = PasswordField('Contraseña', validators=[DataRequired(), EqualTo('password_rep', message='Las contraseñas no coinciden')])
    password_rep = PasswordField('Repetir contraseña', validators=[DataRequired()])
    button = SubmitField('Registrarse')


class LoginForm(FlaskForm):
    email = StringField('Correo electrónico', validators=[Email(message='Correo electrónico inválido'), DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=8, max=255)])
    connected = BooleanField('Mantener conexión')
    button = SubmitField('Conectarse')
