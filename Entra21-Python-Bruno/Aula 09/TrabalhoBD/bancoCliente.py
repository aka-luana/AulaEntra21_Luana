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

    identificadorPessoa = None
    cursor.execute("""
    SELECT * FROM pessoas;
    """)
    for linha in cursor.fetchall():
        identificadorPessoa = linha
        break
    identificadorPessoa = identificadorPessoa[0]

    lista = list(dadosVeiculo.values())
    lista.append(identificadorPessoa)
    cursor.execute("""
    INSERT INTO veiculos (marca, modelo, ano, cor, placa, motor, kmRodado, proprietario, combustivel, numPortas, qtdPassageiros, valor, identificadorPessoa)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, lista)
    
    conexao.commit()

    conexao.close()

def visualizarCadastro():
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()
    
    escolha = int(input("""
            1. Todos os cadastros
            2. Pesquisar um cadastro específico.
            Digite a opção desejada: """))

    if escolha == 1:
        cursor.execute("""
        SELECT * FROM pessoas
        """)
        dPessoas = cursor.fetchall()
        cursor.execute("""
        SELECT * FROM veiculos
        """)
        dVeiculos = cursor.fetchall()
        
        for dadosP, dadosV in zip(dPessoas, dVeiculos):
            print(f"""           ------------------------
           ------ Cadastro {dadosP[0]} ------
              Informações pessoa
           Nome: {dadosP[1]}
           Data Nascimento: {dadosP[2]} 
           CPF: {dadosP[3]}
           Endereço: {dadosP[4]}
           Profissão: {dadosP[5]}
           Salário: {dadosP[6]}
           Email: {dadosP[7]}
           Telefone: {dadosP[8]}
           Nome Responsável: {dadosP[9]}
           Sexo: {dadosP[10]}
           Naturalidade: {dadosP[11]}
           Nacionalidade: {dadosP[12]}
           
              Informações veículo
           Marca: {dadosV[1]}
           Modelo: {dadosV[2]}
           Ano: {dadosV[3]}
           Cor: {dadosV[4]}
           Placa: {dadosV[5]}
           Motor: {dadosV[6]}
           Km Rodado: {dadosV[7]}
           Nome proprietário(a): {dadosV[8]}
           Combustível: {dadosV[9]}
           Quantidade portas: {dadosV[10]}
           Quantidade passageiros: {dadosV[11]}
           Valor: {dadosV[12]}
           ------------------------""")
    elif escolha == 2:
        numCpf = input("            Digite seu cpf: ")
        cursor.execute("""
        SELECT * FROM pessoas
        """)
        dPessoas = cursor.fetchall()
        cursor.execute("""
        SELECT * FROM veiculos
        """)
        dVeiculos = cursor.fetchall()
        
        for dadosP, dadosV in zip(dPessoas, dVeiculos):
            if (numCpf == dadosP[3]):
                print(f"""           ------------------------
               ------ Cadastro {dadosP[0]} ------
                   Informações pessoa
               Nome: {dadosP[1]}
               Data Nascimento: {dadosP[2]} 
               CPF: {dadosP[3]}
               Endereço: {dadosP[4]}
               Profissão: {dadosP[5]}
               Salário: {dadosP[6]}
               Email: {dadosP[7]}
               Telefone: {dadosP[8]}
               Nome Responsável: {dadosP[9]}
               Sexo: {dadosP[10]}
               Naturalidade: {dadosP[11]}
               Nacionalidade: {dadosP[12]}
               
                  Informações veículo
               Marca: {dadosV[1]}
               Modelo: {dadosV[2]}
               Ano: {dadosV[3]}
               Cor: {dadosV[4]}
               Placa: {dadosV[5]}
               Motor: {dadosV[6]}
               Km Rodado: {dadosV[7]}
               Nome proprietário(a): {dadosV[8]}
               Combustível: {dadosV[9]}
               Quantidade portas: {dadosV[10]}
               Quantidade passageiros: {dadosV[11]}
               Valor: {dadosV[12]}
               ------------------------""")
                break
            else:
                pass
    else:
        print("Opção inválida.")

    conexao.close()

def excluirCadastro():
    conexao = sqlite3.connect('clientes.db')
    cursor  = conexao.cursor()
    numCpf = input("            Digite o cpf da pessoa a ser excluída: ")
    cursor.execute("""
    SELECT * FROM pessoas
    """)
    dPessoas = cursor.fetchall()
    cursor.execute("""
    SELECT * FROM veiculos
    """)
    dVeiculos = cursor.fetchall()
    
    for dadosP, dadosV in zip(dPessoas, dVeiculos):
        if numCpf in dadosP:
            print(f"""           ------------------------
           ------ Cadastro {dadosP[0]} ------
               Informações pessoa
           Nome: {dadosP[1]}
           Data Nascimento: {dadosP[2]} 
           CPF: {dadosP[3]}
           Endereço: {dadosP[4]}
           Profissão: {dadosP[5]}
           Salário: {dadosP[6]}
           Email: {dadosP[7]}
           Telefone: {dadosP[8]}
           Nome Responsável: {dadosP[9]}
           Sexo: {dadosP[10]}
           Naturalidade: {dadosP[11]}
           Nacionalidade: {dadosP[12]}
           
              Informações veículo
           Marca: {dadosV[1]}
           Modelo: {dadosV[2]}
           Ano: {dadosV[3]}
           Cor: {dadosV[4]}
           Placa: {dadosV[5]}
           Motor: {dadosV[6]}
           Km Rodado: {dadosV[7]}
           Nome proprietário(a): {dadosV[8]}
           Combustível: {dadosV[9]}
           Quantidade portas: {dadosV[10]}
           Quantidade passageiros: {dadosV[11]}
           Valor: {dadosV[12]}
           ------------------------""")
            break
        else:
            print("         Número de cadastro inválido.")
    
    verificacacao = int(input("""
           1. Está Correto.
           2. Não está correto.
           3. Cancelar.
           Digite a opção correspondente: """))
    
    if verificacacao == 1:
        cursor.execute("SELECT id FROM pessoas WHERE cpf = ?", (numCpf,))
        identificadorPessoa = cursor.fetchone()

        cursor.execute("DELETE FROM pessoas WHERE cpf = ?", (numCpf,))
        cursor.execute("DELETE FROM veiculos WHERE identificadorPessoa = ?", (identificadorPessoa[0],))
        conexao.commit()

        print("           Excluido com sucesso.")
    elif verificacacao == 2:
        excluirCadastro()
    elif verificacacao == 3:
        print("Operação cancelada.")
    else:
        print("         Opção inválida.")
