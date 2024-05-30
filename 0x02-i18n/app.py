#!/usr/bin/env python3
"""Basic Flask app"""
from datetime import datetime
from flask import Flask, g, render_template, request
from flask_babel import Babel, format_datetime
import pytz
from pytz.exceptions import UnknownTimeZoneError


class Config:
    """Config class for the flask app"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """mehod to Get user"""
    login_as = request.args.get('login_as')
    if login_as:
        return users.get(int(login_as))
    return None


@app.before_request
def before_request():
    """mehod to use the Get user method"""
    user = get_user()
    g.user = user
    if g.user and g.user.get('timezone'):
        try:
            user_timezone = pytz.timezone(g.user['timezone'])
        except UnknownTimeZoneError:
            user_timezone = pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])
    else:
        user_timezone = pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])

    current_time = datetime.now(user_timezone)
    g.current_time = format_datetime(current_time)


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    header_locale = request.headers.get('locale', '')
    if header_locale in app.config['LANGUAGES']:
        return header_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """Get timezone from request"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass
    if g.user and g.user.get('timezone'):
        try:
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def home() -> str:
    """web Home page"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
