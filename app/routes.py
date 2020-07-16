import random
from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Léo'}
    if random.choice([True, False]):
        title = 'Home'
    else:
        title = ''

    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': user,
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.jinja', title=title, user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.jinja', title='Sign In', form=form)