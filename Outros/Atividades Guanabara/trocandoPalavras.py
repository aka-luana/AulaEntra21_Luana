frase = input("Digite a frase: ")
palavraAntiga = input("Digite a palavra que você quer retirar: ")
palavraNova = input("Digite a palavra que você quer colocar no lugar: ")

frase = frase.replace(palavraAntiga, palavraNova)

print(frase)