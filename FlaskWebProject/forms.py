from flask_wtf import Form
from wtforms import StringField, BooleanField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional

# TODO: Change to OAuth
class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

#Shift Assignment Form
class User(Form):
	user_id = StringField('userid', validators=[DataRequired()])
   