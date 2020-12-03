from itertools import permutations

quadradoMagico = list(permutations([1,2,3,4,5,6,7,8,9]))
qtd            = len(quadradoMagico)
cont           = 0

def geradorQuadrado():
    horizontal, vertical, diagonal = False, False, False
    for numero in quadradoMagico:
        somaHorizontal1 = numero[0] + numero[1] + numero[2]
        somaHorizontal2 = numero[3] + numero[4] + numero[5]
        somaHorizontal3 = numero[6] + numero[7] + numero[8]

        if (somaHorizontal1 == 15) and (somaHorizontal2 == 15) and (somaHorizontal3 == 15):
            horizontal = True

        somaVertical1 = numero[0] + numero[3] + numero[6]
        somaVertical2 = numero[1] + numero[4] + numero[7]
        somaVertical3 = numero[2] + numero[5] + numero[8]

        if (somaVertical1 == 15) and (somaVertical2 == 15) and (somaVertical3 == 15):
            vertical  = True
        
        somaDiagonal1 = numero[0] + numero[4] + numero[8]
        somaDiagonal2 = numero[2] + numero[4] + numero[6]

        if (somaDiagonal1 == 15) and (somaDiagonal2 == 15):
            diagonal  = True
        
        if horizontal and vertical and diagonal: 
            global cont
            cont += 1
            print(f"""
              MAGIC SQUARE {cont}
                | {numero[0]} {numero[1]} {numero[2]} |
                | {numero[3]} {numero[4]} {numero[5]} |
                | {numero[6]} {numero[7]} {numero[8]} |
            """)
             
        horizontal, vertical, diagonal = False, False, False
                  
if __name__ == "__main__":
    # Colocar menuzinho com com algumas opções para o jogador
    # Fazer o clear e sleep pra ficar legal
    geradorQuadrado()