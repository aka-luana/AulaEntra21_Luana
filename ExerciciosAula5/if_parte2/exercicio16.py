# Exercicio 16
# 
# Crie um programa para uma promoção de um posto de combustivel.
# 
# O programa deve pedir ao usuário quantos litros ele quer abastecer e qual combustivel: álcool, diessel ou gasolina
# 
# A promoção é a seguinte:
#  - Para gasolina: Até 20 litros 0% de desconto e acima de 20 litros 10% de desconto
#  - Para diessel: Até 10 litro 1.5% de desconto e acima de 10 litros 5% de desconto
#  - para álcool: Até 10 litros 5% de desconto e acima de 10 litros 10% de desconto.
#  
# Mostre o combustivel que ele selecionou, o total abastecido e a porcentagem de desconto a ser aplicada.
# 
# Não precisa calcular o valor do combustivel!
# 
escolhaGasolina = int(input("""Combustível:
1. Para gasolina
2. Para diesel
3. Para álcool \n"""))
litros = int(input("Quantos litros? \n"))

if(escolhaGasolina == 1):
    if(litros <= 20):
        print("Combustivel: gasolina \n Total abastecido: ", litros, "\n Desconto: 0%")
    else:
        print("Combustivel: gasolina \n Total abastecido: ", litros, "\n Desconto: 10%")
elif(escolhaGasolina == 2):
    if(litros <= 10):
        print("Combustivel: diesel \n Total abastecido: ", litros, "\n Desconto: 0%")
    else:
        print("Combustivel: diesel \n Total abastecido: ", litros, "\n Desconto: 5%")
elif(escolhaGasolina == 3):
    if(litros <= 10):
        print("Combustivel: álcool \n Total abastecido: ", litros, "\n Desconto: 0%")
    else:
        print("Combustivel: álcool \n Total abastecido: ", litros, "\n Desconto: 10%")
else:
    print("Cobustível inválido.")