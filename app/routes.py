from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Darwin'}
    posts = [
        {
            'author': {'username': 'Jagex'},
            'body': 'MTX aint that bad!'
        },
        {
            'author': {'username': 'Blizzard'},
            'body': 'You have phones, right?'
        },
        {
            'author': {'username': 'Riot Games'},
            'body': 'Valorant is a good game.'
        },
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)