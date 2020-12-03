# Vídeo youtube: https://www.youtube.com/watch?v=c43-mTD-8XM&list=PLesCEcYj003QiX5JaM24ytHrHiOJknwog

import sqlite3

conexao = sqlite3.connect('bdEstudo.db') # instância de acesso ao banco de dados
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS estados (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        uf TEXT NOT NULL,
        nome TEXT NOT NULL
    );
    """)

def colocaDados(uf, nome):
    cursor.execute("""
        INSERT INTO estados (uf, nome)
        VALUES (?, ?)
    """,(uf, nome))

colocaDados("AC", "ACRE")
colocaDados("AL", "ALAGOAS")
colocaDados("AM", "AMAZONAS")
colocaDados("AP", "AMAPA")
colocaDados("BA", "BAHIA")
colocaDados("CE", "CEARA")
colocaDados("DF", "DISTRITO FEDERAL")
colocaDados("ES", "ESPIRITO SANTO")
colocaDados("GO", "GOIAS")
colocaDados("MA", "MARANHAO")
colocaDados("MG", "MINAS GERAIS")
colocaDados("MS", "MATO GROSSO DO SUL")
colocaDados("MT", "MATO GROSSO")
colocaDados("PA", "PARA")
colocaDados("PB", "PARAIBA")
colocaDados("PE", "PERNAMBUCO")
colocaDados("PI", "PIAUI")
colocaDados("PR", "PARANA")
colocaDados("RJ", "RIO DE JANEIRO")
colocaDados("RN", "RIO GRANDE DO NORTE")
colocaDados("RO", "RONDONIA")
colocaDados("RR", "RORAIMA")
colocaDados("RS", "RIO GRANDE SO SUL")
colocaDados("SC", "SANTA CATARINA")
colocaDados("SE", "SERGIPE")
colocaDados("SP", "SAO PAULO")
colocaDados("TO", "TOCANTINS")

cursor = conexao.execute('select * from estados')
rows = cursor.fetchall() # Atribuindo todos os elementos de cursor para rows -> todos os elementos vão em
# tuplas, ao colocá-las em rows fica-se várias tuplas dentro de uma lista: [(id, uf, nome), (id, uf, nome)]

for row in rows:
    print(row)
