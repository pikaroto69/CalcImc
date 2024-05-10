from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/calc')
def calc():
    return render_template('calc.html')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/calcular_imc', methods=['POST'])
def calcular_imc():
    altura = float(request.form['altura'])
    peso = float(request.form['peso'])
    imc = round(peso / (altura ** 2), 2)

    return render_template('calc.html', imc=imc)


if __name__ == '__main__':
    app.run(debug=True)
