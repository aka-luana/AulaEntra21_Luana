# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
#
n1 = int(input("Entre com um número: \n"))
n2 = int(input("Entre com um número: \n"))
n3 = int(input("Entre com um número: \n"))

if (n1 < n2 and n2 < n3):
    print("A ordem é: ", n1, n2, n3)
if (n1 < n3 and n3 < n2):
    print("A ordem é: ", n1, n3, n2)
if (n2 < n3 and n3 < n1):
    print("A ordem é: ", n2, n3, n1)
if (n2 < n1 and n1 < n3):
    print("A ordem é: ", n2, n1, n3)
if (n3 < n2 and n2 < n1):
    print("A ordem é: ", n3, n2, n1)
if (n3 < n1 and n1 < n2):
    print("A ordem é: ", n3, n1, n2)
