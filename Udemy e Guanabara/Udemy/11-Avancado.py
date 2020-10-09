#Funcao map

def dobro(x):
    return x * 2

valor = [1, 2, 3, 4, 5]

valorDobrado = map(dobro, valor) #map(função, valor)

valorDobrado = list(valorDobrado) #Para transformar em uma lista

print(valorDobrado)