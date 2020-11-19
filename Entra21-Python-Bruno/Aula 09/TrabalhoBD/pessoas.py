class Pessoa:
    def __init__(self, nome, dataNascimento, cpf, endereco, salario, profissao, email, telefone, nomeResponsavel, sexo, naturalidade, nacionalidade):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nomeResponsavel = nomeResponsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade
    
    def infoPessoa(self):
        nome = input("Digite nome completo: ")
        dataNascimento = input("Digite sua data de nascimento: ")
        cpf = input("Digite seu CPF: ")
        endereco = input("Digite seu endereço: ")
        profissao = input("Digite sua profissão: ")
        salario = input("Digite seu salário: ")
        email = input("Digite seu email: ")
        telefone = input("Digite seu telefone: ")
        nomeResponsavel = input("Digite o nome do seu responsável: ")
        sexo = input("Digite seu sexo: ")
        naturalidade = input("Digite sua naturalidade: ")
        nacionalidade = input("Digite sua nacionalidade: ")
        dadosPessoa = Pessoa(nome, dataNascimento, cpf, endereco, profissao, salario, email, telefone, nomeResponsavel, sexo, naturalidade, nacionalidade)
        return dadosPessoa
