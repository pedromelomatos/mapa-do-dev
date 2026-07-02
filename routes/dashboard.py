from flask import url_for, render_template, request, redirect, Blueprint
from flask_login import login_required, current_user
from routes.storage import dados_temporarios
from pypdf import PdfReader
from google import genai
from io import BytesIO
from dotenv import load_dotenv
import re
import os
import json

load_dotenv()

api_chave = os.getenv("api_key")

client = genai.Client(api_key=api_chave)

dashboard = Blueprint('dashboard', __name__, template_folder='../templates')

def analisar_curriculo(curriculo):
    resposta = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="""
Você é uma IA especialista em análise de currículos para vagas de tecnologia, principalmente desenvolvimento web, estágio e nível júnior.

Considere que a data atual é 01/07/2026.

Analise o currículo abaixo e retorne exclusivamente um JSON válido, sem markdown, sem comentários, sem texto antes ou depois.


O JSON deve seguir exatamente esta estrutura:

{
"compatibilidade_junior": "",
"analise_compatibilidade": "",
"pontos_fortes": [],
"pontos_fracos": [],
"proximos_passos": [],
"resumo_ia": "",
"roadmap_personalizado": {
"titulo": "Plano de estudos de 30 dias",
"status": "Em andamento",
"semana_1": {
"titulo": "",
"descricao": ""
},
"semana_2": {
"titulo": "",
"descricao": ""
},
"semana_3": {
"titulo": "",
"descricao": ""
},
"semana_4": {
"titulo": "",
"descricao": ""
}
}
}

Regras obrigatórias:

1. Retorne apenas JSON válido.
2. Não use markdown.
3. Não use blocos de código.
4. Não use ```json.
5. Não escreva nenhuma explicação antes ou depois do JSON.
6. Não use asteriscos, negrito, títulos com ## ou listas em markdown dentro dos valores.
7. Use somente texto simples nos valores.
8. A chave "compatibilidade_junior" deve conter uma porcentagem estimada, por exemplo: "78%".
9. A chave "analise_compatibilidade" deve conter uma frase curta explicando o nível de compatibilidade com vagas júnior ou estágio.
10. A chave "pontos_fortes" deve ser uma lista de strings com os principais pontos positivos do currículo.
11. A chave "pontos_fracos" deve ser uma lista de strings com lacunas técnicas, pontos ausentes ou aspectos que precisam melhorar.
12. A chave "proximos_passos" deve ser uma lista de strings com ações práticas recomendadas para melhorar o perfil.
13. A chave "resumo_ia" deve conter um resumo geral da análise em linguagem simples, direta e profissional.
14. O roadmap deve ser personalizado com base no currículo analisado.
15. Não invente experiências profissionais, tecnologias, projetos, cursos ou resultados que não estejam no currículo.
16. Caso alguma informação importante esteja ausente, indique isso como ponto de melhoria.
17. Use uma linguagem clara, objetiva, profissional e motivadora.
18. Evite respostas genéricas. A análise deve refletir o conteúdo real do currículo.
19. A compatibilidade deve considerar principalmente vagas de estágio e desenvolvimento júnior.
20. Se o currículo for mais voltado a suporte técnico do que desenvolvimento, explique isso nos pontos fracos e nos próximos passos.

Currículo para análise:



""" + curriculo
)
    analise = resposta.text
    return analise

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


@dashboard.route("/dashboard/", methods=['GET', 'POST'])
@login_required
def dashboard_home():
    dados_analise = current_user.analise
    analise = json.loads(dados_analise)
    return render_template("dashboard.html", analise=analise)

