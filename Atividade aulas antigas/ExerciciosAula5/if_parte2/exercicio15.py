# Exercicio 15
# Crie um programa que peça ao usuário que digite um número de 1 a 12 e mostre o mês correspondente ao número.
# 
numMes = int(input("Digite um número de 1 a 12: \n"))

if(numMes == 1):
    print("Janeiro")
elif(numMes == 2):
    print("Fevereiro")
elif(numMes == 3):
    print("Março")
elif(numMes == 4):
    print("Abril")
elif(numMes == 5):
    print("Maio")
elif(numMes == 6):
    print("Junho")
elif(numMes == 7):
    print("Julho")
elif(numMes == 8):
    print("Agosto")
elif(numMes == 9):
    print("Setembro")
elif(numMes == 10):
    print("Outubro")
elif(numMes == 11):
    print("Novembro")
elif(numMes == 12):
    print("Dezembro")
else: 
    print("Número inválido.")