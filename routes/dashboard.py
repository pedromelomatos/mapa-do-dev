from flask import url_for, render_template, request, redirect, Blueprint
from flask_login import login_required
from routes.storage import dados_temporarios
from pypdf import PdfReader
from io import BytesIO

dashboard = Blueprint('dashboard', __name__, template_folder='../templates')

def ler_pdf():
    arquivo = request.files.get("pdf")

    pdf_na_memoria = BytesIO(arquivo.read()) #salvando pdf na memória ao invés de ter q jogar pro banco

    curriculo = PdfReader(pdf_na_memoria)

    texto_final = ""

    for pagina in curriculo.pages:
        texto_da_pagina = pagina.extract_text()

        if texto_da_pagina:
            texto_final += texto_da_pagina
    return texto_final


@dashboard.route("/dashboard/<id_curriculo>", methods=['GET', 'POST'])
@login_required
def dashboard_home(id_curriculo):
    curriculo = dados_temporarios[id_curriculo]
    print(curriculo)
    return render_template("dashboard.html")

