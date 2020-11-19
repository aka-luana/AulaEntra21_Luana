
def cadastroPessoa():
    nome = input("Digite seu nome: ")
    if(nome.isspace()):
        while(nome.isspace()):
            nome = input("Nome em branco. Digite novamente: ")

    sobrenome = input("Digite seu sobrenome: ")
    if(sobrenome.isspace()):
        while(sobrenome.isspace()):
            sobrenome = input("Sobrenome em branco. Digite novamente: ")

    idade = input("Digite sua idade: ")
    if(idade.isspace()):
        while(idade.isspace()):
            idade = input("Idade em branco. Digite novamente: ")

    idUser = id(sobrenome)
    idUser = int(idUser)
    idade =  int(idade)

    if idade >= 18:
        listaPessoa.append((nome, sobrenome, idade, idUser))
        print(f"Cadastrado com sucesso! Seu número de ID é {idUser}")
    else:
        print("Sua idade não é permitida. Volte daqui a alguns anos.")

def cadastroEndereco():
    idEndereco = input("Digite o seu ID: ")
    if(idEndereco.isspace()):
        while(idEndereco.isspace()):
            idEndereco = input("ID em branco. Digite novamente: ")
    idEndereco = int(idEndereco)

    rua = input("Digite a sua rua: ")
    if(rua.isspace()):
        while(rua.isspace()):
            rua = input("Rua em branco. Digite novamente: ")

    numCasa = input("Digite o número: ")
    if(numCasa.isspace()):
        while(numCasa.isspace()):
            numCasa = input("Número em branco. Digite novamente: ")
    numCasa = int(numCasa)

    complemento = input("Digite o complemento: ")
    if(complemento.isspace()):
        while(complemento.isspace()):
            complemento = input("Complemento em branco. Digite novamente: ")

    bairro = input("Digite o bairro: ")
    if(bairro.isspace()):
        while(bairro.isspace()):
            bairro = input("Bairro em branco. Digite novamente: ")

    cidade = input("Digite o cidade: ")
    if(cidade.isspace()):
        while(cidade.isspace()):
            cidade = input("Cidade em branco. Digite novamente: ")

    estado = input("Digite o estado: ")
    if(estado.isspace()):
        while(estado.isspace()):
            estado = input("Estado em branco. Digite novamente: ")
    
    listaEndereco.append((idEndereco, rua, numCasa, complemento, bairro, cidade, estado))
    print("Endereço cadastrado com sucesso!")

def listarPessoas():
    print("""
    1) Listar Todos
    2) Listar específico
    """)
    escolhaUserListar = int(input("Qual opção você deseja? "))
    if (escolhaUserListar == 1):
        for mostrar in listaPessoa:
            nome, sobrenome, idade, idUser = mostrar
            print(f"Nome: {nome} - Sobrenome: {sobrenome} - Idade: {idade} - ID: {idUser}")

    elif (escolhaUserListar == 2):
        idPesquisa = int(input("Digite o id da pessoa desejada: "))
        for mostrar in listaPessoa:
            if idPesquisa in mostrar:
                try:
                    print(f"Nome: {mostrar[1]} - Sobrenome: {mostrar[2]} - Idade: {mostrar[3]} - ID: {mostrar[4]}")
                except:
                    print("ID não encontrado.")

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
    else:
        print("Opção inválida")
    while(entradaUser != 5):
        main()

listaPessoa = []
listaEndereco = []

main()