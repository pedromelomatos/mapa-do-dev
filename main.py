from flask import Flask, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from models.database import db
from dotenv import load_dotenv
from models.database import db
import os

app =  Flask(__name__)

load_dotenv()

user = os.getenv("user")
senha = os.getenv("senha")
host = os.getenv("host")
nome_do_banco = os.getenv("nome_do_banco")

app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg://{user}:{senha}@{host}/{nome_do_banco}"

db.init_app(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
