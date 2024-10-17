import flask

tour_app = flask.Blueprint(
    name = 'tour',
    import_name = 'tour',
    template_folder = 'templates'
)