
#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

def divisao(n1, n2):
    if n1 == 0 or n2 == 0:
        return(print("Não é possivel calcular"))
    else:
        resultado = n1 / n2
        return(print(f"A divisão entre o número {num1} e o {num2} é {resultado:.2f}"))

num1, num2 = input("Digite os números: ").split()
num1 = float(num1)
num2 = float(num2)
divisao(num1, num2)