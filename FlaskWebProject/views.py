"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect
from FlaskWebProject import app
from .forms import LoginForm, User

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )

#login page that validates and stores the form data    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/home')
    return render_template('login.html', 
                           title='Sign In',
                           form=form)


@app.route('/user', methods=['GET', 'POST'])
def user():
    form1 = User()
    if form1.validate_on_submit():
        return redirect('/home')
    return render_template('user.html', 
                           title='User Info',
                           form=form1)