'''qntd = int(input())

qntd = qntd - 1

while(qntd >= 0):
    n1, n2 = input().split()

    n1 = int(n1)
    n2 = int(n2)   

    if (n1 > n2):
        for i in range(1, n2 + 1):
            if (n1 % i == 0):
                div = i
        print(f"{div}")
    else:
        for i in range(1, n1 + 1):
            if (n2 % i == 0):
                div = i
        print(f"{div}")
    
    qntd = qntd - 1'''

'''def achaMDC(num1, num2, menorNum):
    for i in range(menorNum):
        if(num1 % menorNum == 0 and num2 % menorNum == 0):
            return(menorNum)
        else:
            menorNum = menorNum - 1

qntd = int(input())

for i in range(qntd):
    n1, n2 = input().split()

    n1 = int(n1)
    n2 = int(n2)

    menor = min(n1, n2)
    resultado = achaMDC(n1, n2, menor)
    print(resultado)'''

'''def achaMDC(a, b):
    resto = None

    while resto != 0:
        resto = a % b
        a = b
        b = resto

    return a

trocas = int(input())
for i in range(trocas):
    n1, n2 = input().split()

    n1 = int(n1)
    n2 = int(n2)

    print(achaMDC(n1, n2))'''

# está dando time limit exceded