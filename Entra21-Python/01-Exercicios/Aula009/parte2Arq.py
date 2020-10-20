import parte1Arq

def cadastroEndereco():
    continuaCadastro = False
    existeEndereco = True
    
    numeroId = input("Digite o seu ID: ")
    if(numeroId.isspace() or numeroId == ''):
        while(numeroId.isspace() or numeroId == ''):
            numeroId = input("ID em branco. Digite novamente: ")
    numeroId = int(numeroId)

    arquivoPessoas = open('pessoas.txt', 'r')
    for procuraId in arquivoPessoas: # Verifica se existe o ID informado no cadastros das pessoas
        linhaLimpa = procuraId.strip()
        listaDados = linhaLimpa.split(';')
        if (str(numeroId) == listaDados[3]):
              continuaCadastro = True
    arquivoPessoas.close()

    arquivoEnderecos = open('enderecos.txt', 'r')
    for procuraId in arquivoEnderecos: # Verifica se já existe o cadastro do endereco com o ID informado
        linhaLimpa = procuraId.strip()
        listaDados = linhaLimpa.split(';')
        if (str(numeroId) != listaDados[0]):
              existeEndereco = False
    arquivoEnderecos.close()

    if (continuaCadastro and existeEndereco == False):
        rua = input("Digite a sua rua: ")
        if(rua.isspace() or rua == ''):
            while(rua.isspace() or rua == ''):
                rua = int(input("Rua em branco. Digite novamente: "))

        numero = input("Digite o número: ")
        if(numero.isspace() or numero == ''):
            while(numero.isspace() or numero == ''):
                numero = input("Número em branco. Digite novamente: ")
        numero = int(numero)

        complemento = input("Digite o complemento: ")
        if(complemento.isspace() or complemento == ''):
            while(complemento.isspace() or complemento == ''):
                complemento = int(input("Complemento em branco. Digite novamente: "))

        bairro = input("Digite o bairro: ")
        if(bairro.isspace() or bairro == ''):
            while(bairro.isspace() or bairro == ''):
                bairro = int(input("Bairro em branco. Digite novamente: "))

        cidade = input("Digite o cidade: ")
        if(cidade.isspace() or cidade == ''):
            while(cidade.isspace() or cidade == ''):
                cidade = int(input("Cidade em branco. Digite novamente: "))

        estado = input("Digite o estado: ")
        if(estado.isspace() or estado == ''):
            while(estado.isspace() or estado == ''):
                estado = int(input("Estado em branco. Digite novamente: "))

        dictEndereco = {'ID':numeroId, 'Rua':rua, 'Numero-Casa':numero, 'Complemento':complemento, 'Bairro':bairro, 'Cidade':cidade, 'Estado':estado}
        arquivoEnderecos = open('enderecos.txt', 'a')
        arquivoEnderecos.write(f"{dictEndereco['ID']};{dictEndereco['Rua']};{dictEndereco['Numero-Casa']};{dictEndereco['Complemento']};{dictEndereco['Bairro']};{dictEndereco['Cidade']};{dictEndereco['Estado']} \n")
        arquivoEnderecos.close()
        print("Cadastrado com sucesso!")
    elif (continuaCadastro and existeEndereco):
        print("Endereço já cadastrado com o ID informado.")
    else:
        print("ID inválido")