from travel_agency.settings import DATABASE

class User(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    username = DATABASE.Column(DATABASE.String(50), nullable = False)
    password = DATABASE.Column(DATABASE.String(50), nullable = False)
    def repr(self) -> str:
        return f"user : {self.username}"