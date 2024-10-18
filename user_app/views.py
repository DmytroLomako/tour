import flask, flask_login
from project.settings import DATABASE
from .models import User

is_login = True

def render_auth():
    global is_login, username
    try:
        print(flask_login.current_user.username)
    except:
        is_login = False
    if flask.request.method == "POST":
        for user in User.query.filter_by(username = flask.request.form['username']):
            username = user.username



            flask_login.login_user(user)
            return flask.redirect("/")
        try:
            return flask.render_template('auth.html', is_login = is_login, username = flask_login.current_user.username)
        except:
            return flask.render_template('auth.html', is_login = is_login, username = "You are Not registred")

    else:
        try:
            return flask.render_template('auth.html', is_login = is_login, username = flask_login.current_user.username)
        except:
            return flask.render_template('auth.html', is_login = is_login, username = "You are Not registred")

def render_reg():
    if flask.request.method == "POST":
        user = User(
            username = flask.request.form.get("username"),
            password = flask.request.form.get("password")
        )
        DATABASE.session.add(user)
        DATABASE.session.commit()
        return flask.redirect("/authorization/")
    else:
        return flask.render_template('reg.html')

