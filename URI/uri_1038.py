codigo, quantidade = input().split(" ")

codigo     = int(codigo)
quantidade = int(quantidade)

listPrecos = [4.00, 4.50, 5.0, 2.0, 1.50]
total       = listPrecos[codigo - 1] * quantidade

print(f"Total: R$ {total:.2f}")