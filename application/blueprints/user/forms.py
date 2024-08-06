from my_form import MyForm
from .models import User as Obj
from sqlalchemy import not_

class Form(MyForm):
    def validate_on_submit(self):
        self.errors = {}

        if not self.first_name:
            self.errors["first_name"] = "Please type first name."

        if not self.last_name:
            self.errors["last_name"] = "Please type last name."
            
        if self.first_name and self.last_name:
            if self.id:
                duplicate = Obj.query.filter(
                    Obj.first_name == self.first_name,
                    Obj.last_name == self.last_name,
                    not_(Obj.id == self.id)
                ).first()
            else:
                duplicate = Obj.query.filter(
                    Obj.first_name == self.first_name,
                    Obj.last_name == self.last_name
                ).first()

            if duplicate:
                self.errors["last_name"] = "First and last name combination is already in record."

        return True if not self.errors else False
        