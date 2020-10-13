def cadastroEndereco():
    numeroId = int(input("Digite o seu ID: "))
    if(numeroId.isspace()):
        while(numeroId.isspace()):
            numeroId = int(input("ID em branco. Digite novamente: "))
    dictEndereco['numID'] = numeroId

    rua = input("Digite a sua rua: ")
    if(rua.isspace()):
        while(rua.isspace()):
            rua = int(input("Rua em branco. Digite novamente: "))
    dictEndereco['Rua'] = rua

    numero = int(input("Digite o número: "))
    if(numero.isspace()):
        while(numero.isspace()):
            numero = int(input("Número em branco. Digite novamente: "))
    dictEndereco['NumCasa'] = numero
    
    complemento = input("Digite o complemento: ")
    if(complemento.isspace()):
        while(complemento.isspace()):
            complemento = int(input("Complemento em branco. Digite novamente: "))
    dictEndereco['Complemento'] = complemento

    bairro = input("Digite o bairro: ")
    if(bairro.isspace()):
        while(bairro.isspace()):
            bairro = int(input("Bairro em branco. Digite novamente: "))
    dictEndereco['Bairro'] = bairro 

    cidade = input("Digite o cidade: ")
    if(cidade.isspace()):
        while(cidade.isspace()):
            cidade = int(input("Cidade em branco. Digite novamente: "))
    dictEndereco['Cidade'] = cidade
    
    estado = input("Digite o estado: ")
    if(estado.isspace()):
        while(estado.isspace()):
            estado = int(input("Estado em branco. Digite novamente: "))
    dictEndereco['Estado'] = estado
    
    listaEndereco.append(dictEndereco)
    print("Cadastrado com sucesso!")

listaEndereco = []
dictEndereco = {}