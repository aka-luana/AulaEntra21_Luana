# https://www.youtube.com/watch?v=j6B8shHXzks&list=PLnNURxKyyLIKX73U7hISjIY7T5KiNNLu_&index=1
# Class
# Syntaxe

# Classes devem ser dinâmicas, ou seja, se modelar a situação que estão sendo usadas

# Propriedades do computador: Marca, Memória Ram, Placa de vídeo
class Computador:
    # Construtor: __init__ -> Cria a funcionalidade incial que a classe terá
    # Self: serve para acessar as propriedades e métodos de uma instância
    def __init__(self, marca, memoriaRam, placaDeVideo):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.placaDeVideo = placaDeVideo
    
    # Funções/Métodos para toda a classe. Exemplo: Ligar, Desligar, Exibir configurações
    
    def Ligar(self):
        print("Estou ligando")
    
    def Desligar(self):
        print("Estou desligando")
    
    def ExibirConfiguracoes(self):
        print(self.marca, self.memoriaRam, self.placaDeVideo)

# Instanciando
# Todos são do tipo computador, mas cada um deles são
# diferentes pois possuem propriedades diferentes 
# cada um é independente do outro! 
computador1 = Computador('Asus','8gb','Nvidia') # Passa as informações esperadas pelo parâmetro
#computador2 = Computador('Dell','10gb','Geforce')
#computador3 = Computador('Acer','16gb','ATM')

#print(computador1.marca, computador1.memoriaRam, computador1.placaDeVideo)
#print(computador2.marca, computador2.memoriaRam, computador2.placaDeVideo)
#print(computador3.marca, computador3.memoriaRam, computador3.placaDeVideo)

computador1.Ligar()
computador1.Desligar()
computador1.ExibirConfiguracoes()
