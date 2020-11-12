# Construa uma classe chamada veículo com no minímo 5 atributos e 3 metódos
# Faça outras 3 classes que herdem da classe veículo; 
# por exemplo Carro; e ajuste as funções onde necessário (polimorfismo)
from pessoa import Pessoa
from pessoa import NovaPessoa

class Veiculo:
    passageiros = []

    def __init__(self, cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta):
        self.cor = cor
        self.marca = marca
        self.ano = ano
        self.kmRodado = kmRodado
        self.tipoVeiculo = tipoVeiculo
        self.qtdPorta = qtdPorta
    
    def som(self):
        return "bi bi"
    
    def uber(self):
        if ((self.qtdPorta > 2) and (self.ano > 2010) and (self.tipoVeiculo == 'Carro')): return("Pode ser uber!")
        else: return("Não pode ser uber")
    
    def venda(self, preco):
        return(
f"""Oportunidade de compra:
Veículo: {self.tipoVeiculo}
Ano: {self.ano}
Marca: {self.marca}
Km rodado: {self.kmRodado}
Cor: {self.cor}
Preco: {preco}""")
    
    def addPassageiro(self, classe):
        if (self.tipoVeiculo == "Carro"):
            if (len(self.passageiros) < 5):
                self.passageiros.append(classe)
            else:
                print(f"Carro cheio para o(a) {classe.nome}") 
        elif (self.tipoVeiculo == "Moto"):
            if (len(self.passageiros) < 2):
                self.passageiros.append(classe)
            else:
                print(f"Moto cheia para o(a) {classe.nome}") 
        elif (self.tipoVeiculo == "Onibus"):
            if (len(self.passageiros) < 30):
                self.passageiros.append(classe)
            else:
                print(f"Onibus cheio para o(a) {classe.nome}") 


    def remPassageiro(self):
        contador = 0
        print("Escolha a pessoa para excluir:")
        for pessoa in self.passageiros:
            print(f"{contador}. {pessoa.nome} {pessoa.idade} {pessoa.cpf}")
            contador += 1
        
        escolhaUser = int(input("Qual passageiro você deseja excluir? "))
        del(self.passageiros[escolhaUser])
    
    def mostraPassageiros(self):
        for pessoa in self.passageiros:
            print(pessoa.nome, pessoa.idade, pessoa.cpf)

class Moto(Veiculo):
    def __init__(self, cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta):
        super().__init__(cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta)

class Onibus(Veiculo):
    def __init__(self, cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta):
        super().__init__(cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta)
    
    def som(self):
        return "BII BII"

class Carro(Veiculo):
    def __init__(self, cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta):
        super().__init__(cor, marca, ano, kmRodado, tipoVeiculo, qtdPorta)
    
    def som(self):
        return "bibi bibi bibi"

moto = Moto("Vermelho", "Honda", 2014, 2000, "Moto", 0)
print(moto.som())
print(moto.uber())
print(moto.venda(3000))

print("\n")

onibus = Onibus("Cinza", "Honda", 2020, 10000, "Onibus", 3)
print(onibus.som())
print(moto.uber())

print("\n")

carro = Carro("Preto", "Tesla", 2020, 0, "Carro", 4)
print(carro.som())
print(carro.uber())
carro.addPassageiro(NovaPessoa("Luana", 19, 123))
carro.addPassageiro(NovaPessoa("Amana", 18, 321))
print(carro.mostraPassageiros())
carro.addPassageiro(NovaPessoa("Alana", 49, 456))
carro.addPassageiro(NovaPessoa("Ana", 39, 654))
print(carro.mostraPassageiros())
carro.addPassageiro(NovaPessoa("Maria", 60, 789))
carro.addPassageiro(NovaPessoa("Peter", 30, 987))
carro.remPassageiro()
print(carro.mostraPassageiros())