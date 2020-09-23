"""Exercicio 05

Faça um programa que peça ao usuário digitar a quantidade de vendas do dia. 
Cadastre cada venda separadaemnte e depois mostre a média e o valor total vendido no dia.
"""

qtdVendas = int(input("Quantas vendas foram realizadas hoje? "))

itensVendidos = []
precoItens    = []

for i in range(qtdVendas):
    itensVendidos.append(input("Qual item foi ventido? "))
    precoItens.append(float(input("Qual o preco do item? ")))

print(f"Itens vendidos: {itensVendidos}")
print(f"Média de lucro do dia: {(sum(precoItens)) / qtdVendas}")
print(f"Lucro do dia: {sum(precoItens)}")