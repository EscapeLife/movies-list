from flask import Flask, render_template

from data import movies, name

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name=name, movies=movies)
