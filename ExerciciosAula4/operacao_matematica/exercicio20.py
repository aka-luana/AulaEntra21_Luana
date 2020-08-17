#  Exercicio 20
# Usando a seguinte fórmula:
# 
# valor_receber = dinheiro_emprestado*(1+(taxa_juros/100))**tempo_emprestimo
# 
# Crie um programa que solicite ao usuário o valor do dinheiro emprestado, 
# a taxa de juros em porcentagem e o tempo do empréstimo.
# 
# Mostre na telas o valor do dinheiro emprestado, a taxa de juros em porcentagem, 
# tempo do empréstimo e o valor que deve ser devolvido no final do empréstimo.

valorEmprestado = float(input("Qual será o valor emprestado? \n"))
taxaJuros = float(input("Qual será a taxa de juros? \n"))
meses = float(input("Qual será o tempo do empréstimo? \n"))
print("Dinheiro emprestado: ", valorEmprestado)
print("Taxa de juros: ", taxaJuros)
print("Tempo do empréstimo: ", meses)
print("Valor a ser devolvido no final: ",valorEmprestado*(1+(taxaJuros/100))**meses)
