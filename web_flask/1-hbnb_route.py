#!/usr/bin/python3
"""
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route0():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route1():
    return 'HBNB!'

if __name__ == "__main__":
    app.run(debug=True)
