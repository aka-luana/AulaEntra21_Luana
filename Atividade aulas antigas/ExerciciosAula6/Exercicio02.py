"""Execicios 02

Escreva um programa que receba 4 notas e calcule a média.
Mostre a seguinte mensagem conforme a media final.

Media Final
de 0 a 5 - Reprovado
de 5 a 6.5 - Recuperação
de 6.5 a 9 - Aprovado
Acima de 9 - Aprovado com louvor
"""

nota1 = float(input("Qual a nota? \n"))
nota2 = float(input("Qual a nota? \n"))
nota3 = float(input("Qual a nota? \n"))
nota4 = float(input("Qual a nota? \n"))
media = (nota1+nota2+nota3+nota4)/4
if(media <= 5):
    print("Reprovado")
elif(media >= 5.1 and media <= 6.5):
    print("Recuperação")
elif(media >= 6.5 and media <= 9):
    print("Aprovado")
else:
    print("Aprovado com louvor")