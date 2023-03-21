from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class Neweventform(FlaskForm):
        title = StringField('A program neve',validators=[DataRequired()])
        tutor = StringField('A program előadója ',validators=[DataRequired()])
        location = StringField('A program helyszíne ',validators=[DataRequired()])
        seat = IntegerField('A program helyszínének befogadóképessége ',validators=[DataRequired()])
        description = StringField('A program leírása ',validators=[DataRequired()],widget=TextArea())
        column = SelectMultipleField('A program sávjai',choices=["A sáv","B sáv","C sáv"],validators=[DataRequired()])
        submit = SubmitField('Létrehozás')