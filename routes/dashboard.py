from flask import url_for, render_template, request, redirect, Blueprint

dashboard = Blueprint('dashboard', __name__, template_folder='../templates')

@dashboard.route("/dashboard", methods=['GET', 'POST'])
def dashboard_home():
    return render_template("dashboard.html")

