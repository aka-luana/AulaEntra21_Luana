# Exercicio 8
# Faça um programa que peça 3 números inteiros e mostre o número maior.

n1 = int(input("Entre com um número: \n"))
n2 = int(input("Entre com um número: \n"))
n3 = int(input("Entre com um número: \n"))

if (n1 > n2 and n1 > n3):
    print (n1, " é o maior número")
elif (n2 > n1 and n2 > n3):
    print (n2, " é o maior número")
else:
    print (n3, " é o maior número")

