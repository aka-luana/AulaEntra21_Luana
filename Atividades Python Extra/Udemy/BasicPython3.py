# -*- coding utf-8 -*-
#Funções def - colocar na parte de cima
def soma(x, y):
	return x + y
print(soma(2, 3))

#Arquivos
""" Modos:
r: somente leitura
w/w+: escrita (caso o arquivo já exista, ele será apagado e um novo criado)
a/a+/r+: leitura e ecrita (abre arquivo e edita) """
""" Lendo arquivos:
read(): lê o arquivo inteiro
readline(): lê uma linha
readlines(): lê arquivo e o armazena em uma linha """
arq = open("arquivo.txt")
#linhas = arq.readlines() # - linha por linha
#print(linhas)
#for linha in linhas:
	#print(linha)

linhas2 = arq.read()
print(linhas2)

newFile = open("arquivo.txt", "w")
newFile.write("Esse eh o meu arquivo")
newFile.close()
arq2 = open("arquivo.txt")
linhas = arq2.readlines() # - linha por linha
print(linhas)
