# ==== Arquivos - Manipulação texto

# ==== open

# ==== Escrita
# ==== x - cria um novo arquivo, caso o arquivo já exista, da erro
# ==== w - cria um novo arquivo, porem se o arquivo existir apaga o que já tinha salvo
# ==== a - adiciona uma nova linha ao final do arquivo - usar com \n

dictPessoa = {'first':'luana', 'last':'matos', 'age':19}
arquivo = open('pessoa.txt', 'a')
arquivo.write(f"{dictPessoa['first']};{dictPessoa['last']};{dictPessoa['age']}; \n")
arquivo.close()

# ==== Leitura
arquivo = open('pessoa.txt', 'r')
for linha in arquivo:
    linhaLimpa = linha.strip() # ==== Limpa espaços em branco e caracteres de formatação (\n \t)
    listaDados = linhaLimpa.split(';') # ==== Não precisa falar que listaDados é uma lista pq o retorno de split é uma lista
    print(f"Nome: {listaDados[0]} - Sobrenome: {listaDados[1]} - idade: {listaDados[2]}")
    break

arquivo.close()