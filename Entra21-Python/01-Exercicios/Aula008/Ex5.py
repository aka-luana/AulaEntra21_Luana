#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#                com seus respectivos endereços utilizando as funções do ex3 e ex4

from Ex1 import cadastroPessoa
from Ex2 import cadastroEndereco
from Ex3 import 

def main():
        print("""
1) Cadastrar Pessoa
2) Cadastrar endereço
3) Listar Pessoas cadastradas
4) Listar Endereços cadastrados
5) Sair
""")

main()
entradaUser = int(input())
while(entradaUser != 5):
    main()
    if (entradaUser == 1):
        cadastroPessoa()
    elif (entradaUser == 2):
        cadastroEndereco()
    elif (entradaUser == 3):
        listarPessoas()
    elif (entradaUser == 4):
        listarEnderecos()
    else:
        print ("Opção inválida.")