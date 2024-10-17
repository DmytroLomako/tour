import flask, flask_login
from .models import User_responce
from project.settings import DATABASE
from project.login_manager import login_manager

def render_home():
    user = User_responce(username = flask.request.form.get('client_name'),
            email = flask.request.form.get('client_email'),
            rewiew = flask.request.form.get('client_review'))

    if flask.request.method == 'POST':

        DATABASE.session.add(user)
        DATABASE.session.commit()
    name = str(flask_login.current_user)
    print(name.username)
    return flask.render_template(template_name_or_list= "home.html")

