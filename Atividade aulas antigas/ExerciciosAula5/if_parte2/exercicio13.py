# Exercicio 13
# 
# Crie um programa que peça o nome do cliente, idade, endereço, email e telefone.
# 
# Depois crie um menu interativo com as seguintes opções: Dados, Endereço, Contato.
# 
# Se o usuário selecionar "Dados" deve aparecer o nome do cliente e a idade
# 
# Se o usuário selecionar "Endereço" deve aparecer o nome do cliente e o endereço
# 
# Se o usuário selecionar "Contato" deve aparecer o nome do cliente, email e o telefone

nomeUser     = input("Qual o seu nome? \n")
idadeUser    = int(input("Qual a sua idade? \n"))
endereçoUser = input("Qual o seu endereço? \n")
emailUser    = input("Qual o seu email? \n")
telefoneUser = int(input("Qual seu telefone? \n"))

escolhaUser = int(input("""Opções:
1. Dados
2. Endereço
3. Contato \n"""))

if (escolhaUser == 1):
    print("Nome: ", nomeUser)
    print("Idade: ", idadeUser)
elif (escolhaUser == 2):
    print("Endereço: ", endereçoUser)
elif (escolhaUser == 3):
    print("Email: ", emailUser)
    print("Telefone: ", telefoneUser)
else:
    print("Opção inválida.")