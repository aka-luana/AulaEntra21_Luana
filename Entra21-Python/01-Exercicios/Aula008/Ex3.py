#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve exibir todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
#        a função deve exibir uma pessoa cadastrada na função do ex1 filtrando por id

def menuLista():
        print("""
        1) Listar todas as pessoas
        2) Listar pessoas específica
        """)
        escolhaUser = int(input("Digite a opção desejada: "))

if(escolhaUser == 1):
        listarTodos()
elif(escolhaUser == 2):
        listarEspecifico()
else:
        print("Opcao inválida")

def listarTodos():
        for pessoas in listaPessoas:
                print(pessoas)



menuLista()
