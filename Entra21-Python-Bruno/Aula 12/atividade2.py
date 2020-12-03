######################################################################################################

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#     Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#     comprar apenas latas de 18 litros;
#     comprar apenas galões de 3,6 litros;
#     misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# 

#######################################################################################################

from time import sleep
from os import system, name

def apenas18(litros):
    cont = 0
    cont = litros // 18
    if litros % 18 != 0:
        cont += 1
    return cont 

def apenas36(litros):
    cont = 0
    cont = litros // 3.6
    if litros % 3.6 != 0:
        cont += 1
    return cont

def misturado(litros):
    cont18 = 0
    cont36 = 0
    lista = []
    while litros > 0:
        if litros >= 18:
            litros -= 18
            cont18 += 1
        elif litros < 18:
            litros -= 3.6
            cont36 += 1
    lista.append(cont18)
    lista.append(cont36)
    return(lista)

def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

if __name__ == "__main__":
    while True:
        try:
            print('='*15 + ' LOJA TINTAS ' + '='*15)
            sleep(0.8)
            print("Carregando opções...")
            sleep(0.8)
            escolha = int(input("""
1. Resultado apenas com latas 18 litros
2. Resultado apenas com latas 3,6 litros
3. Resultado misturado
"""))
            metros = float(input("Tamanho em m² da parede a ser pintada: "))
            print("Calculando...")
            sleep(1.5)
            litrosNecessarios = metros / 6 * 1.1 # Regra de 3 + 10%

            limpaTela()
            if escolha == 1:
                print(f"Para pintar {metros:.2f} m² será necessário {apenas18(litrosNecessarios)} galão(es) de 18 litros")
                break
            elif escolha == 2:
                print(f"Para pintar {metros:.2f} m² será necessário {apenas36(litrosNecessarios)} galão(es) de 3,6 litros")
                break
            elif escolha == 3:
                print(f"Para pintar {metros:.2f} m² será necessário {misturado(litrosNecessarios)[0]} galão(es) de 18 litros e {misturado(litrosNecessarios)[1]} lata(s) de 3,6 litros")
                break
        except:
            print("Valor inválido.")