# ===== Dicionários

# ===== Declaração
dicionario_pessoa = {}

# ===== Declaração com chave/valor
dicionario_pessoa = {'nome':"Arthur"}

# ===== Acessando dados
print(dicionario_pessoa['nome'])

# ===== Adicionando novas chaves e valores após a criação
dicionario_pessoa['idade'] = 27
dicionario_pessoa['rua'] = 'agua branca'
dicionario_pessoa['numCasa'] = 355

print(dicionario_pessoa)

# ===== Alterando o valor de uma chave
dicionario_pessoa['idade'] = 17

# ===== Removendo uma chave
del dicionario_pessoa['rua']
dicionario_pessoa.pop('numCasa')

# ===== CRUD - Create, Read, Update, Delete
# ===== São as 4 operações básicas de um dado

# ===== Lendo dados do dicionário um a um
print(dicionario_pessoa['nome'], dicionario_pessoa['idade'])
# ===== Lendo dados do dicionário de forma diamica e excluindo uma chave
for chaves, valores in dicionario_pessoa.items():
    if chaves == 'idade':
        dicionario_pessoa.pop('idade')
        break

print(dicionario_pessoa)