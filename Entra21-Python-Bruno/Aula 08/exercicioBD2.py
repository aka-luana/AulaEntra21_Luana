import sqlite3

veic = sqlite3.connect('veiculos.bd')

cursor = veic.cursor()

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN placa TEXT;
""")

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN proprietario TEXT;
""")

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN numRodas INTEGER;
""")

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN qtdPassageiros INTEGER;
""")

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN motor TEXT;
""")

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN combustivel TEXT;
""")

cursor.execute("""
ALTER TABLE veiculos
    ADD COLUMN modelo TEXT;
""")

print("Colunas novas inseridas com sucesso.")

veic.close()
