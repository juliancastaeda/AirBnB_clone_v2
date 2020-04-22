#!/usr/bin/python3
"""
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index_hbnb_C(text):
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index_hbnb_python(text='is cool'):
    return "Python %s" % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def index_hbnb_int(n):
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(debug=True)
