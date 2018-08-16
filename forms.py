from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class SignupForm(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your First Name")])
	last_name = StringField('Last name', validators=[DataRequired("Please enter your Last Name")])
	email = StringField('Email', validators=[DataRequired("Please enter your Email address")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your Password")])
	submit = SubmitField('Sign Up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Please Enter correct Email"), Email("Please enter correct email")])
	password = PasswordField('Password', validators=[DataRequired("Please Enter your password")])
	submit = SubmitField('Login')

class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired('Please enter address')])
	submit = SubmitField('Search')