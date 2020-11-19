frase = input("Digite a frase: ")
letra = input("Digite a letra que você deseja pesquisar: ")

print(f"A letra {letra} aparece {frase.count(letra)} vezes")

# Tem como pesquisar uma letra específica -> frase.count('u')
# Tem como pesquisar uma apenas um pedaço da frase -> frase.count('u', 0, 13)
# Uma outra função legal é o frase.find('qualquercoisa') -> retorna a posição de onde começa a palavra qualquercoisa,
# caso a frase não tenha a palavra 'qualquercoisa' o retorno será -1
# Pode-se utilizar o 'in' para verificar se existe uma palavra na frase, o retorno é um boleano -> 'Curso' in frase
