from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired, NumberRange

class Answer(FlaskForm):
    answer = IntegerField('Ваш ответ:', validators=[DataRequired(), NumberRange(min=10, max=99)])
