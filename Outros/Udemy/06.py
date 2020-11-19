import random

#----- Para dar o mesmo resultado sempre é usado o .seed()
#numero2 = random.seed(1)

#----- Para sortar um numero aleatorio entre o 0 e o 10
#numero = random.randint(0, 10)
#print(numero)

#----- Sorteia/escolhe um numero dentro de uma lista
lista = [1, 20, 5, -60]
numero = random.choice(lista)
print(numero)
