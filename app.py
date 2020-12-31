from flask import Flask
from flask.helpers import url_for

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Welcome to watch list!'


@app.route('/user/<name>')
def user_page(name):
    return f'User page: {name}.'


@app.route('/test')
def test_url_for():
    print(url_for('hello'))                    # /
    print(url_for('test_url_for'))             # /test
    print(url_for('user_page', name='peter'))  # /user/peter
    print(url_for('test_url_for', num=2))      # /test?num=2
    return "Test page."
