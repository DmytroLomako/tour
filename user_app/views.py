import flask
from project.settings import DATABASE
from .models import User

def render_auth():
    if flask.request.method == "POST":
        user = User(
            username = flask.request.form.get("username"),
            password = flask.request.form.get("password")
        )
    else:
        return flask.render_template('auth.html')

def render_reg():
    if flask.request.method == "POST":
        user = User(
            username = flask.request.form.get("username"),
            password = flask.request.form.get("password")
        )
        return flask.redirect("/authorization/")
    else:
        return flask.render_template('reg.html')

def render_user():
    return flask.render_template('user.html')