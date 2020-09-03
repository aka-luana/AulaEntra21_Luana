# Exercicio 12
# 
# Crie um programa que peça 2 números.
# 
# Depois mostre um menu interativo contendo 5 operações matemáticas do python
# (adição, subtração, multiplicação, divisão e expoente)
# 
# Peça para o usuário escolher uma destas opções e mostre o resultado da operação escolhida.

n1 = int(input("Entre com um número: \n"))
n2 = int(input("Entre com um número: \n"))

escolhaUser = int(input("""Escolha a operação desejada:
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
5. Expoente \n"""))

if (escolhaUser == 1):
    print("O resultado é: ", n1 + n2)
elif (escolhaUser == 2):
    print("O resultado é: ", n1 - n2)
elif (escolhaUser == 3):
    print("O resultado é: ", n1 * n2)
elif (escolhaUser == 4):
    print("O resultado é: ", n1 / n2)
elif (escolhaUser == 5):
    print("O resultado é: ", n1 ** n2)
else:
    print("Opção inválida.")
    