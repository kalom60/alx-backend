#!/usr/bin/env python3
"""
Flask app
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """
    Configuration for Babel
    """
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
    """check if request has id and return its id value or None"""
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    """calls get_user method and set it global on flask.g.user"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """
    create a locale from request
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """render 5-index.html"""
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
