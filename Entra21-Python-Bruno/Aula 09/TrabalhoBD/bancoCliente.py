'''
Este arquivo é responsável pelo banco de dados das Pessoas, 
tudo relacionado a isso se encontra neste módulo.
'''

import sqlite3
#from pessoas import pessoa
#from veiculos import Veiculo, veiculo
#from pessoas import teste
#from veiculos import veiculo

#class Conexao:
#    def __init__(self):
#        pass 
#
#    def conectar(self):
#        self.conexao = sqlite3.connect('clientes.db')
#        return self.conexao.cursor()
#
#    def desconectar(self):
#        self.conexao.close()
#
#c = Conexao()

def criaTabelaPessoa():
    '''
    Aqui é feita a criação da tabela de banco de dados de pessoas, 
    passando o nome das colunas e seus tipos. 
    '''
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoas (
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

    conexao.close()

def criaTabelaVeiculos():
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS veiculos (
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

    conexao.close()

def criaTabelaPessoaVeiculo():
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pessoasVeiculos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        idPessoa INTEGER,
        idVeiculo INTEGER,

        FOREIGN KEY (idPessoa) references pessoas(id),
        FOREIGN KEY (idVeiculo) references veiculos(id)
    )
    """)

    conexao.close()

def insereDadosPessoaVeiculo():
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()
    
    cursor.execute("SELECT id from pessoas")
    idPessoa = cursor.fetchall()

    cursor.execute("SELECT id from veiculos")
    idVeiculos = cursor.fetchall()

    cursor.execute("""
    INSERT INTO pessoasVeiculos (idPessoa, idVeiculo)
    VALUES (?,?)
    """, (idPessoa, idVeiculos))
    conn.commit()

    conexao.close()

def insereDadosPessoas(dadosPessoa):
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()
    lista = list(dadosPessoa.values())
    cursor.execute("""
    INSERT INTO pessoas (nome, dataNascimento, cpf, endereco, profissao, salario, email, telefone, nomeResponsavel, sexo, naturalidade, nacionalidade)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
    """, lista)

    conexao.commit()

    conexao.close()

def insereDadosVeiculos(dadosVeiculo):
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()

    cont = 0
    cursor.execute(f"""
    SELECT * FROM pessoas;
    """)
    for linha in cursor.fetchall():
        cont += 1

    lista = list(dadosVeiculo.values())
    lista.append(cont)
    cursor.execute("""
    INSERT INTO veiculos (marca, modelo, ano, cor, placa, motor, kmRodado, proprietario, combustivel, numPortas, qtdPassageiros, valor, identificadorPessoa)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, lista)
    
    conexao.commit()

    conexao.close()

    print(f"Cadastro realizado com sucesso! Seu número de cadastro é {cont}")

def visualizarCadastro():
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()
    
    escolha = int(input("""Digite a opção desejada: 
    1. Todos os cadastros
    2. Pesquisar um cadastro específico.
    """))

    if escolha == 1:
        cursor.execute("""
        SELECT pessoas.nome, pessoas.id, veiculos.identificadorPessoa, veiculos.placa FROM pessoas 
        INNER JOIN pessoasVeiculos ON pessoas.id = pessoasVeiculos.idPessoa
        INNER JOIN veiculos ON pessoasVeiculos.idVeiculo = veiculos.id
        """)

        result = cursor.fetchall()
        print(result)

        #print(f"Seja bem vindo ao mundo pokemon, {result[0][0]}! Cuide bem do seu {result[0][1]}!")

    conexao.close()