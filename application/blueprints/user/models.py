from application.extensions import db


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    