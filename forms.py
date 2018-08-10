from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your First Name")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your Last Name")])
	email = StringField('Email', validators=[DataRequired("Please enter your Email address")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your Password")])
	submit = SubmitField('Sign Up')