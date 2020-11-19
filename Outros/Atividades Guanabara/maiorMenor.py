aux = 0
n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
n3 = int(input("Numero 3: "))

if (n1 > n2):
    aux = n1
    n1  = n2
    n2  = aux
if (n1 > n3):
    aux = n1
    n1  = n3
    n3  = aux
if (n2 < n1):
    aux = n2
    n2  = n1
    n1  = aux
if (n2 > n3):
    aux = n2
    n2  = n3
    n3  = aux
if (n3 < n1):
    aux = n3
    n3  = n1
    n1  = aux
if (n3 < n2):
    aux = n3
    n3  = n2
    n2  = aux

print(n1, " - ", n2, " - ", n3)