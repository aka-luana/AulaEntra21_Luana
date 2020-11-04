try:
    dictInfo = {'nome':'Luana', 'idade': '19', 'pet': 'Cachorro'}
    file = open("arqInformacoes.txt", "w")
    file.write(f"{dictInfo['nome']};{dictInfo['idade']};{dictInfo['pet']};\n")
    file.close()
except:
    print("ops, deu ruim na escrita!")

try:
    file = open("arqInformacoes.txt", "r")
    for linha in file:
        linhaLimpa = linha.strip() # ==== Limpa espaços em branco e caracteres de formatação (\n \t)
        listaDados = linhaLimpa.split(';') # ==== Não precisa falar que listaDados é uma lista pq o retorno de split é uma lista
        print(f"Idade: {listaDados[1]}")
        break
    file.close()
except:
    print("ops, deu ruim na leitura!")