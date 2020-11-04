# arq com a palavra secreta e o numero de vidas (chutes) do jogador
# aplicar em funcao e colocar nas variaveis palavra e chances

from os import system, name 

def palavraSecreta():
    arqPalavra = open("config.txt", "r")
    palavra = arqPalavra.readline()
    arqPalavra.close()
    return palavra.strip()

def vidasJogador():
    chances = None
    arqVida = open("config.txt", "r")
    for linha in arqVida: # sobrescrve
        chances = linha
    arqVida.close()
    return int(chances)
 
def jogar():
    palavra = palavraSecreta()
    chances = vidasJogador()
    letras_usadas = []
    while True:
        tentativa_palavra = ""
 
        # for windows 
        if name == 'nt': 
            system('cls') 
        # for mac and linux(here, os.name is 'posix') 
        else: 
            system('clear')       
 
        print("Número de chances: %d - tentativas:" % chances) # interpolação de string
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra + "\n\n")
 
        chute = input("Digite uma letra:")
        letras_usadas.append(chute)
 
        if not chute in palavra:
            chances -= 1
 
        if chances == 0:
            print("Você perdeu!")
            break
        if tentativa_palavra == palavra:
            print("Você ganhou com apenas %d!" % 5 - chances)
            break
 
 
if __name__ == "__main__":
    jogar()
