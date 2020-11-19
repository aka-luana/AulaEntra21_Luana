import random

aluno1 = input("Nome do aluno: ")
aluno2 = input("Nome do aluno: ")
aluno3 = input("Nome do aluno: ")
aluno4 = input("Nome do aluno: ")

print(f"O aluno sorteado para limpar o quadro é {random.choice([aluno1, aluno2, aluno3, aluno4])}")
