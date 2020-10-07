a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

lista = [a, b, c]
lista.sort(reverse = True)

a = lista[0]
b = lista[1]
c = lista[2]

if (a >= b + c):
    print("NAO FORMA TRIANGULO")
else:
    if(a ** 2 == b ** 2 + c ** 2):
        print("TRIANGULO RETANGULO")
    if(a ** 2 > b ** 2 + c ** 2):
        print("TRIANGULO OBTUSANGULO")
    if(a ** 2 < b ** 2 + c ** 2):
        print("TRIANGULO ACUTANGULO")
    if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
    if((a == b and b != c) or (a == c and b != c) or (b == c and c != a)):
        print("TRIANGULO ISOSCELES")
