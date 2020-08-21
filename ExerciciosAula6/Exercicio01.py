"""Execicios 01

Escreva um programa que calcule a porcentagem de comissão de vendedores com as seguintes condições

Venda Total
de R$ 0.00 a R$ 30000.00 - 0%
de R$ 30000.01 a R$ 50000.00 - 1.5%
de R$ 50000.01 a R$ 100000.00 - 2.5%
Acima de R$ 100000.00 - 3.5%
"""

qtdVendida = float(input("Quanto você vendeu? \n"))
if (qtdVendida <= 0.00):
    print("Não houve venda")
elif(qtdVendida <= 30000.00):
    print("Não teve comissão")
elif(qtdVendida >= 30000.01 and qtdVendida <= 50000.00):
    print("A comissão de 1.5%", " ficou: ", qtdVendida*(1.5/100))
elif(qtdVendida >= 50000.01 and qtdVendida <= 100000.00):
    print("A comissão de 2.5%", " ficou: ", qtdVendida*(2.5/100))
else:
    print("A comissão de 3.5%", " ficou: ", qtdVendida*(2.5/100)) 