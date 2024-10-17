from project.settings import DATABASE

class User_responce(DATABASE.Model):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    username = DATABASE.Column(DATABASE.String(50))
    email = DATABASE.Column(DATABASE.String(50))
    rewiew = DATABASE.Column(DATABASE.String(50))

    def repr(self) -> str:
        return f"user : {self.username}"