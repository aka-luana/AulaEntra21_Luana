#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

def media():
    n1, n2, n3 = input("Digite os números: ").split()
    n1 = float(n1)
    n2 = float(n2)
    n3 = float(n3)
    med = (n1 + n2 + n3) / 3
    print(f"A média entre o número {n1}, {n2} e {n3} é {med:.2f}")

media()