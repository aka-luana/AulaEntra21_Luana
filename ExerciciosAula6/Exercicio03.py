"""Execicios 03

Escreva um programa que contenha um menu com 4 opções:
A) soma
B) média
C) divisão
D) Sair

As opções podem ser escolhidas com as letras maiusculas ou minusculas.

Para a opção soma, deve solicitar 2 números, fazer a soma e mostrar o resultado.

Para a opção média, deve solicitar 4 números, fazer a média e mostrar os resultados.

Para a opção divisão, deve solicitar 2 números, dividir o primeiro pelo segundo e montrar o resultado. Caso o segundo for igual a 0, então deve mostrar o a mensagem "Erro! Não pode dividir por ZERO!"

Para a opção sair, deve aparecer a mensagem: "Muito Obrigado e Volte sempre!"
"""

escolhaUser = input("""Escreva um programa que contenha um menu com 4 opções:
A) soma
B) média
C) divisão
D) Sair \n""")
if (escolhaUser == 'A' or escolhaUser == 'a'):
    num1 = float(input("Número 1: \n"))
    num2 = float(input("Número 2: \n"))
    print ("Resultado: ", num1 + num2)
elif (escolhaUser == 'B' or escolhaUser == 'b'):
    num1 = float(input("Número 1: \n"))
    num2 = float(input("Número 2: \n"))
    num3 = float(input("Número 3: \n"))
    num4 = float(input("Número 4: \n"))
    media = (num1 + num2 + num3 + num4)/4
    print("A média é: ", media)
elif (escolhaUser == 'C' or escolhaUser == 'c'):
    num1 = float(input("Número 1: \n"))
    num2 = float(input("Número 2: \n"))
    print ("Resultado: ", num1 / num2)
else:
    print("Hasta la vista, baby.")