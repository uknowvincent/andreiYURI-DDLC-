from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст')
    position = StringField('Место', validators=[DataRequired()])
    speciality = StringField('Профессия', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Войти')