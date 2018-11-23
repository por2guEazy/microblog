from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Eli'}
    posts = [
        {
            'author': {'username': 'Eli'},
            'body': 'A very rainy day in Corvallis.'
        },
        {
            'author': {'username': 'Kurupt'},
            'body': 'Oh, hey. What a warm chair'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)