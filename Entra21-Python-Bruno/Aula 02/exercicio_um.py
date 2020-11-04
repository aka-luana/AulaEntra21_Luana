# Crie uma lista com todas as letras do alfabeto

# Remova as vogais dessa lista e crie uma tupla com elas

# Crie uma coleção com as letras do seu nome (utilizando a lista e a tupla, sem remover itens).
# depois, adicione sua idade e o nome do seu livro 

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
listaVogais = []

for vogal in alfabeto:
    if (vogal == "a" or vogal == "e" or vogal == "i" or vogal == "o" or vogal == "u"):
        letra = vogal
        alfabeto.remove(vogal)
        listaVogais.append(letra)

tuplaVogais = (listaVogais)
print(f"Vogais retiradas do alfabeto: {tuplaVogais}")
print(f"Restante do alfabeto: {alfabeto}")

nome = "luana"
colecaoNome = []

for letra in nome:
    for consoante in alfabeto:
        if letra == consoante:
            colecaoNome.append(consoante)
    for vogal in tuplaVogais:
        if letra == vogal:
            colecaoNome.append(vogal)

idade = "19 anos"
livro = "harry potter e o prisioneiro de azkaban"
colecaoNome.append(idade)
colecaoNome.append(livro)

dictColecao = {}
dictColecao[0] = colecaoNome

print("Coleção Luana: ")
for i in dictColecao.values():
	print(i)