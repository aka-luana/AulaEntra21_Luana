import parte1
from parte1 import listaPessoa

listaEndereco = []

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