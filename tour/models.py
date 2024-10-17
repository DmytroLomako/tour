from project.settings import DATABASE
from project.settings import travel_agency

class Tour(DATABASE.Model):

    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    title = DATABASE.Column(DATABASE.String(50))
    date = DATABASE.Column(DATABASE.String(50))
    country = DATABASE.Column(DATABASE.String(50))
    price = DATABASE.Column(DATABASE.String(50))
    description = DATABASE.Column(DATABASE.String(50))

    def repr(self) -> str:
        return f"title : {self.title}"
    
