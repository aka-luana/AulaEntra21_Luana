"""Execicios 04
Exercicio retirado do site <https://wiki.python.org.br/EstruturaDeDecisao>

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;

Triângulo Equilátero: três lados iguais;

Triângulo Isósceles: quaisquer dois lados iguais;

Triângulo Escaleno: três lados diferentes;
"""

lado1 = float(input("Lado 1: \n"))
lado2 = float(input("Lado 2: \n"))
lado3 = float(input("Lado 3: \n"))

if(((lado1 + lado2) > lado3) or ((lado2 + lado3) > lado1) or (lado3 + lado1) > lado2): 
    if((lado1 == lado2 and lado1 != lado3) or (lado3 == lado1 and lado3 != lado2) or (lado2 == lado3 and lado2 != lado1)):
        print ("Triângulo Isósceles")
    elif(lado1 == lado2 and lado1 == lado3):
        print ("Triângulo Equilátero")
    else:
        print ("Triângulo Escaleno")
else:
    print("Não é triângulo.")