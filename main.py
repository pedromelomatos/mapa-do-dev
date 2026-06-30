from flask import Flask, url_for, render_template, request, redirect, blueprints
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth, lm
from routes.dashboard import dashboard
from models.database import db
from dotenv import load_dotenv
from models.usuario import Usuario
import os

app =  Flask(__name__)

load_dotenv()
user = os.getenv("user")
senha = os.getenv("senha")
host = os.getenv("host")
nome_do_banco = os.getenv("nome_do_banco")
secretkey = os.getenv("secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg://{user}:{senha}@{host}/{nome_do_banco}"
db.init_app(app)

app.secret_key = secretkey
lm.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(dashboard)

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html")

with app.app_context(): #with aqui é usado pra nos "conectarmos" a aplicação flask antes da gente estar app.run ela. Ativamos ela e desativamos após criarmos o db.
    db.create_all()
    print("conexão")

if __name__ == '__main__':

    app.run(host="0.0.0.0",debug=True)
    
