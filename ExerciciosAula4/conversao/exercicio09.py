
# Exercicio 9
# Faça um programa que peça o nome do cliente, a quantidade do produto (inteiro) e o preço (float).
# 
# Mostre o nome do cliente e o valor total da venda.

nome = input("Qual o nome do cliente?")
qtdProduto = int(input("Quantos produtos foram comprados?"))
precoProduto = float(input("Qual o preço do produto?"))

print("O cliente ", nome, " comprou R$", qtdProduto*precoProduto)
