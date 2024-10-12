import flask
from .models import User
from project.settings import DATABASE

def render_home():
    user = User(username = flask.request.form.get('client_name'),
            email = flask.request.form.get('client_email'),
            rewiew = flask.request.form.get('client_review'))

    if flask.request.method == 'POST':

        DATABASE.session.add(user)
        DATABASE.session.commit()
        
    return flask.render_template(template_name_or_list= "home.html")