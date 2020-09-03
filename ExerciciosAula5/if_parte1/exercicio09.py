# Exercicio 9
# Faça um programa que peça 3 números inteiros e mostre o os tês em ordem crescente.
# 
#
maior = int(input("Entre com um número: \n"))
medio = int(input("Entre com um número: \n"))
menor = int(input("Entre com um número: \n"))
aux   = 0

if (maior < medio):
    aux   = maior
    maior = medio
    medio = aux
if (maior < menor):
    aux   = maior
    maior = menor
    menor = aux
if (medio < menor):
    aux   = medio
    medio = menor
    menor = aux
if (medio > maior):
    aux   = medio
    medio = maior
    maior = aux
if (menor > maior):
    aux   = menor
    menor = maior
    maior = aux
if (menor > medio):
    aux   = menor
    menor = medio
    medio = aux

print (menor, " - ", medio, " - ", maior)
