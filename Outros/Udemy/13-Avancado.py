#funcao zip
lista1 = [1, 2, 3, 4, 5]
lista2 = ["Pão", "Ovo", "Leite", "Sabonete", "Amaciante"] #mesma quantidade de itens da lista1
lista3 = ["R$4,00", "R$10,00", "R$3,00", "R$1,00", "R$12,00"]

# o zip serve para concatenar (juntar) duas ou mais listas em uma só

for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)