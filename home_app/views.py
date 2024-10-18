import flask, flask_login
from project.settings import DATABASE
from project.login_manager import login_manager
from flask_mail import Message
from project.mail_config import ADMINISTRATOR_ADDRESS, mail

is_login = False

def render_home():
    global is_login
    try:
        print(flask_login.current_user.username)
        is_login = True
    except:
        is_login = False

    # Проверка, была ли нажата кнопка с именем "send_email"
    if flask.request.method == 'POST':

        
        print(flask.request.form.get("send_email"))
        
    

        try:

            message = Message(
                f"Dear, {flask.request.form.get('client_name')}",
                sender = ADMINISTRATOR_ADDRESS,
                recipients= flask.request.form["client_email"],
                body = "Your review was saved"
            )

            mail.send(message)
        except:
            return "<p>email is not exist</p>"

    return flask.render_template("home.html", is_login=is_login)


