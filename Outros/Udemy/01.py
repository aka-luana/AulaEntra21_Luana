# -*- coding: utf-8 -*-
print ("Hello World!")
print ("Olá mundo!") #foi com acento pq tem o utf-8

# comentario de linha unica
""" comentario
de varias
linhas """

print (2 ** 3) # ** é exponenciação
print (10 % 3) # modulo é %

sNome = "Meu nome é Luana"
print (sNome)

iNumero  = 2
iNumero2 = 3
print (iNumero == iNumero2) # a resposta mostrada sera False
iNumero3 = 1
iNumero4 = 1
print (iNumero3 == iNumero4) # a resposta mostrada sera True

if iNumero3 > iNumero:
	print("Algo está errado.")
if iNumero3 < iNumero:
	print("Agora sim.")

if iNumero3 > iNumero:
	print("Algo está errado. Com Else")
else:
	print("Agora sim. Com Else")

iUm   = 1
iDois = 2
iTres = 3
if   iDois < iUm:
	print("Dois maior que um")
elif iUm < iTres: # elif é o else if
	print("Três maior que um")
else:
	print("Nada está correto")

x = 1
while x <= 5:
	print(x)
	x += 1

#listas
iLista   = [1,2,3,4,5]
sLista  = ["ola", "mundo", "!"]
mixLista = [1, "kkkk", 0.4, True]
for i in sLista:
	print(i)

#range
for aux in range(5, 10, 2): #range de 5 até 10 imprimindo de 2 em 2
	print(aux)
print("----")
for e in range (5): # Não esquecer que começa do 0
	print(e)
print("----")
for o in range (5, 10):
	print(o)
print("----")