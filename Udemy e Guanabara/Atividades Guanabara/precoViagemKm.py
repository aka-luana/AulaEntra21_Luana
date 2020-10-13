preco = 0
distancia = int(input("Qual a distância da viagem? "))

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print("O preço é {:.2f}".format(preco))