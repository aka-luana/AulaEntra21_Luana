'''
Este arquivo é responsável por tudo relacionado diretamente com os veiculos.
'''

class Veiculo:
    def __init__(self, tipoVeiculo, marca, modelo, ano, cor, placa, motor, kmRodado, proprietario, combustivel, numPortas, qtdPassageiros, valor):
        self.tipoVeiculo    = tipoVeiculo
        self.marca          = marca
        self.modelo         = modelo
        self.ano            = ano
        self.cor            = cor
        self.placa          = placa
        self.motor          = motor
        self.kmRodado       = kmRodado
        self.proprietario   = proprietario
        self.combustivel    = combustivel
        self.numPortas      = numPortas
        self.qtdPassageiros = qtdPassageiros
        self.valor          = valor
    
def infoVeiculo(veic):
    '''
    Aqui fazemos os inputs das informações de cadastro de um carro, após isso
    colocamos os dados em um objeto da classe Carro e retornamos esse mesmo objeto.
    '''
    print("\n            ----- CADASTRO VEICULO ----- \n")
    tipoVeiculo    = input("            Qual o tipo de veículo: ")
    marca          = input("            Qual a marca?: ")
    modelo         = input("            Qual o modelo?: ")
    ano            = input("            Qual o ano?: ")
    cor            = input("            Qual a cor?: ")
    placa          = input("            Qual a placa?: ")
    motor          = input("            Qual o motor?: ")
    kmRodado       = input("            Quantos km rodados?: ")
    proprietario   = input("            Qual o nome do proprietario?: ")
    combustivel    = input("            Qual o tipo de combustível?: ")
    numPortas      = input("            Quantas portas?: ")
    qtdPassageiros = input("            Quantos passageiros?: ")
    valor          = input("            Qual o valor do veículo?: ")
    
    print("\n            ----------------------------- \n")
    dadosVeiculo = Veiculo(tipoVeiculo, marca, modelo, ano, cor, placa, motor, kmRodado, proprietario, combustivel, numPortas, qtdPassageiros, valor)
    return dadosVeiculo.__dict__

