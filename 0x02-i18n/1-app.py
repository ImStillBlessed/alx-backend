#!/usr/bin/env python3
"""Basic Flask app"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """Config class for the flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "fr"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object('1-app.Config')
babel = Babel(app)


@app.route('/', strict_slashes=False)
def home():
    """Home page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
