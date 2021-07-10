from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class Musica:
    def __init__(self, nome, artista, link):
        self.nome = nome
        self.artista = artista
        self.link = link

# @app.route('/')