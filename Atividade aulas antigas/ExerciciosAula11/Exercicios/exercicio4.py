"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair
-----

Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""

sair           = False
listaNomes     = []
listaIdades    = []
listaSexos     = []
listaTelefones = []

while sair == False:
    escolha = input("""A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados:
    C) Ver cadastro pelo nome:
    D) Apagar um cadastro pelo nome:
    S) Sair \n""")

    if escolha == 'A' or escolha == 'a':
        nomeBool     = False
        idadeBool    = False
        sexoBool     = False
        telefoneBool = False

        nome = input("Digite o nome: ")
        while nomeBool == False:
            if nome.isalpha():
                listaNomes.append(nome)
                nomeBool = True
            else:
                nome = input("Nome inválido. Digite nome: ")
            
        idade = input("Digite a idade: ")
        while idadeBool == False:
            if idade.isnumeric():
                listaIdades.append(idade)
                idadeBool = True
            else:
                idade = input("Idade inválida. Digite a idade: ")
        
        sexo = input("Digite o sexo: ")
        while sexoBool == False:
            if sexo.isalpha():
                listaSexos.append(sexo)
                sexoBool = True
            else:
                sexo = input("Sexo inválido. Digite o sexo:")
        
        telefone = input("Digite o telefone: ")
        while telefoneBool == False:
            if telefone.isnumeric():
                listaTelefones.append(telefone)
                telefoneBool = True
            else:
                telefone = input("Telefone inválido. Digite o telefone: ") 
        
    elif escolha == 'B' or escolha == 'b':
        if (len(listaNomes) == 0):
            print("Nenhum cadastro.")
        else:
            for i in range(len(listaNomes)):
                print(f"{i}. {listaNomes[i]}")

    elif escolha == 'C' or escolha == 'c':
        procuraNome = input("Ver dados do nome: ")

        if (procuraNome not in listaNomes or len(listaNomes) == 0):
            print("Nome não encontado.")
        else:
            for i in range(len(listaNomes)):
                if procuraNome in listaNomes:
                    idx = listaNomes.index(procuraNome)
                    print(f"Dados: \n Nome: {listaNomes[idx]} \n Idade: {listaIdades[idx]} \n Sexo: {listaSexos[idx]} \n Telefone: {listaTelefones[idx]}")
                    break

    elif escolha == 'D' or escolha == 'd':
        deletaNome = input("Deletar cadastro do nome: ")
        cont       = 0

        if (deletaNome not in listaNomes or len(listaNomes) == 0):
            print("Não encontrado.")
        else:
            for i in range(len(listaNomes)):
                if deletaNome in listaNomes:
                    idx = listaNomes.index(deletaNome)

                    listaNomes.remove(deletaNome)
                    listaIdades.pop(idx)
                    listaSexos.pop(idx)
                    listaTelefones.pop(idx)

                    print("Cadastro deletado.")
                    break

    elif escolha == 'S' or escolha == 's':
        print("Até a próxima :)")
        sair = True
    
    else:
        print("Opção inválida!")

