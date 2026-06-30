from flask import url_for, render_template, request, redirect, Blueprint
from models.usuario import Usuario
from models.database import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
import hashlib

lm = LoginManager()

auth = Blueprint('auth', __name__, template_folder='../templates')

lm.login_view = 'auth.login' #se não estiver logado mandamos pra route /login

@lm.user_loader #pra quando o flask precisar de infos do current_user, damos essa função pra ele que retorna um obj do usuário
def user_loader(id):
    id=int(id)
    usuario = db.session.query(Usuario).filter_by(id=id).first()
    return usuario


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
            login_user(usuario_db)
            print("Usuário Logado")
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
        login_user(usuario_existe)
        return redirect(url_for('dashboard.dashboard_home'))