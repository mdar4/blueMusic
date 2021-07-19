from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Musica():
    def __init__(self, nome, artista, link):
        self.nome = nome
        self.artista = artista
        self.link = link

# Criando rota 
@app.route("/")
# Linkando ao index.html
def index():
    return render_template('index.html')

@app.route("/new")
def new():
    return render_template('new.html')

@app.route('/edit/<id>')
def edit(id):
    return render_template('new.html')

# Verificação de Debug, irá recarregar a cada alteração do programa
if __name__ == '__main__':
    app.run(debug=True)
