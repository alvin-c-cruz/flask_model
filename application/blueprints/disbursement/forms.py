from my_form import MyForm
from .models import DisbursementDetail

DETAIL_ROWS = 10


class SubForm(MyForm):
    def validate_on_submit(self):
        self.errors = {}

        if not self.description:
            self.errors["description"] = "Please type description"

        if not self.amount:
            self.errors["amount"] = "Please type amount."

        return True if not self.errors else False

    def is_dirty(self):
        return any([getattr(self, column) for column in self.get_columns().keys()])


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
    