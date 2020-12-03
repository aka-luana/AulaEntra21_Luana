#######################################################################################################

# Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. 

#######################################################################################################

numLimite = int(input("Digite um número: "))

for i in range(1, numLimite + 1):
    cont = 0
    for j in range(1, numLimite + 1):
        if i % j == 0:
            cont += 1
    if (cont == 2):
        print(i)
