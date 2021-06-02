from functions import a_linha_4, calc_alfa, calc_resistividade_aparente, calc_rho_h, resistencia
import flask
from flask import jsonify, request
from flask_cors import CORS

app = flask.Flask(__name__)
# app.config["DEBUG"] = True
cors = CORS(app, resources={r'/api/*': {'origins': '*'}})


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


@app.route('/api/rhoh', methods=['POST'])
def calc_rhoh():
    data = request.get_json()
    resistividade_camada_1 = data['resistividade_camada1']
    resistividade_camada_2 = data['resistividade_camada2']
    rho_h = calc_rho_h(resistividade_camada_1,
                       resistividade_camada_2)
    return jsonify({'rho_h': rho_h})


@app.route('/api/alfa', methods=['POST'])
def calc_alpha():
    data = request.get_json()
    comprimento_contrapeso = data['comprimento_contrapeso']
    distancia_contrapesos = data['distancia_contrapesos']
    altura_camada1 = data['altura_camada1']
    alfa = calc_alfa(comprimento_contrapeso,
                     distancia_contrapesos, altura_camada1)
    return jsonify({'alfa': alfa})


@app.route('/api/resistencia', methods=['POST'])
def calc_res_final():
    data = request.get_json()
    comprimento_contrapeso = data['comprimento_contrapeso']
    distancia_contrapesos = data['distancia_contrapesos']
    n = data['n']
    profundidade_instalacao = data['profundidade_instalacao']
    raio_condutor = data['raio_condutor']
    resistividade_camada1 = data['resistividade_camada1']

    resistividade_aparente = calc_resistividade_aparente(
        resistividade_camada1, n)

    a_linha = a_linha_4(raio_condutor, profundidade_instalacao,
                        distancia_contrapesos)

    resistencia_final = resistencia(
        resistividade_aparente, comprimento_contrapeso, a_linha)
    return jsonify({
        'resistividade_aparente': resistividade_aparente,
        'a_linha': a_linha,
        'resistencia': round(resistencia_final, 10)
    })


app.run()
