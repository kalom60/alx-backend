#!/usr/bin/env python3
"""create a basic flask app"""
from flask import Flask, render_template, request, g
from typing import Dict, Union
from flask_babel import Babel


class Config:
    """babel config file"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

user = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
        }


def get_user() -> Union[Dict, None]:
    """check if request has id and return its id value or None"""
    login_as = request.args.get("login_as")
    if login_as is None:
        return None
    if int(login_as) not in user:
        return None
    if int(login_as) in user:
        return user[int(login_as)]


@app.before_request
def before_request():
    """calls get_user method and set it global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """create a locale from request"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """render 5-index.html"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
