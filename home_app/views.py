import flask
from .models import User
from project.settings import DATABASE
from project.mail_config import mail, ADMINISTRATOR_ADDRESS
from flask_mail import Message

def render_home():
    user = User(username = flask.request.form.get('client_name'),
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