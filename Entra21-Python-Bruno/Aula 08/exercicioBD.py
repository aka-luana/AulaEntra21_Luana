import sqlite3

veic = sqlite3.connect('veiculos.bd')

cursor = veic.cursor()

cursor.execute("""
CREATE TABLE veiculos (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cor TEXT NOT NULL,
    marca TEXT NOT NULL,
    ano INTEGER NOT NULL,
    kmRodado REAL NOT NULL,
    tipoVeiculo TEXT NOT NULL,
    qtdPorta INTEGER)
""")

print("Tabela veiculos criada.")

cursor.execute("""
    INSERT INTO veiculos (cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta)
    VALUES ('Preto', 'Honda', '2012', 50000, 'Carro', 4)    
""")

cursor.execute("""
    INSERT INTO veiculos (cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta)
    VALUES ('Vermelho', 'Honda', '2010', 0, 'Moto', NULL)    
""")

veic.commit()

print("Dados salvos na tabela.")

cursor.execute("""
SELECT * FROM veiculos;
""")

for linha in cursor.fetchall():
    print(linha)

veic.close()
