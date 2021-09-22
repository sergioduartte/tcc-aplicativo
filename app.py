from flask import Flask, render_template, request
from formulas.formulas_normal import *

app = Flask(__name__)

if (__name__ == '__main__'):
    app.run(debug=True)


@app.route('/')
def index():
    title = "Abraão TCC"
    return render_template('index.html', title=title)


@app.route('/resultado', methods=["POST"])
def resultado():
    momentosd = float(request.form.get("momento"))
    cortantesd = float(request.form.get("cortante"))
    normalsd = float(request.form.get("normalsd"))
    lb = float(request.form.get("lb"))
    kx = float(request.form.get("kx"))
    ky = float(request.form.get("ky"))
    kz = float(request.form.get("kz"))
    
    resist = resiste(normalsd, lb, kx, ky, kz)

    return render_template('resultado.html', normalsd=normalsd, lb=lb, kx=kx, ky=ky, kz=kz, resiste=resist)






