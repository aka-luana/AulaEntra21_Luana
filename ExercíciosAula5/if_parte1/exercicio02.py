# Exercicio 2
# Faça um programa que peça um número.
# 
# Mostre na tela se este número é negativo ou positivo. (lembrando que números positivos são maiores que zero!)

num = int(input("Entre com um número: \n"))
if (num > 0):
    print(num, " é positivo")
elif (num < 0):
    print (num, " é negativo")
else:
    print ("Neutro (0)")