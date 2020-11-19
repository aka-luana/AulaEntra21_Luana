import sqlite3

veic = sqlite3.connect('teste.bd')

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

print("Tabela teste criada.")

veic.close()

veic = sqlite3.connect('teste.bd')

cursor = veic.cursor()

def incluiColuna(coluna, tipo):
    cursor.execute("""
    ALTER TABLE teste
        ADD COLUMN ? ?;
    """, (coluna, tipo))

incluiColuna("Pais", "TEXT")

veic.close()