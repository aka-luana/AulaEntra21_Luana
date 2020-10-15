import parte1Arq
import parte2Arq
#from parte2Arq import listaEndereco
#from parte1Arq import listaPessoa

def listarEnderecos():
    #arquivoEnderecos = open('enderecos.txt', 'a')

    #if(len(arquivoEnderecos) == 0):
    #    print("Primeiro cadastre um endereço.")
    #else:
    print("-" * 45)
    print("""
    1) Listar Todos
    2) Listar específico
    """)
    print("-" * 45)
    escolhaUserListar = int(input("Qual opção você deseja? "))
    if (escolhaUserListar == 1):
        arquivoEnderecos = open('enderecos.txt', 'r')
        for endereco in arquivoEnderecos:
            linhaLimpa = endereco.strip()
            listaDados = linhaLimpa.split(';')
            print(f"ID: {listaDados[0]} - Rua: {listaDados[1]} - Numero Casa: {listaDados[2]} - Complemento: {listaDados[3]} - Bairro: {listaDados[4]} - Cidade: {listaDados[5]} - Estado: {listaDados[6]}")
        arquivoEnderecos.close()
    elif (escolhaUserListar == 2):
        idPesquisa = input("Digite o id da pessoa desejada: ")

        arquivoEnderecos = open('enderecos.txt', 'r')

        for pesquisa in arquivoEnderecos:
            linhaLimpa = pesquisa.strip()
            listaDados = linhaLimpa.split(';')
            if (idPesquisa == listaDados[0]):
                print(f"ID: {listaDados[0]} - Rua: {listaDados[1]} - Numero Casa: {listaDados[2]} - Complemento: {listaDados[3]} - Bairro: {listaDados[4]} - Cidade: {listaDados[5]} - Estado: {listaDados[6]}")

        arquivoEnderecos.close()
    else:
        print("Opção inválida.")
