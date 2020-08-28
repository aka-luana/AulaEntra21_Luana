"""Exercicio 03

Faça um programa que peça 10 notas do aluno. Faça a média e mostre as seguintes mensagens:

Para 7 a 10 - Aprovado
Para 5.5 a 7 - Recuperação 
Para menor de 5.5 - Reprovado
"""

somaNotas = 0

for i in range(1, 10):
    nota = float(input(f"Digite a nota {i}: "))
    if(nota > 10 or nota < 0):
        print("Nota invalida!")
        nota = float(input(f"Digite a nota {i}: "))
    somaNotas = nota + somaNotas

media = somaNotas / 10

if(media >= 7):
    print("Aprovado")
elif(media >= 5.5 and media < 7):
    print("Recuperação")
else:
    print("Reprovado")