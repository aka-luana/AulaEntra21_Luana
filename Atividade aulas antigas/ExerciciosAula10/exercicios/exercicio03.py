"""Exercício 03

3.1) Crie um programa que cadastre o id, nome, sexo e a idade de 5 clientes.

3.2) Depois mostre os dados dos 5 clientes.

3.3) Peça para que o usuário escolha um id de um cliente e mostre as informações deste cliente.

3.4) Crie um filtro que ao digitar um id de um cliente mostre as seguintes informações:
- Para menores de 17 anos: Entrada Proibida
- Para maiores de 17 anos: Entrada Liberada
- Para o sexo Feminino: 50% de desconto
- Para o sexo Masculino: 5% de desconto
"""

listaNome  = []
listaSexo  = []
listaIdade = []
listaId    = []

print("***********************************")
print("Cadastro de clientes")
print("***********************************")

for i in range(1, 5):
    listaNome.append(input("Nome: "))
    sexo = input("Sexo (Escreva 'M' ou 'F'): ")
    listaIdade.append(int(input("Idade: ")))
    listaId.append(i)
    listaSexo.append(sexo)
    print("***********************************")

print("Todos os cadastros: ")

numCadastro = len(listaNome)

for i in range(numCadastro):
    print(f"id: {listaId[i]}")
    print(f"Nome: {listaNome[i]}")
    print(f"Idade: {listaIdade[i]}")
    print(f"Sexo: {listaSexo[i]}")
    print("***********************************")


id = int(input("Entre com o id: "))

for i in range(numCadastro):
    if (id == listaId[i]):
        print(f"id: {listaId[i]}")
        print(f"Nome: {listaNome[i]}")
        print(f"Idade: {listaIdade[i]}")
        print(f"Sexo: {listaSexo[i]}")
        if(listaIdade[i] <= 17):
            print("Entrada Proibida")
            print("***********************************")
        else:
            print("Entrada Permitida")
            if(listaSexo[i] == 'M'):
                print("5%" + " de desconto")
            else:
                print("50%" " de desconto")
        print("***********************************")
