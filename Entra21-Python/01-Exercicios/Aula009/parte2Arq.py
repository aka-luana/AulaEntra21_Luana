import parte1Arq

def cadastroEndereco():
    numeroId = input("Digite o seu ID: ")
    if(numeroId.isspace()):
        while(numeroId.isspace()):
            numeroId = input("ID em branco. Digite novamente: ")
    numeroId = int(numeroId)           

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

    dictEndereco = {'ID':numeroId, 'Rua':rua, 'Numero-Casa':numero, 'Complemento':complemento, 'Bairro':bairro, 'Cidade':cidade, 'Estado':estado}
    arquivoEnderecos = open('enderecos.txt', 'a')
    arquivoEnderecos.write(f"{dictEndereco['ID']};{dictEndereco['Rua']};{dictEndereco['Numero-Casa']};{dictEndereco['Complemento']};{dictEndereco['Bairro']};{dictEndereco['Cidade']};{dictEndereco['Estado']} \n")
    arquivoEnderecos.close()
    print("Cadastrado com sucesso!")