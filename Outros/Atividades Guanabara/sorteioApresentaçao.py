import random

aluno1 = input("Nome do aluno: ")
aluno2 = input("Nome do aluno: ")
aluno3 = input("Nome do aluno: ")
aluno4 = input("Nome do aluno: ")

listaAlunos = []
lista = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(lista)

print(f"A ordem de apresentação é: {lista}")
