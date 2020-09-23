"""Exercício 3

(use somente o while)

Faça um programa que peça o nome e a idade do cliente e mostre a seguinte mensagem:

Para mairores de 18 anos: Entrada Permitida
Para menores de 18 anos: Entrada proibida.

Depois mostre a lista dos nomes (somente os nomes) das pessoas com entrada permitida.

Regras:
- O programa não pode aceitar nomes em branco. Caso não se digite um nome o programa deve mostrar a mensagem "Nome em branco" e repetir o código.
- Caso o usuário deixe em branco a idade, o progama deve mostrar uma mensagem: "Obrigado pela preferência" e terminar logo em seguida.
"""

listaNomes = []
sair       = False
temEspaco  = True

while sair == False:
    escolha = int(input("""1. Cadastro
    2. Lista dos nomes permitidos
    3. Sair \n"""))

    if(escolha == 1):
        print("Cadastro para a balada")

        nome = input("Digite o nome: ")
        if nome.isspace():
            while temEspaco:
                nome = input("Erro. Digite o nome novamente: ")
                if nome.isspace() == False:
                    temEspaco = False

        idade = input("Digite a idade: ")
        if idade.isspace():
            print("Obrigada pela preferência")
            break
        else:
            if(int(idade) >= 18):
                print("Entrada permitida! Aproveite a Festa.")
                listaNomes.append(nome)
            else:
                print("Entrada proibida! Volte daqui a alguns anos.")

    elif(escolha == 2):
        if (len(listaNomes) == 0):
            print("Nada aqui.")
        else:
            print("Lista dos nomes permitidos")
            aux = 0

            while(aux != len(listaNomes)):
                print(f"{aux + 1}. {listaNomes[aux]}")
                aux = aux + 1

    elif(escolha == 3):
        print("Até a próxima. Volte sempre :)")
        sair = True
    
    else:
        print("Opção inválida.")
    