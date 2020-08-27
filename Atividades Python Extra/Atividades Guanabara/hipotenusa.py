from math import sqrt, pow

catetoOposto    = float(input("Digite o cateto oposto: "))
catetoAdjacente = float(input("Digite o cateto adjacente: "))

hipotenusa = pow(catetoOposto, 2) + pow(catetoAdjacente, 2)

print(f"A hipotenusa é {sqrt(hipotenusa):.2f}")
