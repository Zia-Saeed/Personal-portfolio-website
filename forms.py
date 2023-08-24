from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, InputRequired, Regexp


class Contact(FlaskForm):
    name = StringField(label="Name", validators=[DataRequired()])
    email = StringField(label="Email", validators=[DataRequired(), Email()])
    phone = StringField('Phone Number', validators=[
        InputRequired('Phone number is required.'),
        Regexp(r'^\d{11}$', message='Phone number must be 11 digits.')
    ])
    message = TextAreaField(label="Message", validators=[DataRequired()])
    submit = SubmitField(label="Submit")