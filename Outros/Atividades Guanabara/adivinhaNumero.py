from random import *

numUser = int(input("Tente adivinhar o número (de 0 a 5) que o computador está pensando... "))
numComputer = randint(0, 5)

if numUser == numComputer:
    print(f""""Quanta sorte!
    Seu numero {numUser}, numero computador {numComputer}""")
else:
    print(f"""Mais sorte da próxima vez!
    Seu numero {numUser}, numero computador {numComputer}""")