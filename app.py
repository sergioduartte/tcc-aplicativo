from flask import Flask, render_template, request
from banco_formula import *

app = Flask(__name__)

__name__ = '__main__'

@app.route('/')
def index():
    title = "Abraão TCC"
    return render_template('index.html', title=title)


@app.route('/aplicacao')
def aplicacao():
    return render_template('aplicacao.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/resultado', methods=["POST"])
def resultado():
    momentosd = float(request.form.get("momento"))
    cortantesd = float(request.form.get("cortante"))
    axialsd = float(request.form.get("axial"))
    esbeltezx = esbeltezEmX(lb, Kx, ix)
    axialrd = axialsd
    return render_template('resultado.html', momento=momentosd, cortante=cortantesd, axial=axialsd, esbeltezx=esbeltezx)