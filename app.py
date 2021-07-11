from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# Criando rota 
@app.route('/')
# Linkando ao index.html
def index():
    return render_template('index.html')

# Verificação de Debug, irá recarregar a cada alteração do programa
if __name__ == '__main__':
    app.run(debug=True)
class Musica:
    def __init__(self, nome, artista, link):
        self.nome = nome
        self.artista = artista
        self.link = link
