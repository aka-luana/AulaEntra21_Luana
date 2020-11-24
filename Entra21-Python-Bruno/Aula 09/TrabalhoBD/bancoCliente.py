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
        tipoVeiculo TEXT NOT NULL,
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

    identificadorPessoa = 0
    cursor.execute("""
    SELECT id FROM pessoas;
    """)
    for todosId in cursor.fetchall():
        identificadorPessoa = todosId
    identificadorPessoa = identificadorPessoa[0]
    
    print(identificadorPessoa)

    lista = list(dadosVeiculo.values())
    lista.append(identificadorPessoa)
    cursor.execute("""
    INSERT INTO veiculos (tipoVeiculo, marca, modelo, ano, cor, placa, motor, kmRodado, proprietario, combustivel, numPortas, qtdPassageiros, valor, identificadorPessoa)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
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
           Tipo Veiculo: {dadosV[1]}
           Marca: {dadosV[2]}
           Modelo: {dadosV[3]}
           Ano: {dadosV[4]}
           Cor: {dadosV[5]}
           Placa: {dadosV[6]}
           Motor: {dadosV[7]}
           Km Rodado: {dadosV[8]}
           Nome proprietário(a): {dadosV[9]}
           Combustível: {dadosV[10]}
           Quantidade portas: {dadosV[11]}
           Quantidade passageiros: {dadosV[12]}
           Valor: {dadosV[13]}
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
    numCpf = input("           Digite o cpf da pessoa a ser excluída: ")
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
        print("           Operação cancelada.")
    else:
        print("         Opção inválida.")

def editarCadastro():  
    def edicao(campo, escolha, escolha2, identificadorPessoa):
        conexao = sqlite3.connect('clientes.db')
        cursor  = conexao.cursor()
        if escolha == 1 and escolha2 != 13:
            cursor.execute(f"""
            UPDATE pessoas
            SET {campo[0]} = ?
            WHERE cpf = ?
            """, (campo[1], identificadorPessoa))
            conexao.commit()
            print("            Edição feita com sucesso!")
        elif escolha == 1 and escolha2 == 13:
            cursor.execute(f"""
            UPDATE pessoas
            SET nome = ?, dataNascimento = ?, cpf = ?, endereco = ?, profissao = ?, salario = ?, email = ?, telefone = ?, nomeResponsavel = ?, sexo = ?, naturalidade = ?, nacionalidade = ?
            WHERE cpf = ?
            """, (campo[12], campo[13], campo[14], campo[15], campo[16], campo[17], campo[18], campo[19], campo[20], campo[21], campo[22], campo[23], identificadorPessoa))
            conexao.commit()
            print("           Edição feita com sucesso!")
        elif escolha == 2 and escolha2 != 14:
            print(identificadorPessoa)
            #identificadorP = identificadorPessoa[0]
            #print(identificadorP)
            cursor.execute(f"""
            UPDATE veiculos
            SET {campo[0]} = ?
            WHERE identificadorPessoa = ?
            """, (campo[1], identificadorPessoa))
            conexao.commit()
            print("           Edição feita com sucesso!")
        else:
            #identificadorP = identificadorPessoa[0]
            cursor.execute(f"""
            UPDATE veiculos
            SET tipoVeiculo = ?, marca = ?, modelo = ?, ano = ?, cor = ?, placa = ?, motor = ?, kmRodado = ?, proprietario = ?, combustivel = ?, numPortas = ?, qtdPassageiros = ?, valor = ?
            WHERE identificadorPessoa = ?
            """, (campo[13], campo[14], campo[15], campo[16], campo[17], campo[18], campo[19], campo[20], campo[21], campo[22], campo[23], campo[24], campo[25], identificadorPessoa))
            conexao.commit()
            print("           Edição feita com sucesso!")

        cursor.close()

    def opcoes(escolha, identificadorPessoa):
        campo = []

        def getDados(campo, escolha, escolha2, identificadorPessoa):
            print(identificadorPessoa)
            tamanhoListaCampo = len(campo)
            for i in range(tamanhoListaCampo):
                info = input(f"           Digite {campo[i]}: ")
                campo.append(info)
            edicao(campo, escolha, escolha2, identificadorPessoa)

        if escolha == 1:
            escolha2 = int(input("""
           Opções para edição:
           1. Nome
           2. Data nascimento
           3. CPF
           4. Endereço
           5. Profissão
           6. Salário
           7. Email
           8. Telefone
           9. Nome responsável
           10. Sexo
           11. Naturalidade
           12. Nacionalidade
           13. Tudo
           Digite a opção desejada: """))

            if escolha2 == 1:
                campo.append("nome")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 2:
                campo.append("dataNascimento")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 3:
                campo.append("cpf")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 4:
                campo.append("endereco")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 5:
                campo.append("profissao")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 6:
                campo.append("salario")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 7:
                campo.append("email")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 8:
                campo.append("telefone")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 9:
                campo.append("nomeResponsavel")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 10:
                campo.append("sexo")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 11:
                campo.append("naturalidade")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 12:
                campo.append("nacionalidade")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 13:
                campo.append("nome")
                campo.append("dataNascimento")
                campo.append("cpf")
                campo.append("endereco")
                campo.append("profissao")
                campo.append("salario")
                campo.append("email")
                campo.append("telefone")
                campo.append("nomeResponsavel")
                campo.append("sexo")
                campo.append("naturalidade")
                campo.append("nacionalidade")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            else:
                print("             Opção inválida.")
                opcoes(escolha, identificadorPessoa)

        elif escolha == 2:
            escolha2 = int(input("""
           Opções para edição:
           1. Tipo Veiculo
           2. Marca
           3. Modelo
           4. Ano
           5. Cor
           6. Placa
           7. Motor
           8. Km rodado
           9. Proprietário
           10. Combustível
           11. Número portas
           12. Quantidade Passageiros.
           13. Valor
           14. Tudo
           Digite a opção desejada: """))

            if escolha2 == 1:
                campo.append("tipoVeiculo")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 2:
                campo.append("marca")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 3:
                campo.append("modelo")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 4:
                campo.append("ano")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 5:
                campo.append("cor")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 6:
                campo.append("placa")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 7:
                campo.append("motor")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 8:
                campo.append("kmRodado")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 9:
                campo.append("proprietario")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 10:
                campo.append("combustivel")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 11:
                campo.append("numPorta")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 12:
                campo.append("qtdPassageiros")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 13:
                campo.append("valor")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            elif escolha2 == 14:
                campo.append("tipoVeiculo")
                campo.append("marca")
                campo.append("modelo")
                campo.append("ano")
                campo.append("cor")
                campo.append("placa")
                campo.append("motor")
                campo.append("kmRodado")
                campo.append("proprietario")
                campo.append("combustivel")
                campo.append("numPorta")
                campo.append("qtdPassageiros")
                campo.append("valor")
                getDados(campo, escolha, escolha2, identificadorPessoa)
            else:
                print("             Opção inválida.")
                opcoes(escolha, identificadorPessoa)

        else:
            print("             Opção inválida.")
            opcoes(escolha, identificadorPessoa)

    escolha = int(input("""
           1. Editar cadastro pessoa.
           2. Editar cadastro veículo.
           Digite a opção desejada: """))

    if escolha == 1:
        identificadorPessoa = input("           Digite o CPF da pessoa: ")
        opcoes(escolha, identificadorPessoa)
    elif escolha == 2:
        identificadorPessoa = input("           Digite o CPF da pessoa com o carro: ")
        conexao = sqlite3.connect('clientes.db')
        cursor  = conexao.cursor()
        cursor.execute(f"SELECT id FROM pessoas WHERE cpf = ?", (identificadorPessoa,))
        identificadorPessoa = cursor.fetchone()[0]
        print(identificadorPessoa)
        opcoes(escolha, identificadorPessoa)
        conexao.close()
    else:
        print("          Opção inválida.")
