# 3) Estas 3 listas:
# 
# Estas listas são referente as vendas dos vendedores Armando, Paulo e Eduardo.
# 
# 3.1) Com base nelas e usando funções da lista mostradas em aula, mostre:
# A média de vendas de cada um;
# A venda total de cada vendedor;
# A quantidade de vendas de cada vendedor.
# 
# 3.2) Calcule o valor de comissão que o dono da loja deve pagar para seus funcionários seguindo a regra:
# Para total de vendas de 0.00 a 1000.00 Reais - 1%
# Para total de vendas de 1000.01 a 2500.00 Reais - 1.5%
# Para total de vendas de 2500.01 a 5000.00 Reais - 2%
# Para total de vendas a cima de 5000.01 Reais - 3%

# Link do meu git: https://github.com/aka-luana/AulaEntra21_Luana

vendas_armando = [100.00, 500.00, 258.50, 710.00, 50.50,750.00 ]
vendas_eduardo = [10.00, 1050.00, 859.75, 199.05, 500.50,750.00, 568.60, 950.00 ]
vendas_paulo   = [950.00, 89.90, 2500.00, 1750.00,500.00]

totalVendasArmando = sum(vendas_armando)
totalVendasEduardo = sum(vendas_eduardo)
totalVendasPaulo   = sum(vendas_paulo)

qtdVendasArmando = len(vendas_armando)
qtdVendasEduardo = len(vendas_eduardo)
qtdVendasPaulo   = len(vendas_paulo)

print(f"A média de vendas do Armando é {totalVendasArmando/qtdVendasArmando:.2f}")
print(f"A média de vendas do Eduardo é {totalVendasEduardo/qtdVendasEduardo:.2f}")
print(f"A média de vendas do Paulo é {totalVendasPaulo/qtdVendasPaulo:.2f} \n")

print(f"O valor total de vendas do Armando é R${totalVendasArmando}")
print(f"O valor total de vendas do Eduardo é R${totalVendasEduardo}")
print(f"O valor total de vendas do Paulo é R${totalVendasPaulo} \n")

print(f"A quantidade de vendas feito por Armando é {qtdVendasArmando}")
print(f"A quantidade de vendas feito por Eduardo é {qtdVendasEduardo}")
print(f"A quantidade de vendas feito por Paulo é {qtdVendasPaulo} \n")


# Armando
if (totalVendasArmando >= 0 and totalVendasArmando <= 1000):
    print(f"Deve ser pago o Armando R${totalVendasArmando*(1/100):.2f}")
elif (totalVendasArmando >= 1000.01 and totalVendasArmando <= 2500):
    print(f"Deve ser pago o Armando R${totalVendasArmando*(1.5/100):.2f}")
elif (totalVendasArmando >= 2500 and totalVendasArmando <= 5000):
    print(f"Deve ser pago para o Armando R${totalVendasArmando*(2/100):.2f}")
else:
    print(f"Deve ser pago para o Armando R${totalVendasArmando*(3/100):.2f} \n")

# Eduardo
if (totalVendasEduardo >= 0 and totalVendasEduardo <= 1000):
    print(f"Deve ser pago o Eduardo R${totalVendasEduardo*(1/100):.2f}")
elif (totalVendasEduardo >= 1000.01 and totalVendasEduardo <= 2500):
    print(f"Deve ser pago o Eduardo R${totalVendasEduardo*(1.5/100):.2f}")
elif (totalVendasEduardo >= 2500 and totalVendasEduardo <= 5000):
    print(f"Deve ser pago para o Eduardo R${totalVendasEduardo*(2/100):.2f}")
else:
    print(f"Deve ser pago para o Eduardo R${totalVendasEduardo*(3/100):.2f} \n")

#Paulo
if (totalVendasPaulo >= 0 and totalVendasPaulo <= 1000):
    print(f"Deve ser pago o Eduardo R${totalVendasPaulo*(1/100):.2f}")
elif (totalVendasPaulo >= 1000.01 and totalVendasPaulo <= 2500):
    print(f"Deve ser pago o Eduardo R${totalVendasPaulo*(1.5/100):.2f}")
elif (totalVendasPaulo >= 2500 and totalVendasPaulo <= 5000):
    print(f"Deve ser pago para o Eduardo R${totalVendasPaulo*(2/100):.2f}")
else:
    print(f"Deve ser pago para o Eduardo R${totalVendasPaulo*(3/100):.2f}")
