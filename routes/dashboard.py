from flask import Blueprint, render_template
from flask_login import login_required, current_user

dashboard = Blueprint('dashboard', __name__)

# STUDENT DASHBOARD
@dashboard.route("/student/dashboard")
@login_required
def student_dashboard():
    if current_user.role != "student":
        return "Access Denied"
    return render_template("student_dashboard.html")


# FACULTY DASHBOARD
@dashboard.route("/faculty/dashboard")
@login_required
def faculty_dashboard():
    if current_user.role != "faculty":
        return "Access Denied"
    return render_template("faculty_dashboard.html")


# AUTHORITY DASHBOARD
@dashboard.route("/authority/dashboard")
@login_required
def authority_dashboard():
    if current_user.role != "authority":
        return "Access Denied"
    return render_template("authority_dashboard.html")


# ADMIN DASHBOARD
@dashboard.route("/admin/dashboard")
@login_required
def admin_dashboard():
    if current_user.role != "admin":
        return "Access Denied"
    return render_template("admin_dashboard.html")
