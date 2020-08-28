"""Exercicio 06

Faça um programa que peça ao usuário que digite o nome de 10 pessoas. 
Depois mostre cada nome em linhas separadas.
"""

listaNomes = []

for i in range(3):
    listaNomes.append(input(f"Digite o nome {i}: "))

print("\n")

for i in listaNomes:
    print(f"Nome: {i}")