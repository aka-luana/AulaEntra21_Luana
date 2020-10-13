#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada 

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

listaEndereco = []