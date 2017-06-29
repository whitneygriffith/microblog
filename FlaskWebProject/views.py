"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, flash, redirect
from FlaskWebProject import app
from .forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

#login page    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
