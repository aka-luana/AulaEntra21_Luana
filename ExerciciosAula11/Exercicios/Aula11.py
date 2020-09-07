
"""
----

Laço de Repetição WHILE

----

O While é um laço de repetição que possui um operação condicional como controlador.

Se a operação condicional resultar em True (Verdadeiro) o while irá fazer o loop. 

Caso a operação condicional resultar em False ele não executará o código indentado.


Ele é muito útil para quando se quer repetir um código infinitamente ou não se sabe quantas vezes ele deve repetir.
"""

# Exemplo:

# Crie um programa que peça 2 números inteiros.
# Mostre um menu para o usuário e peça para ele escolher se quer soma ou subtração ou sair

# Se ele escolher soma, some os números e mostre o resultado.
# Se ele escolher subtração, subtraia os números e mostre o resultado.
# Se ele escolher sair, mostre uma mensagem de despidida e termine o programa.
# Para qualquer outra opção apareça a mensagem "Opção Invalida"

# Criando a variável opcao e atribuindo um valor
opcao = '' # Como vamos usar esta variável no while é importante cria-la
           # antecipadamente e colocar um valor que não interfira no nosso
           # while

while opcao != '3': #  opcao != '3' tem que ser True para funcionar!  

    # Pedindo 2 números:
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    # Criando o menu de escolha:
    opcao = input('''
    Programa Soma/Subtração

    1) Soma:
    2) Subtração:
    3) Sair:

    Digite a opção desejada: ''')

    # Criando o filtro
    print('\n')
    if opcao == '1':
        soma = numero1 + numero2
        print(f"O resultado da soma é {soma}\n")
    elif opcao == '2':
        sub = numero1 - numero2
        print(f"O resultado da subtração é {sub}\n")
    elif opcao == '3':
        print(f"Obrigado pela escolha!\nBye!\n")
    else:
        print('Opção inválida\n')

# Note que o nosso código ficou mais dinâmico e o loop ajuda muito

# Exemplo2:

# Crie um programa que peça 2 números e divida um pelo outro.
# Crie um filtro que verifique se o segundo número é igual a zero. 
# se for igual a zero deve mostrar a mensagem 
# "Número inválido! Digite novamente" e peça que o usuário digite o segundo 
# valor novamente. repita isso até que o usuário digite um valor diferente de zero.
# Depois mostre o resultado.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

not_div_zero = "True" #Criando uma variável booleana para fazermos o loop

while not_div_zero:
    if numero2 == 0:
        print("Número inválido! Digite novamente")
        numero2 = int(input("Digite o segundo número: "))
    else:
        not_div_zero = False # Mudando o valor para False garantimos o fim do loop
        div = numero1 / numero2
        print(f'O resultado da divisão é {div}')

# Note que aqui nós forçamos o usuário a digitar o valor corretamente! 
# O programa só seguiu em frente quando o segundo número estava correto!




"""
----

Comandos Break e Continue

----

Este comandos servem para controlar o fluxo do loop.

continue: Para o fluxo atual e volta para o inicio do loop

break: Termina o loop e finaliza o laço de repetição.

Estes comando funcionam tanto no while quanto no for
"""

# Exemplo Continue:

# Faça um programa que mostre todos os números de 1 a 40. 
# Some os todos os números menos os números de 20 a 30.
# Mostre o resultado.

lista = [ ]
cont = 0
while cont < 40:
    cont = cont + 1
    if cont >= 20 and cont <= 30:
        continue # Se o continue for executado o código volta para o inicio
    
    print(cont)
    lista.append(cont)

print(sum(lista))
print(lista)

# Exemplo Break:

# Crie um programa que mostre "Bom dia" e pergunte se deseja continuar. 

while True: # Este é o nosso carro descendo um morro a toda velocidade
    print('Bom dia')
    continuar = input("Deseja continuar? (S para sim ou N para não): ")
    if continuar == 'N' or continuar == 'n':
        break # Este é o nosso freio!






