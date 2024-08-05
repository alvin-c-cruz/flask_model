from my_form import MyForm
from .models import DisbursementDetail
import json

DETAIL_ROWS = 10


class SubForm(MyForm):
    def validate_on_submit(self):
        #  Validates the form fields and populates the errors dictionary if any fields are missing.
        self.errors = {}

        if not self.description:
            self.errors["description"] = "Please type description"

        if not self.amount:
            self.errors["amount"] = "Please type amount."

        return True if not self.errors else False

    def is_dirty(self):
        #  Determines if any of the form fields are not empty).
        return any([self.description, self.amount])
    
    def __str__(self):
        return json.dumps({"description": self.description, "amount": self.amount}, indent=4)


class Form(MyForm):
    def __init__(self, model):
        super().__init__(model)

        self.details = []
        for i in range(DETAIL_ROWS):
            self.details.append(SubForm(DisbursementDetail))

    def enumerated_details(self):
        return enumerate(self.details)

    def validate_on_submit(self):
        self.errors = {}

        if not self.user_id:
            self.errors["user_id"] = "Please select user."

        return True if not self.errors else False
    