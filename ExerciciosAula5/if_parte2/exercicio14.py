# Exercicio 14
# Crie um programa que peça ao usuário digitar um número de 1 a 7 e mostre o dia da semana correspondente sendo que segunda feira é o numero 1 e domingo é 7.

numSemana = int(input("Digite um número de 1 a 7: \n"))

if(numSemana == 1):
    print("Segunda-feira")
elif(numSemana == 2):
    print("Terça-feira")
elif(numSemana == 3):
    print("Quarta-feira")
elif(numSemana == 4):
    print("Quinta- feira")
elif(numSemana == 5):
    print("Sexta-feira")
elif(numSemana == 6):
    print("Sábado")
elif(numSemana == 7):
    print("Domingo")
else: 
    print("Número inválido.")