'''
Este arquivo é responsável pelo banco de dados das Pessoas, 
tudo relacionado a isso se encontra neste módulo.
'''

import sqlite3
#from pessoas import teste
#from veiculos import Veiculo, veiculo
#from pessoas import teste
from veiculos import veiculo

conexao = sqlite3.connect("clientes.db")
cursor  = conexao.cursor()

def criaTabelaPessoa():
    '''
    Aqui é feita a criação da tabela de banco de dados de pessoas, 
    passando o nome das colunas e seus tipos. 
    '''
    
    cursor.execute("""
    CREATE TABLE pessoas (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        dataNascimento TEXT NOT NULL,
        cpf TEXT NOT NULL,
        endereco TEXT NOT NULL,
        profissao TEXT NOT NULL,
        salario TEXT NOT NULL,
        email TEXT NOT NULL,
        telefone TEXT NOT NULL,
        nomeResponsavel TEXT,
        sexo TEXT NOT NULL,
        naturalidade TEXT NOT NULL,
        nacionalidade TEXT NOT NULL
    );
    """)

def criaTabelaVeiculos():
    cursor.execute("""
    CREATE TABLE veiculos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        marca TEXT NOT NULL,
        modelo TEXTE NOT NULL,
        ano TEXT NOT NULL,
        cor TEXT NOT NULL,
        placa TEXT NOT NULL,
        motor TEXT NOT NULL,
        kmRodado TEXT NOT NULL,
        proprietario TEXT NOT NULL,
        combustivel TEXT NOT NULL,
        numPortas TEXT NOT NULL,
        qtdPassageiros TEXT NOT NULL,
        valor TEXT NOT NULL,
        identificadorPessoa INTEGER,

        FOREIGN KEY (identificadorPessoa) REFERENCES pessoas(id)
    );
    """)

def insereDadosPessoas(dadosPessoa):
    lista = list(dadosPessoa.values())
    print(lista)
    cursor.execute("""
    INSERT INTO pessoas (nome, dataNascimento, cpf, endereco, profissao, salario, email, telefone, nomeResponsavel, sexo, naturalidade, nacionalidade)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, lista)

    conexao.commit()

def insereDadosVeiculos(dadosVeiculo):
    cont = 0
    cursor.execute(f"""
    SELECT * FROM pessoas;
    """)
    for linha in cursor.fetchall():
        cont += 1
    print(cont)

    lista = list(dadosVeiculo.values())
    lista.append(cont)
    #print(lista)
    cursor.execute("""
    INSERT INTO veiculos (marca, modelo, ano, cor, placa, motor, kmRodado, proprietario, combustivel, numPortas, qtdPassageiros, valor, identificadorPessoa)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, lista)

    conexao.commit()

#criaTabelaPessoa()
#criaTabelaVeiculos()
#insereDadosPessoas(teste)
insereDadosVeiculos(veiculo)

conexao.close()