import tour
from .settings import travel_agency
import home_app
import user_app

tour.tour_app.add_url_rule(
    rule = '/tour/',
    view_func = tour.render_tour,
    methods=["GET", "POST"]
)

home_app.home.add_url_rule(
    rule= "/",
    view_func= home_app.render_home,
    methods = ["GET", "POST"]
)

tour.tour_app.add_url_rule(
    rule = '/tour/Paris/',
    view_func = tour.render_paris,
    methods=["GET", "POST"]
)

tour.tour_app.add_url_rule(
    rule = '/tour/London/',
    view_func = tour.render_london,
    methods=["GET", "POST"]
)

tour.tour_app.add_url_rule(
    rule = '/tour/Tokyo/',
    view_func = tour.render_tokyo,
    methods=["GET", "POST"]
)

user_app.user_app.add_url_rule(
    rule = '/registration/',
    view_func = user_app.render_reg,
    methods=["GET", "POST"]
)

user_app.user_app.add_url_rule(
    rule = '/authorization/',
    view_func = user_app.render_auth,
    methods=["GET", "POST"]
)

user_app.user_app.add_url_rule(
    rule = '/user/',
    view_func = user_app.render_user,
    methods=["GET", "POST"]
)

travel_agency.register_blueprint(
    blueprint= tour.tour_app
)

travel_agency.register_blueprint(
    blueprint= home_app.home
)

travel_agency.register_blueprint(
    blueprint= user_app.user_app
)