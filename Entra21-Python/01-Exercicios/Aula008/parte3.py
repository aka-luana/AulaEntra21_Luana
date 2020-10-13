import parte1
#import parte2
from parte1 import listaPessoa

def listarPessoas():
    if (len(listaPessoa) == 0):
        print("Nenhuma pessoa cadastrada.")
    else:
        print("-" * 45)
        print("""
        1) Listar Todos
        2) Listar específico
        """)
        print("-" * 45)
        escolhaUserListar = int(input("Qual opção você deseja? "))
        if (escolhaUserListar == 1):
            for pessoa in enumerate(listaPessoa):
                print ("ID: ", pessoa)

        elif (escolhaUserListar == 2):
            idPesquisa = int(input("Digite o id da pessoa desejada: "))
            if(idPesquisa > len(listaPessoa) or idPesquisa < 0):
                print("ID não encontrado.")
            else:
                print(listaPessoa[idPesquisa])
        else:
            print("Opção inválida.")