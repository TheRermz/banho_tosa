import os
from db.db import *
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, origins="*")


@app.route("/api/cliente", methods=["GET"])
def get_all_cliente():
    return select_all_from_cliente()


@app.route("/api/pet", methods=["GET"])
def get_all_pet():
    return select_all_from_pet()


@app.route("/api/venda", methods=["GET"])
def get_all_venda():
    return select_all_from_venda()


@app.route("/api/cliente/", methods=["POST"])
def post_cliente():
    nome = request.json["nome"]
    telefone = request.json["telefone"]
    rua = request.json["rua"]
    bairro = request.json["bairro"]
    numero = request.json["numero"]
    return insert_cliente(nome, telefone, rua, bairro, numero)


@app.route("/api/pet/", methods=["POST"])
def post_pet():
    nome = request.json["nome_pet"]
    raca = request.json["raca"]
    nome_cliente = request.json["nome_cliente"]
    return insert_pet(nome, raca, nome_cliente)


@app.route("/api/venda/", methods=["POST"])
def post_venda():
    tipo_venda = request.json["tipo_venda"]
    nome_cliente = request.json["nome_cliente"]
    nome_pet = request.json["nome_pet"]
    return insert_venda(tipo_venda, nome_cliente, nome_pet)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
