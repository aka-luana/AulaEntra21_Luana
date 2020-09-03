"""Exercício 02

O id de um cliente é um código único (só aquela pessoa tem) composto por números inteiros 
que inicia do número 1 e vai aumentando de 1 em 1 enquanto for necessário.

Exemplo:
id: 1
Nome: Dudu

id: 2
Nome: Marta

id: 3
Nome: Pedro


ATENÇÃO!!!!
O id é um número atribuido automáticamente! O cliente não escolhe o número. O seu programa deve fazer o cadastro deste id automaticamente.


Com isso, crie um cadastro de clientes que receba o id, nome e idade. Depois mostre os dados dos clientes individualmente.
(cadastre no minimo 4 clientes)
"""

listaNome   = []
listaIdade  = []
listaCidade = []
id = 1

for i in range(4):
    listaNome.append(input("Nome: "))
    listaIdade.append(input("Idade: "))
    listaCidade.append(input("Cidade: "))
    print("***********************************")


for i in range(4):
    print(f"id: {id}")
    print(f"Nome: {listaNome[i]}")
    print(f"Idade: {listaIdade[i]}")
    print(f"Cidade: {listaCidade[i]}")
    print("***********************************")
    
    id = id + 1
