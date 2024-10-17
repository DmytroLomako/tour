import flask, flask_login
from .models import User_responce
from project.settings import DATABASE
from project.login_manager import login_manager

def render_home():
    user = User_responce(username = flask.request.form.get('client_name'),
            email = flask.request.form.get('client_email'),
            rewiew = flask.request.form.get('client_review'))

    if flask.request.method == 'POST':

        # message = Message(
        #     f"Dear, {flask.request.form.get('client_name')}",
        #     sender = ADMINISTRATOR_ADDRESS,
        #     recipients= ["dmitriychep2011@gmail.com"],
        #     body = "Your review was saved"
        # )

        # mail.send(message)

        DATABASE.session.add(user)
        DATABASE.session.commit()
        
    return flask.render_template(template_name_or_list= "home.html")


