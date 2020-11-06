class Celular:
    setor = "Eletronico"

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def __str__(self):
        return (f"Setor: {self.setor}\nMarca: {self.marca}\nModelo: {self.modelo}\nCor: {self.cor}")
    
    def tiraFoto(self):
        print("Tirando foto - Xiis")

if __name__ == "__main__":
    c = Celular("Xiaomi", "Mi 8 Lite", "Preto")
    print(c)

    print(isinstance(c, Celular))

    c.tiraFoto()