
import flask
import flask_migrate
import flask_sqlalchemy
import os


travel_agency = flask.Flask(
    import_name= "project",
    template_folder= "templates/",
    instance_path= os.path.abspath(__file__ + "/.."),
    static_folder='static/'
)


travel_agency.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db" 

DATABASE = flask_sqlalchemy.SQLAlchemy(app=travel_agency)
MIGRATE = flask_migrate.Migrate(app=travel_agency, db=DATABASE)