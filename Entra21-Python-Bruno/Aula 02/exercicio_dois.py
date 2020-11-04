# Calcule o valor total dos itens e aplique descontos:

# se o valor for superior a 50, 2% de desconto
# se o valor for superior a 100, 5% de desconto
# se o valor for superior a 200, 10% de desconto

# descubra qual o item mais caro da lista

# ordene os itens da lista por ordem alfabética

total = 0
carrinhoCompra = {3:"Pão", 100:"Vinho", 6:"Queijo", 15: "Arroz", 5:"Suco", 8:"Chocolate"}

for valor in carrinhoCompra.keys():
    total = valor + total

if total >= 50 and total < 100:
    valor = (2 / 100) * 50
elif total >= 100 and total < 200:
    valor = (5 / 100) * 100
elif total >= 200:
    valor = (10 / 100) * 200

maior = sorted(carrinhoCompra, reverse=True)

print(f"Cupom fiscal: {sorted(carrinhoCompra.values())}")
print(f"Total da compra sem desconto: R${valor}")
print(f"Total da compra com desconto: R${(total - valor)}")
print(f"O item mais caro foi o {carrinhoCompra[maior[0]]} no valor de R$ {maior[0]}")
