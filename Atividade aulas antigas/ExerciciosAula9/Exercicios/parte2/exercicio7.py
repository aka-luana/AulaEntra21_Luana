"""Exercicio 07

Faça um programa que receba 10 idades e mostre a seguinte mensagem:

Para maiores de 18 anos: Ingreços da Rave liberado!
De 16 a 18 anos: Ingreços de cinema liberado 
De 13 a 16 anos: Ingreços para fliperama liberado
Menores de 13 anos: Piscina de bolinhas liberado
"""

listaIdades = []

for i in range(10):
    listaIdades.append(int(input("Qual a idade? ")))

for i in listaIdades:
    if (i >= 18):
        print(f"{i} - Ingreços da Rave liberado!")
    elif (i >= 16 and i < 18):
        print(f"{i} - Ingreços de cinema liberado!")
    elif (i >= 13 and i < 16):
        print(f"{i} - Ingreços para fliperama liberado!")
    else:
        print(f"{i} - Piscina de bolinhas liberado!")