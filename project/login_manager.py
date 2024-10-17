import flask_login
from .settings import travel_agency
from user_app.models import User

travel_agency.secret_key = '123321'

login_manager = flask_login.LoginManager()
login_manager.init_app(travel_agency)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))