# https://www.youtube.com/watch?v=RhtsCbKyYoA

# Classes deixa o programador utilizar variáveis 'locais' fora do escopo delas

# Boa prática: Nomes de classes com letras maiúsculas
class DidaticaTech():
    def __init__(self, valorAntigo: int, valorNovo:int):
        self.valorAntigo = valorAntigo 
        self.valorNovo = valorNovo

    def incrementa(self):
        # O objeto que instancia a classe torna-se o self
        self.valorNovo += self.valorAntigo
        return self.valorNovo
    
    # Esse método verificará se o valor (após ser incrementado) passar de 12
    def verifica(self):
        if(self.valorNovo > 12):
            return("Ultrapassou 12")
        else:
            return("Não ultrapassou 12")
    
    # Esse método eleva o resultado a algum número
    def exponencial(self, a):
        return self.valorNovo ** a
    
    # Esse método além de incrementar eleva ao número passado (2)
    def incrementa_quadrado(self):
        self.incrementa()
        self.exponencial(2)

# Quando se instancia uma classe você tem acesso a tudo dentro dela
objDidaticaTech = DidaticaTech(10, 1) # Modo 1 de acessar um método de uma classe
a = DidaticaTech(10, 5).incrementa() # Modo 2 de acessar um método de uma classe
x = objDidaticaTech.incrementa()
# Método é o nome dado a uma funça dentro de uma classe
print(x, a)

print(objDidaticaTech.exponencial(2))

# Com o obj instanciado da classe temos acesso a 'variaveis locais' os atributos
#print(objDidaticaTech.valorAntigo)

# Essa classe herda tudo de sua super classe (DidaticaTech). Com isso ela tem acesso 
# a todos os atributos e métodos que existem dentro dela, além disso pode criar seu próprio
# atributos e métodos. 
class Calculo(DidaticaTech):
    # Para não sobrescever o contrutor da superclasse (DidaticaTech) é necessário usar o super (invoca os atributos do construtor da classe pai)
    def __init__(self, divisor):
        super().__init__(valorAntigo: int, valorNovo:int)
        self.divisor = divisor

    def decrementa(self, n):
        return self.valorNovo - n
    
    def divide(self):
        return self.valorNovo / self.divisor

c = Calculo(10, 5) 
print(c.incrementa()) # Aqui mesmo criando um objeto de Calculo ele ainda pode acessar informações de DidaticaTech
print(c.decrementa(3))
