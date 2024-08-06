from flask import Blueprint, render_template, request
from .models import Disbursement
from application.extensions import db
from .forms import Form


bp = Blueprint('disbursement', __name__, template_folder="pages", url_prefix="/disbursement")


@bp.route("/")
def home():

    return render_template("disbursement/home.html")


@bp.route("/add", methods=["POST", "GET"])
def add():
    form = Form(Disbursement)
    if request.method == "POST":
        user = Disbursement()
        form.post(request, user)
        
    print(form())

    context = {
        "form": form,
    }

    return render_template("disbursement/form.html", **context)


@bp.route("/edit/<int:record_id>", methods=["POST", "GET"])
def edit(record_id):
    record = Disbursement.query.get_or_404(record_id)

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

    return render_template("disbursement/form.html", **context)

