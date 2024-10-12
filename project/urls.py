from home_app.views import render_home
from home_app.app import home

home.add_url_rule(rule= '/', view_func=render_home)