# -*- coding utf-8 -*-
# String concatenação
a = "Luana"
b = "Matos"
sNome = a + " " + b
print(sNome)
# String tamanho
iTamanhoNome = len(sNome)
print(iTamanhoNome)
# String Navegando Pelo Indice
print(a[2]) # a = Luana
# String Imprimindo um pedaço da string
print(a[0:2]) # Até o final fica a[0:]
# String objetos e métodos
cidade = "BLUMENAU"
print(cidade.lower())
estado = "santa catarina"
print(estado.upper())
#String Removendo espaço no início, no final e caracteres especiais
diaTexto = " Hoje é terça  \n"
print(diaTexto)
print(diaTexto.strip())
#Sting Convertendo String em Lista
frase = "O pelo do peito do pé do pedro é preto"
print(frase.split())
listaFrase = frase.split("p") # Colocando ("Algo") ele irá quebrar os elementos
# da lista com isso, caso o caracter inserido não tenha a lista terá apenas um grande elemento
print(listaFrase)
# String Buscando na String a posição de uma SubString
busca = frase.find("pé")
print(busca)
""" exemplo: escrever coisas só depois da palavra 'pé'"""
print(frase[busca:])
# Sting substituindo partes de ums String
frase2 = "O rato roeu a roupa do rei de Roma"
print(frase2)
print(frase2.replace("o rei", "a rainha"))