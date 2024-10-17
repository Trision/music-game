from flask import Flask
import requests
from random import choice

app = Flask('__name__')

@app.route('/')
def home():
    return '<h1>Olá, mundo. Tudo bem com você meu amor?</h1>'

@app.route('/listinha/<listinha>')
def sorte(listinha):# Sortea uma lista de músicas ou albúns escolhidos
    escolhas = []# lista de escolhas
    while len(escolhas) < 5:
        for musica in listinha:
            escolha = choice(listinha)
            if escolha not in escolhas:
                escolhas.append(escolha)
    return f'<h1>{escolhas}</h1>'# retorna as escolhas


if __name__ == "__main__":
    Debug = True
    app.run()
