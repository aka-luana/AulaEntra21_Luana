'''
Criar uma classe Carro com no mínimo 3 propriedades e métodos.
'''

# Criando a calsse Carro
class Carro:
    # Definindo o construtor e passando os parâmetros da classe
    def __init__(self, marca, cor, combustivel, kmRodado):
        self.marca       = marca
        self.cor         = cor
        self.combustivel = combustivel
        self.kmRodado    = kmRodado
    
    # Criando os métodos da classe: postoGasolina, elogioCorCarro, exibeTodasInformacoes

    # Vê se o combustivel do carro está na promoção 
    def postoGasolina(self):
        if self.combustivel == 'Comum':
            print('Que legal a comum está na promoção! Pode encher o tanque :D')
        else:
            print('Poxa vida só a comum está na promoção, vou ver o outro posto D:')
    
    # Pega a cor do carro e da um elogio
    def elogioCorCarro(self):
        print(f"Carros de cor {self.cor} são estilosos")
    
    # Printa na tela todas as informações do carro
    def exibeTodasInformacoes(self):
        print(f"Marca: {self.marca}\nCor: {self.cor}\nCombustível: {self.combustivel}\nKm andado: {self.kmRodado}")

# Criando um objeto da classe Carro e passando os parâmetros
carro1 = Carro("Honda", "Preto", "Comum", 150000)
carro1.postoGasolina()
carro1.elogioCorCarro()
carro1.exibeTodasInformacoes()
