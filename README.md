# 🚀 Mapa do Dev

O Mapa do Dev é uma plataforma em desenvolvimento para analisar currículos de profissionais de tecnologia e transformar essas informações em um plano de evolução personalizado.

A proposta do projeto é ajudar estudantes, pessoas em transição de carreira e desenvolvedores juniores a entender melhor seus pontos fortes, identificar lacunas técnicas e descobrir os próximos passos necessários para se aproximarem de uma oportunidade no mercado.

## Status do Projeto

MVP em desenvolvimento.

O projeto já possui a base visual e estrutural da aplicação, incluindo páginas de apresentação, login, cadastro e dashboard demonstrativo. A análise real com IA e o processamento completo de currículos ainda fazem parte do planejamento.

## O que já está pronto

* Landing page apresentando a proposta do Mapa do Dev.
* Tela de login.
* Tela de cadastro.
* Dashboard demonstrativo com:

  * Compatibilidade com vaga júnior;
  * Pontos fortes;
  * Pontos fracos;
  * Próximos passos;
  * Resumo da análise;
  * Roadmap de estudos de 30 dias.
* Estrutura Flask organizada com Blueprints.
* Modelo inicial de usuário com SQLAlchemy.
* Configuração de banco PostgreSQL via variáveis de ambiente.
* Arquivos CSS separados por responsabilidade.
* Scripts JavaScript iniciais para interações de formulário e simulação de upload.

## Prints das Páginas

### Home

![Home do Mapa do Dev](static/img/screenshots/home.png)

### Login

![Tela de login do Mapa do Dev](static/img/screenshots/login.png)

### Cadastro

![Tela de cadastro do Mapa do Dev](static/img/screenshots/register.png)

### Dashboard

![Dashboard do Mapa do Dev](static/img/screenshots/dashboard.png)

## O que está planejado

* Upload real de currículo em PDF.
* Leitura e extração de texto do currículo.
* Integração com IA para gerar análises personalizadas.
* Cadastro de usuários com persistência de dados no banco.
* Login com autenticação real e gerenciamento de sessões.
* Histórico de currículos analisados.
* Dashboard dinâmico baseado no perfil do usuário.
* Roadmaps personalizados para áreas como Front-end, Back-end, Dados e Mobile.
* Sugestões de estudos, projetos práticos e próximas tecnologias para aprender.
* Exportação do plano de evolução em PDF.
* Melhorias de segurança, validação e tratamento de erros.
* Testes automatizados para rotas, modelos e fluxos principais.

## Tecnologias Utilizadas

* Python
* Flask
* Flask-SQLAlchemy
* PostgreSQL
* Psycopg
* Python-dotenv
* HTML
* CSS
* JavaScript

## Estrutura do Projeto

```text
mapa-do-dev/
|-- main.py
|-- models/
|   |-- database.py
|   `-- usuario.py
|-- routes/
|   |-- auth.py
|   `-- dashboard.py
|-- static/
|   |-- css/
|   |-- img/
|   `-- js/
|-- templates/
|   |-- dashboard.html
|   |-- index.html
|   |-- login.html
|   `-- register.html
`-- README.md
```

## Como Rodar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/mapa-do-dev.git
cd mapa-do-dev
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install Flask Flask-SQLAlchemy psycopg python-dotenv
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
user=seu_usuario
senha=sua_senha
host=localhost
nome_do_banco=mapa_do_dev
```

### 5. Execute a aplicação

```bash
python main.py
```

### 6. Acesse no navegador

```text
http://localhost:5000
```

## Observações

Este projeto ainda está em fase inicial. Algumas telas já representam a experiência planejada, porém parte dos dados exibidos no dashboard ainda é demonstrativa.

O objetivo final é que o usuário envie um currículo, receba uma análise personalizada por IA 🤖 e acompanhe um plano prático de evolução profissional, com sugestões de estudo, projetos e metas alinhadas ao seu perfil.
