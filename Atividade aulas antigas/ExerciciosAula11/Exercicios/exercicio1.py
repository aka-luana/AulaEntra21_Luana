"""Exercício 1

(não usar o continue ou o break)

Crie um programa que mostre um memu com as seguites opções:

1) Soma
2) Subtração
3) Multiplicação
S) Para sair!

Para número 1: Peça 2 números e mostre a soma deles
Para número 2: Peça 2 númeors e mostre a subtração deles
Para númeor 3: Peça 2 números e mostre a multiplicação deles
Para S: Mostre uma mensagem de despedida e termine o programa.

Para qualquer outra opção deve aparecer a mensagem "Opção Inválida"
"""

saida = True

while saida:
    escolhaUser = input("1) Soma \n 2) Subtração \n 3) Multiplicação \n S) Para sair! \n")

    if escolhaUser   == '1':
        n1 = True
        n2 = True

        num1 = input("Número um: ")
        if num1.isdigit():
            n1 = True
        else:
            n1 = False
            while n1 == False:
                num1 = input("Erro! Digite novamente o número 1: ")
                if num1.isdigit():
                    n1 = True

        num2 = input("Número dois: ")
        if num2.isdigit():
            n2 = True
        else:
            n2 = False
            while n2 == False:
                num2 = input("Erro! Digite novamente o número 2: ")
                if num2.isdigit():
                    n2 = True

        print(f"A soma é: {float(num1) + float(num2)}")

    elif escolhaUser == '2':
        n1 = True
        n2 = True

        num1 = input("Número um: ")
        if num1.isdigit():
            n1 = True
        else:
            n1 = False
            while n1 == False:
                num1 = input("Erro! Digite novamente o número 1: ")
                if num1.isdigit():
                    n1 = True

        num2 = input("Número dois: ")
        if num2.isdigit():
            n2 = True
        else:
            n2 = False
            while n2 == False:
                num2 = input("Erro! Digite novamente o número 2: ")
                if num2.isdigit():
                    n2 = True

        print(f"A subtração é: {float(num1) - float(num2)}")

    elif escolhaUser == '3':
        n1 = True
        n2 = True

        num1 = input("Número um: ")
        if num1.isdigit():
            n1 = True
        else:
            n1 = False
            while n1 == False:
                num1 = input("Erro! Digite novamente o número 1: ")
                if num1.isdigit():
                    n1 = True

        num2 = input("Número dois: ")
        if num2.isdigit():
            n2 = True
        else:
            n2 = False
            while n2 == False:
                num2 = input("Erro! Digite novamente o número 2: ")
                if num2.isdigit():
                    n2 = True

        print(f"A multiplicação é: {float(num1) * float(num2)}")

    elif (escolhaUser == 'S' or escolhaUser == 's'):
        print("Até a próxima :)")
        saida = False

    else:
        print("Opção inválida!")