####################################################################################################### 

# Faça um Programa que peça os 3 lados de um triângulo.
# O programa deverá informar se os valores podem ser um triângulo.
# Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

#######################################################################################################

def triangulos(lado1, lado2, lado3):
    lista_lados = [lado1, lado2, lado3]
    lista_lados = sorted(lista_lados, reverse=True)
    lado1, lado2, lado3 = lista_lados[0], lista_lados[1], lista_lados[2]
    if (lado1 >= lado2 + lado3):
        print("Não forma triângulo")
    else:
        if lado1 == lado2 and lado1 == lado3:
            print("Triângulo equilátero")
        elif lado1 == lado2 and lado1 != lado3 or lado2 == lado3 and lado2 != lado1 or lado1 == lado3 and lado1 != lado2:
            print("Triângulo isósceles")
        elif lado1 != lado2 and lado1 != lado3:
            print("Triângulo escaleno")

lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

triangulos(lado1, lado2, lado3)