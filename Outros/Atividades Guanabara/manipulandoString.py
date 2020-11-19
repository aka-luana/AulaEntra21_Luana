frase = input("Digite a frase: ")

print(frase.lower()) # Minusculo
print(frase.upper()) # Maiusculo
print(frase.capitalize()) # Apenas a primera letra em maiusculo
print(frase.title()) # Todas as primeiras letras em maiusculo
print(frase.strip()) # Remove espaços no início e final da frase -> Adaptando o indice || Existe 
# também o frase.rstrip() que remove apenas os espaços do lado direito || Segundo a lógica temos
# o frase.lstrip(), que retira espaços apenas do lado direito
frase = frase.split()
print(frase)
print(''.join(frase))


