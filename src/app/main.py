from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression
import pickle

colunas = ['tamanho', 'ano', 'garagem']
modelo = pickle.load(open('models/modelo.sav', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/cotacao/', methods=['POST'])
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])

    return jsonify(preco=preco[0])

app.run(debug=True, host='0.0.0.0')
