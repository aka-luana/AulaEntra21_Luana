# Exercicio 18
# Crie um programa que solicite o valores (inteiros) de a, b e c para o cálculo do delta
# 
# A fórmula do delta é:
# 
# delta = b²-4ac
# 
# após calcular, mostre o resultado na tela.

a = int(input("Número A: \n"))
b = int(input("Número B: \n"))
c = int(input("Número C: \n"))
print("O delta é: ", (b**2)-4*a*c)
