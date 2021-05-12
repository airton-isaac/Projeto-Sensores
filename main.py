""" Arquivo principal do aplicativo """
from flask import Flask, jsonify, request
from manipula_csv import csv2json, atualiza_csv

app = Flask(__name__)

sensores = csv2json('sensores.csv')


@app.route('/')
def home():
    """ Mensagem para pagina inicial """
    return jsonify(sensores), 200


@app.route('/ListarTodos/<string:tipo>', methods=['GET'])
def retorna_todos(tipo):
    """ Retorna todos os sensores do tipo Temperatura ou Consumo """
    output = [sensor for sensor in sensores if sensor['tipo'] == tipo]
    return jsonify(output), 200


@app.route('/ListarEspecifico/<string:id>', methods=['GET'])
def retorna_especifico(i_d):
    """ Retorna um sensor de acordo com o id """
    for sensor in sensores:
        if sensor['id'] == int(i_d):
            return jsonify(sensor), 200

    return jsonify({'error': 'id não encontrado'}), 404


@app.route('/MaiorConsumo', methods=['GET'])
def maior_consumo():
    """ Retorna o sensor de consumo com maior valor """
    consumo = [sensor for sensor in sensores if sensor['tipo'] == "Consumo"]
    maior = 0
    id_out = 0
    for (i, sensor) in enumerate(consumo):
        if sensor['valor'] > maior:
            maior = sensor['valor']
            id_out = i

    return jsonify(consumo[id_out]), 200


@app.route('/MudarNome/<string:id>', methods=['PUT'])
def mudar_nome(i_d):
    """ Muda o nome de um sensor de acordo com o id """
    for sensor in sensores:
        if sensor['id'] == int(i_d):

            sensor['nome'] = request.json['nome']
            atualiza_csv('sensores.csv', int(i_d), 1, sensor['nome'])
            return jsonify(sensor), 200

    return jsonify({'error': 'id não encontrado'}), 404


@app.route('/MudarDisposicao/<string:id>', methods=['PUT'])
def mudar_disposicao(i_d):
    """ Muda a disposição de acordo com o id """
    for sensor in sensores:
        if sensor['id'] == int(i_d):

            sensor['disposicao'] = request.json['disposicao']
            atualiza_csv('sensores.csv', int(i_d), 4, sensor['disposicao'])
            return jsonify(sensor), 200

    return jsonify({'error': 'id não encontrado'}), 404


if __name__ == "__main__":
    app.run()
