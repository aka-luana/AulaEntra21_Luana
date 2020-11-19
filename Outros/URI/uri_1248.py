casosTeste = int(input())

while(casosTeste > 0):   
    dieta  = input()
    cafe   = input()
    almoco = input()

    lanche = cafe + almoco #fica tudo que foi comido em um só lugar

    for i in range(len(lanche)):
        if lanche[i] not in dieta:
            dieta = "CHEATER"
            break
        else:
            dieta = dieta.replace(lanche[i], '')

    if dieta != "CHEATER":
        dieta = ''.join(sorted(dieta)) #join serve para juntar a string
    
    print(dieta)

    casosTeste = casosTeste - 1