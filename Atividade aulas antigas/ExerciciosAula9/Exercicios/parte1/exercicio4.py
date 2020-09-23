"""Exercicio 04

Faça um programa de cadastro de pessoas que receba 10 nomes, idades e e-mails e salve cada um em uma lista.

Depois mostre as listas separadamente 
(print (lista) já é o suficiente)
"""

listaNomes = []
listaIdade = []
listaEmail = []

for i in range(10):
    listaNomes.append(input(f"Digite o nome da pessoa {i}: "))
    listaIdade.append(int(input(f"Digite a idade da pessoa {i}: ")))
    listaEmail.append(input(f"Digite o email da pessoa {i}: "))

print(f"Nomes: {listaNomes} \n Idades: {listaIdade} \n Email: {listaEmail}")
