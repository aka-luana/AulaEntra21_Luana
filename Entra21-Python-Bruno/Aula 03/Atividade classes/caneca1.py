class Caneca:
    setor = "Cozinha"

    def __init__(self, cor, tamanho, preco):
        self.cor = cor
        self.tamanho = tamanho
        self.preco = preco
    
    def __str__(self):
        return f"Setor: {self.setor}\nCor: {self.cor}\nTamanho: {self.tamanho}\nPreço: {self.preco}"
    
    def bebida(self):
        print("Passei café agora, pegue a sua caneca e tome um gole.")
    
if __name__ == "__main__":
    c = Caneca("Amarela", "Grande", 10)
    print(c)

    print(isinstance(c, Caneca))

    c.bebida()