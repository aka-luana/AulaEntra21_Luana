class Bola:
    setor = "Infantil"

    def __init__(self, cor, esporte, tamanho):
        self.cor = cor
        self.esporte = esporte
        self.tamanho = tamanho
    
    def __str__(self):
        return f"Setor: {self.setor}\nCor: {self.cor}\nEsporte: {self.esporte}\nTamanho: {self.tamanho}"

    def partida(self):
        print(f"Vamos jogar uma partida de {self.esporte}")
    
if __name__ == "__main__":
    b = Bola("Branca e preta", "Futebol", "Normal")
    print(b)

    print(isinstance(b, Bola))

    b.partida()