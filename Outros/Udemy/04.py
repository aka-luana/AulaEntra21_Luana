# -*- coding utf-8 -*-
# Listas
minhaLista  = ["abacaxi", "banana", "uva"]
minhaLista2 = [1, 2, 3, 4]
minhaLista3 = ["abacaxi", 2, 9.8, True]

#print(minhaLista, minhaLista2, minhaLista3)
#print(minhaLista[0])
"""for item in minhaLista2:
	print(item)"""

#tamanho = len(minhaLista)
#print(tamanho)

#minhaLista.append("limao") #add algo na lista
#print(minhaLista)

#if 4 in minhaLista2: #verificando se está ou não na lista
#	print(minhaLista2)

#del minhaLista[2:] #deleta algo na lista
#print(minhaLista)

minhaLista4 = [1,9,84,73,0,6,1000,39]
#minhaLista4.sort() #altera lista já existente
#lista = sorted(minhaLista4) #precisa de uma variavel pois ele "cria" uma nova lista
#minhaLista4.sort(reverse = True) #de tras para frente
minhaLista4.reverse() #inverte a lista sem ordena-la
print(minhaLista4)
#Ao fazer isso com listas de strings ele ordena/reordena alfabeticamente