from os import system, name 

palavra = ""
chances = 0
tentativa_palavra = ""
controleJogo = True

def carregarConfig():
    global palavra, chances
    arqConfig = open("config.txt", "r")
    for linha in arqConfig:
        linhaLimpa = linha.strip()
        linhaDados = linhaLimpa.split(';')
    palavra = linhaDados[0]
    chances = int(linhaDados[1])

def limpaTela():
    if name == 'nt':
        system('cls') # for windows 
    else: 
        system('clear') # for mac and linux(here, os.name is 'posix') 

def verifica_fim_jogo():
    global controleJogo, tentativa_palavra, chances,palavra 
    if chances == 0:
        print("Você perdeu!")
        controleJogo = False
        return controleJogo
    if tentativa_palavra == palavra:
        print("Você ganhou com %d chances sobrando!" % chances)
        controleJogo = False
        return controleJogo       

def jogar():
    letras_usadas = []
    tentativaCont = 0
    global palavra, chances, tentativa_palavra, controleJogo
    carregarConfig()
    while controleJogo:
        tentativa_palavra = ""
        limpaTela()
 
        print("Número de chances: %d - tentativas: %d" % (chances, tentativaCont)) # interpolação de string / coloquei o tentativaCont
        print(*letras_usadas) # imprime item por item do array
        print("\n")
        for x in palavra:
            tentativa_palavra += x if x in letras_usadas else "_"
        print(tentativa_palavra)
        print("\n")

        verifica_fim_jogo()

        if(controleJogo):
            chute = input("Digite uma letra:")
            while(True):
                if(ord(chute) >= 97 and ord(chute) <= 122):
                    break
                else:
                    chute = input("Caracter inválido digite novamente: ")

            while(True):
                if chute in letras_usadas:
                    chute = input("Letra já utilizada. Digite outra: ")
                else:
                    letras_usadas.append(chute)
                    tentativaCont += 1 # coloquei isso
                    break

            if not chute in palavra:
                chances -= 1
        else:
            break

def modificaConfig():
    arqConfig = open("config.txt", "w")
    palavra = input("Qual a nova palavra secreta? ")
    chances = input("Quantas chances? ")
    arqConfig.write(f"{palavra};{chances}")
    arqConfig.close()

def menu():
    escolhaJogador = 0
    while(escolhaJogador != 3):
        print("\nJOGO FORCA\n1. Jogar\n2. Modificar configurações\n3. Sair\n")
        escolhaJogador = int(input("Escolha a opção desejada: "))
        if(escolhaJogador == 1):
            jogar()
        elif(escolhaJogador == 2):
            modificaConfig()
        elif(escolhaJogador == 3):
            print("Até a próxima!")
            escolhaJogador = 3
        else:
            print("Opção inválida.")
 
if __name__ == "__main__":
    menu()