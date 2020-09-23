'''
Exercício 01

Crie um programa que cadastre 5 clientes. 

Cada cliente possui: Nome, sexo, Telefone
(Guarde estes dados em listas separadas).

Depois mostre os dados cadastrados no seguinte formato:



***********************************
Relatório de clientes cadastrados 
***********************************
Nome: 
Sexo:
Telefone:
***********************************
'''

listaNome = []
listaSexo = []
listaFone = []

print("***********************************")
print("Cadastro de clientes")
print("***********************************")

for i in range(5):
    listaNome.append(input("Nome: "))
    listaSexo.append(input("Sexo: "))
    listaFone.append(int(input("Telefone: ")))
    print("***********************************")

print("\n")

print("***********************************")
print("Registro de clientes cadastrados")
print("***********************************")

for i in range(5):
    print(f"Nome: {listaNome[i]}")
    print(f"Sexo: {listaSexo[i]}")
    print(f"Telefone: {listaSexo[i]}")
    print("***********************************")
