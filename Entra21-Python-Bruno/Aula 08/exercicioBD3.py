import sqlite3

veic = sqlite3.connect("veiculos.bd")

cursor = veic.cursor()

def atualizaBD(idBanco, placa, proprietario, numRodas, qtdPassageiros, motor, combustivel, modelo):
    cursor.execute("""
        UPDATE veiculos
        SET placa = ?, proprietario = ?, numRodas = ?, qtdPassageiros = ?, motor = ?, combustivel = ?, modelo = ?
        WHERE id = ?
    """, (placa, proprietario, numRodas, qtdPassageiros, motor, combustivel, modelo, idBanco))
    veic.commit()

atualizaBD(1, "JDB-6587", "Amanda", 4, 5, "2.0", "Gás", "Civic")
atualizaBD(2, "LMC-2019", "Luana", 2, 2, "1.6", "Disel", "Biz")

veic.close()