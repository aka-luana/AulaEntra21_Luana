class Esmalte:
    avisoIdade = "Indicado para maiores de 3 anos"

    def __init__(self, cor, marca, preco):
        self.cor = cor
        self.marca = marca
        self.preco = preco
    
    def __str__(self):
        return f"Recomendação: {self.avisoIdade}\nCor: {self.cor}\nMarca: {self.marca}\nPreço: {self.preco}"
    
    def elogioCor(self):
        print("Essa cor vai ficar linda em você!")
    
if __name__ == "__main__":
    e = Esmalte("Vermelho", "XXX", 2.99)
    print(e)

    print(isinstance(e, Esmalte))

    e.elogioCor()