#!/usr/bin/env python3
"""create a basic flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """babel config file"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """create a locale from request"""
    return request.accept_languages.best_match(app.config.LANGUAGES)


@app.route('/')
def index():
    """render 2-index.html"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
