from flask import url_for, render_template, request, redirect, Blueprint

auth = Blueprint('auth', __name__, template_folder='../templates')

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        email = request.form['emailForm']
        senha = request.form['senhaForm']
        return redirect(url_for('dashboard.dashboard_home'))

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")