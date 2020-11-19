produto1 = input().split(" ")
produto2 = input().split(" ")

codigo1, quantidade1, preco1 = produto1
codigo2, quantidade2, preco2 = produto2

valorTotal = (int(quantidade1) * float(preco1)) + (int(quantidade2) * float(preco2))
print("VALOR A PAGAR: R$ %0.2f" %valorTotal)
