def cadastroPessoa():
    nome = input("Digite o nome: ")
    if(nome.isspace()):
        while(nome.isspace()):
            nome = input("Nome em branco. Digite novamente: ")

    sobrenome = input("Digite o sobrenome: ")
    if(sobrenome.isspace()):
        while(sobrenome.isspace()):
            sobrenome = input("Sobrenome em branco. Digite novamente: ")

    idade = input("Digite a idade: ")
    if(idade.isspace()):
        while(idade.isspace()):
            idade = input("Idade em branco. Digite novamente: ")
    idade = int(idade)

    if (idade >= 18):
        listaPessoa.append({'Nome':nome, 'Sobrenome':sobrenome, 'Idade':idade})
        print(f"Cadastrado com sucesso!")
    else:
        print("Não é possivel cadastrar menores de 18 anos")

def cadastroEndereco():
    if(len(listaPessoa) == 0):
        print("Primeiro cadastre uma pessoa.")
    else:
        numeroId = input("Digite o seu ID: ")
        if(numeroId.isspace()):
            while(numeroId.isspace()):
                numeroId = input("ID em branco. Digite novamente: ")

        numeroId = int(numeroId)
        if(numeroId > len(listaPessoa) or numeroId < 0):
            print("Id inválido")
        else:
            rua = input("Digite a sua rua: ")
            if(rua.isspace()):
                while(rua.isspace()):
                    rua = int(input("Rua em branco. Digite novamente: "))

            numero = input("Digite o número: ")
            if(numero.isspace()):
                while(numero.isspace()):
                    numero = input("Número em branco. Digite novamente: ")
            numero = int(numero)

            complemento = input("Digite o complemento: ")
            if(complemento.isspace()):
                while(complemento.isspace()):
                    complemento = int(input("Complemento em branco. Digite novamente: "))

            bairro = input("Digite o bairro: ")
            if(bairro.isspace()):
                while(bairro.isspace()):
                    bairro = int(input("Bairro em branco. Digite novamente: "))

            cidade = input("Digite o cidade: ")
            if(cidade.isspace()):
                while(cidade.isspace()):
                    cidade = int(input("Cidade em branco. Digite novamente: "))

            estado = input("Digite o estado: ")
            if(estado.isspace()):
                while(estado.isspace()):
                    estado = int(input("Estado em branco. Digite novamente: "))

            listaEndereco.append({'ID':numeroId, 'Rua':rua, 'Numero-Casa':numero, 'Complemento':complemento, 'Bairro':bairro, 'Cidade':cidade, 'Estado':estado})
            print("Cadastrado com sucesso!")

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

def listarEnderecos():
    if(len(listaEndereco) == 0):
        print("Primeiro cadastre um endereço.")
    else:
        print("-" * 45)
        print("""
        1) Listar Todos
        2) Listar específico
        """)
        print("-" * 45)
        escolhaUserListar = int(input("Qual opção você deseja? "))
        if (escolhaUserListar == 1):
            for pessoa in enumerate(listaEndereco):
                print (pessoa)

        elif (escolhaUserListar == 2):
            idPesquisa = int(input("Digite o id da pessoa desejada: "))
            if(idPesquisa > len(listaPessoa) or idPesquisa < 0):
                print("ID não encontrado.")
            else:
                print(listaEndereco[idPesquisa])
        else:
            print("Opção inválida.")

def main():
    print("-" * 45)
    print("""
        1) Cadastrar Pessoa
        2) Cadastrar endereço
        3) Listar Pessoas cadastradas
        4) Listar Endereços cadastrados
        5) Sair
    """)
    print("-" * 45)
    entradaUser = int(input("Digite a opção desejada: "))
    if (entradaUser == 1):
        cadastroPessoa()
    elif (entradaUser == 2):
        cadastroEndereco()
    elif (entradaUser == 3):
        listarPessoas()
    elif (entradaUser == 4):
        listarEnderecos()
    elif (entradaUser == 5):
        print("Até a próxima.")
        entradaUser = 5
    else:
        print("Opção inválida")
    while(entradaUser != 5):
        main()

listaEndereco = []
listaPessoa   = []

main()