from flask import url_for, render_template, request, redirect, Blueprint
from flask_login import login_required
dashboard = Blueprint('dashboard', __name__, template_folder='../templates')

@dashboard.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard_home():
    return render_template("dashboard.html")

