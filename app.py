from flask import Flask, render_template
from flask.helpers import url_for

from data import movies, name

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)


@app.route('/user/<name>')
def user_page(name):
    return f'User page: {name}.'
