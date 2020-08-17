# Exercicio 10
# Faça um programa que peça o nome de 2 produtos, a quantidade comprada de cada produto (inteiro) e o valor (float) de cada um.
# 
# Mostre o nome a quantidade, preço por unidade e o total de cada produto.

nomeProduto1 = input("Qual o nome do produto um? \n")
qtdPrduto1 = int(input("Quantos foram comprados? \n"))
valorProduto1 = float(input("Qual o valor? \n"))
nomeProduto2 = input("Qual o nome do produto dois? \n")
qtdPrduto2 = int(input("Quantos foram comprados? \n"))
valorProduto2 = float(input("Qual o valor? \n"))

print("Produto 1: ", nomeProduto1)
print("Quantidade comprada: ", qtdPrduto1)
print("Preço por unidade: ", valorProduto1)
print("Total produto 1: R$", qtdPrduto1*valorProduto1)
print("\n")
print("Produto 2: ", nomeProduto2)
print("Quantidade comprada: ", qtdPrduto2)
print("Preço por unidade: ", valorProduto2)
print("Total produto 2: R$",qtdPrduto2*valorProduto2)
