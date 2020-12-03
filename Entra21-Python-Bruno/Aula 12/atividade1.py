# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o 
# Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#     salário bruto.
#     quanto pagou ao INSS.
#     quanto pagou ao sindicato.
#     o salário líquido.
#     calcule os descontos e o salário líquido, conforme a tabela abaixo: 
#     + Salário Bruto : R$
#     - IR (11%) : R$
#     - INSS (8%) : R$
#     - Sindicato ( 5%) : R$
#     = Salário Liquido : R$

######################################################################################################

def salarioCalculos(salarioHora, horaTrabalhada):
  bruto        = salarioHora * horaTrabalhada
  inss         = bruto * 8 / 100
  sindicato    = bruto * 5 / 100
  importoRenda = bruto * 11 / 100
  print(f"""
        |   SALARIO BRUTO: R$ {bruto:.2f} |
        |      VALOR INSS: R$ {inss:.2f}  |
        | VALOR SINDICATO: R$ {sindicato:.2f}  |
        | SALARIO LÍQUIDO: R$ {bruto - inss - sindicato - importoRenda:.2f} |
         """)

if __name__ == "__main__":
  try:
    print('='*13 + ' CONSULTA SALARIAL ' + '='*13)
    salarioHora = float(input("Digite quando você ganha por hora trabalhada: "))
    horaTrabalhada = int(input("Digite quantas horas você trabalha no mês: "))
    print('='*45)
    salarioCalculos(salarioHora, horaTrabalhada)
  except:
    print("Valor inválido.")
