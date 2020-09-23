"""Exercício 2

(não usar o continue ou o break)

Crie um menu interativo com as seguintes opções:

A) soma
B) Média
C) Taboada
S) Sair


Para A: Peça 2 números, some e mostr o resultado
Para B: Peça 4 números, faça a média e mostre o resultado
Para C: Peça um número e mostre a taboada dele
Para S: Mostre uma mensagem de despidida e encerre o programa.
Para qualquer outro valor: Mostre a mensagem "opção inválida" """

saida = True

while saida:
    escolhaUser = input("1) Soma \n 2) Media \n 3) Tabuada \n S) Sair \n OBS: Apenas números inteiros.")

    if escolhaUser   == '1':
        n1 = True
        n2 = True

        num1 = input("Número um: ")
        if num1.isdigit() or num1.isdecimal():
            n1 = True
        else:
            n1 = False
            while n1 == False:
                num1 = input("Erro! Digite novamente o número 1: ")
                if num1.isdigit() or num1.isdecimal():
                    n1 = True

        num2 = input("Número dois: ")
        if num2.isdigit() or num2.isdecimal():
            n2 = True
        else:
            n2 = False
            while n2 == False:
                num2 = input("Erro! Digite novamente o número 2: ")
                if num2.isdigit() or num2.isdecimal():
                    n2 = True

        print(f"A soma é: {float(num1) + float(num2)}")

    elif escolhaUser == '2':
        n1 = True
        n2 = True
        n3 = True
        n4 = True

        num1 = input("Número um: ")
        if float(num1) >= 0 and float(num1) <= 10 and (num1.isdigit() or (float(num1) % 1 != 0)):
            n1 = True
        else:
            n1 = False
            while n1 == False:
                num1 = input("Erro! Digite novamente o número 1: ")
                if float(num1) >= 0 and float(num1) <= 10 and (num1.isdigit() or (float(num1) % 1 != 0)):
                    n1 = True

        num2 = input("Número dois: ")
        if float(num2) >= 0 and float(num2) <= 10 and (num2.isdigit() or (float(num2) % 1 != 0)):
            n2 = True
        else:
            n2 = False
            while n2 == False:
                num2 = input("Erro! Digite novamente o número 2: ")
                if float(num2) >= 0 and float(num2) <= 10 and (num2.isdigit() or (float(num2) % 1 != 0)):
                    n2 = True

        num3 = input("Número três: ")
        if float(num3) >= 0 and float(num3) <= 10 and (num3.isdigit() or (float(num3) % 1 != 0)):
            n3 = True
        else:
            n3 = False
            while n3 == False:
                num3 = input("Erro! Digite novamente o número 3: ")
                if float(num3) >= 0 and float(num3) <= 10 and (num3.isdigit() or (float(num3) % 1 != 0)):
                    n3 = True
        
        num4 = input("Número quatro: ")
        if float(num4) >= 0 and float(num4) <= 10 and (num4.isdigit() or (float(num4) % 1 != 0)):
            n4 = True
        else:
            n4 = False
            while n4 == False:
                num4 = input("Erro! Digite novamente o número 4: ")
                if float(num4) >= 0 and float(num4) <= 10 and (num4.isdigit() or (float(num4) % 1 != 0)):
                    n4 = True

        print(f"A média é: {(float(num1) + float(num2) + float(num3) + float(num4))/4:.2f}")

    elif escolhaUser == '3':
        n1 = True

        num1 = input("Escolha o número da tabuada: ")
        if num1.isdigit():
            n1 = True
            num1 = int(num1)
        else:
            n1 = False
            while n1 == False:
                num1 = input("Erro! Digite novamente um número: ")
                if num1.isdigit():
                    num1 = int(num1)
                    n1 = True

        print("A tabuada é: ")
        for i in range(11):
            print(f"{num1} x {i} = {num1 * i}")

    elif (escolhaUser == 'S' or escolhaUser == 's'):
        print("Tchaaaaaau :)")
        saida = False

    else:
        print("Opção inválida!")