class Pessoa:
    def __init__(self, nome, endereco, cpf, telefone):
        self.nome = nome
        self.endereco = endereco
        self.cpf = cpf
        self.telefone = telefone

class Banco():
    def __init__(self, numConta):
        self.numConta = numConta

class NuConta(Banco):
    def __init__(self):
        super().__init__()

class Viacredi(Banco):
    def __init__(self):
        super().__init__()

class Conta(Banco):
    def __init__(self, pessoa: Pessoa, banco: Banco, numConta: Banco):
        pass


def cadastroPessoa(pessoa: Pessoa):
    pessoas = open("cadastroPessoasBanco.txt", "a")
    nome = input("Digite seu nome: ")
    endereco = input("Digite seu endereço: ")
    cpf = input("Digite seu cpf: ")
    telefone = input("Digite seu telefone: ")
    pessoas.write(f"{nome};{endereco};{cpf};{telefone}")
    pessoas.close()

def cadastroConta(banco: Banco):
    listaPessoasCadastradas = []
    continuaCadastro = False
    with open("cadastroPessoasBanco.txt") as arqAberto:
        for linha in arqAberto:
            listaPessoasCadastradas.append(linha.strip().split(';'))

    cpf = input("Digite seu cpf para abrir a conta: ")
    for index in listaPessoasCadastradas:
        #print(listaPessoasCadastradas, index)
        print(index[2])
        print(cpf)
        cpfArquivo = str(index[2])
        if cpf == cpfArquivo:
            continuaCadastro = True
            break
        else:
            continuaCadastro = False
        
    if (continuaCadastro):
        banco = open("cadastroConta.txt", "w")
        escolhaBanco = int(input("""Opções banco:
        1. NuConta
        2. Viacredi
        Escolha seu banco: """))
        if escolhaBanco == 1:
            print("Escolheu NuConta")
        elif escolhaBanco == 2:
            print("Escolheu Viacredi")
        else:
            print("Banco inválido")
        banco.write(f"{cpf};{escolhaBanco}")
    else:
        print("Cliente inexistente.")


if __name__ == "__main__":
    while True:
        valor = int(input(
            """
            Menu Banco:
            1 - Cadastrar Pessoa
            2 - Cadastrar Conta
            3 - Visualizar Saldo
            4 - Fazer um depósito
            5 - Sair
            Digite a operação desejada: """))

        if (valor == 1):
            cadastroPessoa(Pessoa)
        elif (valor == 2):
            cadastroConta(Banco)
        if(valor == 5):
            print("Agradecemos a sua visita!")
            break
