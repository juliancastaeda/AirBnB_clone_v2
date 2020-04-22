#!/usr/bin/python3
"""
"""
from flask import Flask
from flask import render_template
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def index_hbnb_html(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True)
