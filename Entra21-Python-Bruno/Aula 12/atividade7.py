#######################################################################################################

# Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

#     quantos espaços em branco existem na frase.
#     quantas vezes aparecem as vogais a, e, i, o, u. 


########################################################################################################

frase = input("Digite sua frase: ")
frase = frase.lower()
contEspaco, contA, contE, contI, contO, contU = frase.count(" "), frase.count("a"), frase.count("e"), frase.count("i"), frase.count("o"), frase.count("u")

print(f"A frase possui {contEspaco} espaços,"
      f" {contA} letras A(a),"
      f" {contE} letras E(e),"
      f" {contI} letras I(i),"
      f" {contO} letras O(o),"
      f" {contU} letras U(u).")
    