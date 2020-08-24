valor = float(input("Qual o valor do produto? R$"))

print("O produto que custava {:.2f}, na promoção com desconto de 5% vai custar R${:.2f}".format(valor, valor-(valor*(5/100))))