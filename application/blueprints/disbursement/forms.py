from my_form import MyForm

class Form(MyForm):
    def validate_on_submit(self):
        self.errors = {}

        if not self.user_id:
            self.errors["user_id"] = "Please select user."

        return self.errors