import pandas as pd
from flask import Flask, jsonify,render_template

app = Flask(__name__)

#construir as funcionalidade

@app.route('/')
def homepage():
  return render_template('index.html')

@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv("advertising.csv")
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total de vendas': total_vendas}
  return jsonify(resposta)

#rodar a API
app.run(host='0.0.0.0')




