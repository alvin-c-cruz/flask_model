from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Disbursement
from application.extensions import db
from .forms import Form
from .. user import User


bp = Blueprint('disbursement', __name__, template_folder="pages", url_prefix="/disbursement")


@bp.route("/")
def home():
    disbursements = Disbursement.query.all()
    
    context = {
        "disbursements": disbursements
    }

    return render_template("disbursement/home.html", **context)


@bp.route("/add", methods=["POST", "GET"])
def add():
    user_options = [(user.id, user) for user in User.query.order_by("first_name", "last_name").all()]
    form = Form(Disbursement)
    if request.method == "POST":
        disbursement = Disbursement()

        form.post(request, disbursement)
        
        for i, detail_form in enumerate(form.details):
            if detail_form.is_dirty():
                detail_form.post(request, disbursement.disbursement_details[i])

        if form.validate_on_submit():
            db.session.add(disbursement)
            for i, detail_obj in enumerate(disbursement.disbursement_details):
                if form.details[i].is_dirty():
                    detail_obj.disbursement_id = disbursement.id
                    db.session.add(detail_obj)
            db.session.commit()
            
            return redirect(url_for('disbursement.home'))
        
    context = {
        "form": form,
        "user_options": user_options
    }

    return render_template("disbursement/form.html", **context)


# @bp.route("/edit/<int:record_id>", methods=["POST", "GET"])
# def edit(record_id):
#     user = User.query.get_or_404(record_id)
#     form = Form(User)

#     if request.method == "POST":
#         form.post(request, user)
#         if form.validate_on_submit():
#             db.session.commit()
#             return redirect(url_for('user.home'))
#     else:
#         form.get(user)

#     context = {
#         "form": form,
#     }

#     return render_template("user/form.html", **context)


# @bp.route("/delete/<int:record_id>", methods=["POST", "GET"])
# def delete(record_id):
#     user = User.query.get_or_404(record_id)
    
#     try:
#         db.session.delete(user)
#         db.session.commit()
#         flash("User deleted successfully.", "success")
#     except Exception as e:
#         db.session.rollback()
#         flash("An error occurred while trying to delete the user.", "error")
    
#     return redirect(url_for("user.home"))