# Exercicio 7
# Faça um programa que peça 3 números inteiros e mostre o menor número.

n1 = int(input("Entre com um número: \n"))
n2 = int(input("Entre com um número: \n"))
n3 = int(input("Entre com um número: \n"))

if (n1 < n2 and n1 < n3):
    print (n1, " é o menor número")
elif (n2 < n1 and n2 < n3):
    print (n2, " é o menor número")
else:
    print (n3, " é o menor número")
