'''import math

num  = int(input("Digite um número: "))

raiz = math.sqrt(num)

print("A raiz de {} é {}".format(num, math.ceil(raiz))) #Ceil arredonda o numero para cima
print("A raiz de {} é {}".format(num, math.floor(raiz))) #Floor arredonda o numero para baixo
print("A raiz de {} é {:.2f}".format(num, raiz))

from math import sqrt, floor #Quando importa algum especifico não precisa mais colocar math.

num  = int(input("Digite um número: "))

raiz = sqrt(num)

print("A raiz de {} é {:.2f}".format(num, floor(raiz)))

import random

# numAleatorio = random.random() # gera um numero aleatorio entre 0 e 1
numAleatorio = random.randint(1, 10) # gera um numero aleatorio interio entre 1 e 10

print("Você é {}!".format(numAleatorio))'''
