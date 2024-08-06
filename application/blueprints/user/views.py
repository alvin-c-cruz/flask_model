from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import User
from application.extensions import db
from sqlalchemy.orm.exc import NoResultFound
from .forms import Form


bp = Blueprint('user', __name__, template_folder="pages", url_prefix="/user")


@bp.route("/")
def home():
    users = User.query.order_by("last_name", "first_name").all()
    
    context = {
        "users": users
    }

    return render_template("user/home.html", **context)


@bp.route("/add", methods=["POST", "GET"])
def add():
    form = Form(User)
    if request.method == "POST":
        user = User()
        form.post(request, user)
        print(form.validate_on_submit())
        if form.validate_on_submit():
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.home'))
        
    context = {
        "form": form,
    }

    return render_template("user/form.html", **context)


@bp.route("/edit/<int:record_id>", methods=["POST", "GET"])
def edit(record_id):
    user = User.query.get_or_404(record_id)
    form = Form(User)

    if request.method == "POST":
        form.post(request, user)
        if form.validate_on_submit():
            db.session.commit()
            return redirect(url_for('user.home'))
    else:
        form.get(user)

    context = {
        "form": form,
    }

    return render_template("user/form.html", **context)


@bp.route("/delete/<int:record_id>", methods=["POST", "GET"])
def delete(record_id):
    user = User.query.get_or_404(record_id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully.", "success")
    except Exception as e:
        db.session.rollback()
        flash("An error occurred while trying to delete the user.", "error")
    
    return redirect(url_for("user.home"))