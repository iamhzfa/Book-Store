from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, IntegerField, PasswordField, SelectField, FileField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegisterForm(FlaskForm):
    name = StringField(label='Your Name', validators = [Length(min=3, max=30), DataRequired()])
    username = StringField(label='Create Username', validators = [Length(min=3, max=30), DataRequired()])
    email = StringField(label='Your Email', validators = [Email(), DataRequired()])
    password = PasswordField(label='Create Password', validators = [Length(min=3, max=30), DataRequired()])
    confirm_password = PasswordField(label='Confirm Password', validators = [EqualTo('password'), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='Enter Username', validators =[DataRequired()])
    password = PasswordField(label='Enter Password', validators = [ DataRequired()])
    submit = SubmitField(label='Sign IN')

class sellingForm(FlaskForm):
    streamName = SelectField(label='Book Stream', choices=['Universities', 'School','Competition'],validate_choice=[DataRequired()])
    bookName = StringField(label= 'Book Name:', validators=[Length(min=2, max=30),DataRequired()])
    subjectName = StringField(label= 'Subject Name :', validators=[Length(min=2, max=20), DataRequired()])
    className = IntegerField(label= 'Class:')
    mfgYear = IntegerField(label= 'Manufacturing Year:', validators=[DataRequired()])
    sellingAmount = IntegerField(label= 'Selling Amount:', validators=[DataRequired()])
    publicationName = StringField(label= 'Publication Name :', validators=[Length(min=2, max=20),DataRequired()])
    quantity = IntegerField(label='Qunatity: ', validators=[DataRequired()])
    bookImage = FileField(label = 'Book Image: ', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    submit = SubmitField(label='Add Book')