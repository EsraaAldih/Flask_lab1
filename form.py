from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField, TextAreaField ,IntegerField
from wtforms.validators import DataRequired, Length,  InputRequired

class ToDoForm(FlaskForm):

    id = IntegerField('id')
    title = StringField('title',
                            validators=[DataRequired(), Length(min=2, max=20)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    submit = SubmitField('add to do')