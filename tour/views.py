import flask
from .models import Tour
from project.settings import travel_agency

all_titles = []
with travel_agency.app_context():
    all_tours = Tour.query.all()
    tour_paris = Tour.query.filter_by(title='Paris').first()
    tour_london = Tour.query.filter_by(title='London').first()
    tour_tokyo = Tour.query.filter_by(title='Tokyo').first()
for tour in all_tours:
    print(tour.title)
    all_titles.append(tour.title)

def render_tour():
    return flask.render_template(template_name_or_list='tour.html', titles = all_titles)

def render_paris():
    return flask.render_template(template_name_or_list='paris.html', title = tour_paris.title, date = tour_paris.date, country = tour_paris.country)

def render_london():
    return flask.render_template(template_name_or_list='london.html', title = tour_london.title, date = tour_london.date, country = tour_london.country)

def render_tokyo():
    return flask.render_template(template_name_or_list='tokyo.html', title = tour_tokyo.title, date = tour_tokyo.date, country = tour_tokyo.country)