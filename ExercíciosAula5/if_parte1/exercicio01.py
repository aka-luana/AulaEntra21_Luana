# Exercicio 1
# 
# Faça um programa que peça 2 numeros inteiros e mostre o maior deles.
# 
# 
num1 = int(input("Entre com um número: \n"))
num2 = int(input("Entre com outro número: \n"))

if (num1 > num2):
    print(num1, " é maior")
elif (num2 > num1):
    print (num2, " é maior")
else:
    print ("Números iguais")
