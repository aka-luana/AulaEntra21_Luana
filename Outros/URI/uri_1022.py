casosTeste = int(input())

while(casosTeste > 0):
    numerador1, barra1, denominador1, operador, numerador2, barra2, denominador2 = input().split()

    numerador1, numerador2, denominador1, denominador2 = int(numerador1), int(numerador2), int(denominador1), int(denominador2)

    if (operador == '/'):
        n = (numerador1 * denominador2)
        d = (numerador2 * denominador1)
    elif (operador == '*'):
        n = (numerador1 * numerador2)
        d = (denominador1 * denominador2)
    elif (operador == '+'):
        n = (numerador1 * denominador2 + numerador2 * denominador1)
        d = (denominador1 * denominador2)
    elif (operador == '-'):
        n = (numerador1 * denominador2 - numerador2 * denominador1)
        d = (denominador1 * denominador2)

    if (n > d):
        maior = n
        menor = d
    elif (n <= d):
        maior = d
        menor = n

    for i in range(1, menor + 1):
        if (menor % i == 0 and maior % i == 0):
            div = i
        else:
            continue
    
    print(f"{n}/{d} = {int(n / div)}/{int(d / div)}")

    casosTeste = casosTeste - 1