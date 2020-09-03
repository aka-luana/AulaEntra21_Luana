# Exercicio 17
# crie um programa que peça 4 notas de um aluno e calcule a média "(nota1+nota2+nota3+nota4)/4" e retorne:
# 
# Pra média igual a 10 apareça a mensagem "Aprovado com louvor"
# Pra média maior igual a 7 apareça a mensagem "Aprovado"
# Pra média menor que 7 apareça a mensagem "Reprovado"
# 
nota1 = float(input("Nota: \n"))
nota2 = float(input("Nota: \n"))
nota3 = float(input("Nota: \n"))
nota4 = float(input("Nota: \n"))

media = (nota1 + nota2 + nota3 + nota4)/4

if(media == 10):
    print("Aprovado com louvor")
elif(media >= 7 and media <= 9.99):
    print("Aprovado")
elif(media < 7):
    print("Reprovado")
else:
    print("Erro.")