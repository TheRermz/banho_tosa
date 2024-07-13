import os
from db.db import *
from flask import Flask

# TODO: ADICIONAR MAIS OPÇÕES PARA O MENU

menu = """
1 - Listar todos os clientes
2 - Listar todos os pets
3 - Listar todas as vendas
4 - Adicionar cliente
5 - Adicionar pet
6 - Adicionar venda
q - Sair
"""


def clear():
    os.system("cls" if os.name == "nt" else "clear")


app = Flask(__name__)
# while True:

#     opcao = input("Insira a opção que deseja, para acessar o menu digite menu: ")
#     if opcao == "1":
#         select_all_from_cliente()
#     elif opcao == "2":
#         select_all_from_pet()
#     elif opcao == "3":
#         select_all_from_venda()
#     elif opcao == "4":
#         nome = input("Digite o nome do cliente: ")
#         telefone = input("Digite o telefone do cliente: ")
#         rua = input("Digite a rua do cliente: ")
#         bairro = input("Digite o bairro do cliente: ")
#         numero = input("Digite o número do cliente: ")
#         insert_cliente(nome, telefone, rua, bairro, numero)
#     elif opcao == "5":
#         nome = input("Digite o nome do pet: ")
#         tipo = input("Digite o tipo do pet: ")
#         nome_cliente = input("Digite o nome do cliente: ")
#         insert_pet(nome, tipo, nome_cliente)
#     elif opcao == "6":
#         nome_pet = input("Digite o nome do pet: ")
#         tipo_venda = input("Digite o tipo da venda: ")
#         nome_cliente = input("Digite o nome do cliente: ")
#         insert_venda(tipo_venda, nome_cliente, nome_pet)
#     elif opcao.lower() == "q":
#         break
#     elif opcao.lower() == "menu":
#         clear()
#         print(menu)
#     else:
#         print("Opção inválida")


@app.route("/api/cliente", methods=["GET"])
def get_all_cliente():
    return select_all_from_cliente()


@app.route("/api/pet", methods=["GET"])
def get_all_pet():
    return select_all_from_pet()


@app.route("/api/venda", methods=["GET"])
def get_all_venda():
    return select_all_from_venda()


if __name__ == "__main__":
    app.run(debug=True, port=8080)
