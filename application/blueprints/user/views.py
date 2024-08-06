from flask import Blueprint, render_template, request
from .models import User
from application.extensions import db


bp = Blueprint('user', __name__, template_folder="pages", url_prefix="/user")


@bp.route("/")
def home():

    return render_template("user/home.html")


@bp.route("/add", methods=["POST", "GET"])
def add():
    record = User()

    if request.method == "POST":
        record.post(request.form)
        errors = record.errors

        if not errors:
            db.session.add(record)
            db.session.commit()
    else:
        errors = {}

    context = {
        "record": record,
        "column_types": record.column_types,
        "errors": errors,
    }

    return render_template("user/form.html", **context)


@bp.route("/edit/<int:record_id>", methods=["POST", "GET"])
def edit(record_id):
    record = User.query.get_or_404(record_id)

    if request.method == "POST":
        record.post(request.form)
        errors = record.errors

        if not errors:
            db.session.commit()
    else:
        errors = {}

    context = {
        "record": record,
        "column_types": record.column_types,
        "errors": errors,
    }

    return render_template("user/form.html", **context)

