from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    team_leader = StringField('тимлид', validators=[DataRequired()])
    job = StringField('капиталистическая работа', validators=[DataRequired()])
    work_size = IntegerField('рабочий день', validators=[DataRequired()])
    collaborators = StringField('коллеги', validators=[DataRequired()])
    start_date = StringField('дата начала работы', validators=[DataRequired()])
    end_date = StringField('дата увольнения', validators=[DataRequired()])
    is_finished = BooleanField('закончена', validators=[DataRequired()])
    submit = SubmitField('стать андреем юрьевичем')
