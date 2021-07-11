from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
class Musica:
    def __init__(self, nome, artista, link):
        self.nome = nome
        self.artista = artista
        self.link = link
