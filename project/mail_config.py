from flask_mail import Mail 
from project.settings import travel_agency


ADMINISTRATOR_ADDRESS = "123travelagency123@gmail.com"
ADMINISTRATOR_PASSWORD = "hqnjfvqfjffqvqhf" 


travel_agency.config["MAIL_SERVER"] = "smtp.gmail.com"
travel_agency.config["MAIL_PORT"] = 587
travel_agency.config["MAIL_USE_TLS"] = True
travel_agency.config["MAIL_USE_SSL"] = False
travel_agency.config["MAIL_USERNAME"] = ADMINISTRATOR_ADDRESS
travel_agency.config["MAIL_PASSWORD"] = ADMINISTRATOR_PASSWORD
mail = Mail(travel_agency)