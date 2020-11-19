import sqlite3
from pessoas import Pessoa

conexao = sqlite3.connect("pessoas.db")

cursor = conexao.cursor()

def criaTabelaPessoa():
    # TRY - EXCEPT
    cursor.execute("""
    CREATE TABLE pessoas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        dataNascimento TEXT NOT NULL,
        cpf VARCHAR(11),
        endereco TEXT NOT NULL,
        profissao TEXT NOT NULL,
        salario FLOAT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        nomeResponsavel TEXT,
        sexo TEXT NOT NULL,
        naturalidade TEXT NOT NULL,
        nacionalidade TEXT NOT NULL
    );
    """)