import flask, flask_login
from project.settings import DATABASE
from .models import User

def render_auth():
    if flask.request.method == "POST":
        for user in User.query.filter_by(username = flask.request.form['username']):
            username = user.username

        user = User(
            username = username,
            password = flask.request.form["password"]
        )

        flask_login.login_user(User.query.filter_by(id = 1))
        return flask.render_template('auth.html')

    else:
        return flask.render_template('auth.html')

def render_reg():
    if flask.request.method == "POST":
        user = User(
            username = flask.request.form.get("username"),
            password = flask.request.form.get("password")
        )
        name = repr(flask_login.current_user.username)
        print(name)
        DATABASE.session.add(user)
        DATABASE.session.commit()
        return flask.redirect("/authorization/")
    else:
        return flask.render_template('reg.html')

