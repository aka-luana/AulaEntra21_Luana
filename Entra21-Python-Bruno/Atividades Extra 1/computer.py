# Crie as seguintes classes com suas determinadas carcteristicas
# ram, hd, processador

# Agora, crie a classe Placa_mae, que deve ser composta pelos 3 itens acima

# Por fim, utilizando herança, crie dispositivos que utilizam a placa mãe; 
# por exemplo: computador

class Ram():
    def __init__(self, nome, desligou, quantidade):
        self.nome = nome
        self.desligou = desligou
        self.quantidade = quantidade
    
    def verificaArquivo_Ram(self, nome, desligou):
        '''
        Ram permite o acesso de arquivo no computador, mas não o armazena permanentemente (só até o desligamento - volátil).
        Aqui é feita a checagem para ver se o arquivo ainda está no amazenamento do dispositivo.
        A verificação é feita com base na variável 'desligou' do tipo boolean. 
        '''
        if self.desligou:
            print(f"O arquivo {self.nome} não está mais disponível no dispositivo.")
        else:
            print(f"O arquivo {self.nome} ainda está disponível.")
    
    def verificaQuantidade_Ram(self, quantidade):
        '''
        A quatidade da memória Ram está diretamente ligada ao desenvolvimento do computador.
        Aqui é verificado se um determinado computadpr com determinada quantidade de memória roda jogos
        Os dados foram retirados do site: https://www.showmetech.com.br/quanto-de-memoria-ram-preciso-para-jogar/
        '''
        if self.quantidade <= 4:
            print("Você talvez consiga jogar um candy crush, mas o chrome precisa estar fechado.")
        elif self.quantidade > 4 and self.quantidade <= 8:
            print("Suficiente para a maioria dos jogos modernos, mas o computador não vai nem respirar.")
        else:
            print("Consegue até pilotar um avião moleque.")

class Hd():
    def __init__(self, espacoTotal, espacoUsado):
        self.espacoTotal = espacoTotal
        self.espacoUsado = espacoUsado

    def verificaEspaco_Hd(self, espacoTotal, espacoUsado):
        '''
        Por ser um sistema de armazenamento essa função retornará ao usuário o espaço livre existente.
        A entrada contém o espaço total dos dispositivo e o espaco que está sendo usado
        '''
        if self.espacoUsado > self.espacoTotal:
            print("Erro! Espaço utilizado maior do que o suportado.")
        elif self.espacoUsado == self.espacoTotal:
            print("Armaazenamento cheio.")
        else:
            print(f"O espaço livre é de {self.espacoTotal - self.espacoUsado}GB.")

class Processador():
    def __init__(self, numero):
        self.numero = numero
    
    def devolveCore(self, numero):
        '''
        Devolve o processador do computador recebido no parâmetro
        '''
        print(f"Seu computador é um Core i{numero}.")

class PlacaMae():
    def __init__(self, ram, hd, processador):
        self.ram = ram
        self.hd = hd
        self.processador = processador         

ram = Ram("aula.py", True, 8)
hd = Hd(9000, 5614)
processador = Processador(5)

computador = PlacaMae(ram, hd, processador)

computador.ram.verificaArquivo_Ram("aula.py", True)
computador.ram.verificaQuantidade_Ram(8)
computador.hd.verificaEspaco_Hd(9000, 5614)
computador.processador.devolveCore(5)
