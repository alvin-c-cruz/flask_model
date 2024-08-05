from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Disbursement, DisbursementDetail
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
        
        # Clear existing details
        disbursement.disbursement_details = []

        for i, detail_form in enumerate(form.details):
            disbursement_detail = DisbursementDetail()
            detail_form.post(request, disbursement_detail, i)

            if detail_form.is_dirty():
                disbursement.disbursement_details.append(disbursement_detail)

        if form.validate_on_submit():
            db.session.add(disbursement)
            db.session.commit()  # Commit all changes together
            
            return redirect(url_for('disbursement.home'))
        
    context = {
        "form": form,
        "user_options": user_options
    }

    return render_template("disbursement/form.html", **context)


@bp.route("/edit/<int:record_id>", methods=["POST", "GET"])
def edit(record_id):
    user_options = [(user.id, user) for user in User.query.order_by("first_name", "last_name").all()]
    
    # Retrieve the existing disbursement
    disbursement = Disbursement.query.get_or_404(record_id)
    form = Form(Disbursement)
    
    if request.method == "POST":
        form.post(request, disbursement)
        
        # Clear existing details
        for detail in disbursement.disbursement_details:
            db.session.delete(detail)

        for i, detail_form in enumerate(form.details):
            disbursement_detail = DisbursementDetail()
            detail_form.post(request, disbursement_detail, i)

            if detail_form.is_dirty():
                disbursement.disbursement_details.append(disbursement_detail)

        if form.validate_on_submit():
            # db.session.add(disbursement)
            db.session.commit()  # Commit all changes together
            
            return redirect(url_for('disbursement.home'))
        
    else:
        # Populate form with existing data
        form.get(disbursement)
        for i, detail_obj in enumerate(disbursement.disbursement_details):
            form.details[i].get(detail_obj)
        
    context = {
        "form": form,
        "user_options": user_options
    }

    return render_template("disbursement/form.html", **context)


@bp.route("/delete/<int:record_id>")
def delete(record_id):
    # Retrieve the disbursement record or return a 404 if not found
    disbursement = Disbursement.query.get_or_404(record_id)
    
    # Delete all associated DisbursementDetail records
    for detail in disbursement.disbursement_details:
        db.session.delete(detail)
    
    # Delete the Disbursement record itself
    db.session.delete(disbursement)
    
    # Commit the transaction to save changes
    db.session.commit()
    
    # Flash a success message and redirect to the home page
    flash('Disbursement and its details have been successfully deleted.', 'success')
    return redirect(url_for('disbursement.home'))
