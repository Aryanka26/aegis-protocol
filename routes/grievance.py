from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from extensions import db
from models.grievance import Grievance
from datetime import datetime, timedelta

grievance = Blueprint('grievance', __name__)

@grievance.route("/submit-grievance", methods=["GET", "POST"])
@login_required
def submit_grievance():
    if current_user.role != "student":
        return "Access Denied"

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        category = request.form.get("category")

        new_grievance = Grievance(
            title=title,
            description=description,
            category=category,
            student_id=current_user.id
        )

        db.session.add(new_grievance)
        db.session.commit()

        return redirect(url_for("grievance.view_grievances"))

    return render_template("submit_grievance.html")


@grievance.route("/my-grievances")
@login_required
def view_grievances():
    if current_user.role != "student":
        return "Access Denied"

    grievances = Grievance.query.filter_by(student_id=current_user.id).all()
    return render_template("my_grievances.html", grievances=grievances)


@grievance.route("/all-grievances")
@login_required
def all_grievances():
    if current_user.role != "authority":
        return "Access Denied"

    grievances = Grievance.query.all()
    return render_template("all_grievances.html", grievances=grievances)

@grievance.route("/update-status/<int:id>", methods=["POST"])
@login_required
def update_status(id):
    if current_user.role != "authority":
        return "Access Denied"

    grievance_obj = Grievance.query.get_or_404(id)

    new_status = request.form.get("status")
    new_remarks = request.form.get("remarks")

    grievance_obj.status = new_status
    grievance_obj.remarks = new_remarks
    grievance_obj.updated_at = datetime.utcnow() + timedelta(hours=5, minutes=30)



    db.session.commit()

    return redirect(url_for("grievance.all_grievances"))
