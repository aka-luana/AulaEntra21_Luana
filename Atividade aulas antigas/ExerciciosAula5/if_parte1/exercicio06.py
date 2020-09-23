# Exercicio 6
# Escreva um programa que peça 2 números e mostre eles em ordem crescente

num1 = int(input("Entre com um número: \n"))
num2 = int(input("Entre com outro número: \n"))

if (num1 > num2):
    print(num2, " -> ", num1)
elif (num2 > num1):
    print(num1, " -> ", num2)
else:
    print("Números iguais")