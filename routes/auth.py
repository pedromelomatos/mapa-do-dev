from flask import url_for, render_template, request, redirect, Blueprint
from models.usuario import Usuario
from models.database import db
import hashlib


auth = Blueprint('auth', __name__, template_folder='../templates')


def hash(senha):
    hash_obj = hashlib.sha256(senha.encode('utf-8'))
    return hash_obj.hexdigest()


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        email= request.form['emailForm']
        senha=hash(request.form['senhaForm'])
        usuario_db = db.session.query(Usuario).filter_by(email=email, senha=senha).first()  
        if not usuario_db:
            print("Usuário inexistente")
            return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('dashboard.dashboard_home'))

@auth.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        email = request.form['emailForm']
        senha = hash(request.form['senhaForm'])
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        usuario_existe = db.session.query(Usuario).filter_by(email=email, senha=senha).first()
        if usuario_existe:
            print("Usuário já existente.")
            return redirect(url_for('auth.register'))
        elif not usuario_existe:
            db.session.add(novo_usuario)
            db.session.commit()
            print(f"USUÁRIO REGISTRADO: {novo_usuario.nome}\nSENHA:{novo_usuario.senha}")

        return redirect(url_for('dashboard.dashboard_home'))