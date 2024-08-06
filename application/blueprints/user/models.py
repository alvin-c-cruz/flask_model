from application.extensions import db
from my_model import MyModel


class User(db.Model, MyModel):
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    @property
    def errors(self):
        _errors = {}

        if not self.first_name:
            _errors["first_name"] = "Please type first name."

        if not self.last_name:
            _errors["last_name"] = "Please type last name."

        return _errors