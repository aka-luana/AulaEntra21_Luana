#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

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
        listaPessoas.append(nome)
        listaPessoas.append(sobrenome)
        listaPessoas.append(idade)
        #idRecebido = idUser()
        idUsuario = idUsuario + 1
        listaPessoas.append(idUsuario)
        print(f"Cadastrado com sucesso! Seu ID é {idUsuario}")
    else:
        print("Não é possivel cadastrar menores de 18 anos")

def cadastroEndereco(numeroId, rua, numero, complemento, bairro, cidade, estado):
    numeroId = int(input("Digite o seu ID: "))
    if(numeroId.isspace()):
        while(numeroId.isspace()):
            numeroId = int(input("ID em branco. Digite novamente: "))
    rua = input("Digite a sua rua: ")
    if(rua.isspace()):
        while(rua.isspace()):
            rua = int(input("Rua em branco. Digite novamente: "))
    numero = int(input("Digite o número: "))
    if(numero.isspace()):
        while(numero.isspace()):
            numero = int(input("Número em branco. Digite novamente: "))
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
    
    listaEndereco.append(numeroId)
    listaEndereco.append(rua)
    listaEndereco.append(numero)
    listaEndereco.append(complemento)
    listaEndereco.append(bairro)
    listaEndereco.append(cidade)
    listaEndereco.append(estado)
    print("Cadastrado com sucesso!")

def main():
        print("""
1) Cadastrar Pessoa
2) Cadastrar endereço
3) Listar Pessoas cadastradas
4) Listar Endereços cadastrados
5) Sair
""")

listaPessoas  = []
listaEndereco = []
idUsuario = 0
main()
entradaUser = int(input("Digite a opção desejada: "))
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