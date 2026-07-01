from flask import url_for, render_template, request, redirect, Blueprint
from flask_login import login_required
from routes.storage import dados_temporarios
from pypdf import PdfReader
from google import genai
from io import BytesIO
from dotenv import load_dotenv
import re
import os

load_dotenv()

api_chave = os.getenv("api_key")

client = genai.Client(api_key=api_chave)

dashboard = Blueprint('dashboard', __name__, template_folder='../templates')

def limpar_texto(texto):
    #re.sub(padrão, substituição, variavel)
    texto = re.sub(r'\n+', '\n', texto)
    texto = re.sub(r'[ \t]+', ' ', texto)
    return texto.strip()

def ler_pdf():
    arquivo = request.files.get("pdf")

    pdf_na_memoria = BytesIO(arquivo.read()) #salvando pdf na memória ao invés de ter q jogar pro banco

    curriculo = PdfReader(pdf_na_memoria)

    texto_final = ""

    for pagina in curriculo.pages:
        texto_da_pagina = pagina.extract_text()

        if texto_da_pagina:
            texto_final += texto_da_pagina 

    return limpar_texto(texto_final)


@dashboard.route("/dashboard/<id_curriculo>", methods=['GET', 'POST'])
@login_required
def dashboard_home(id_curriculo):
    curriculo = dados_temporarios[id_curriculo]
    print(curriculo)
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Bom dia, tudo bem?"
    )
    print(resposta.text)
    return render_template("dashboard.html")

