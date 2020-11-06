class Livro:
    tipo = "Físico"

    def __init__(self, nome, ano, paginas, autor):
        self.nome = nome
        self.ano = ano
        self.paginas = paginas
        self.autor = autor
    
    def __str__(self):
        return (f"Tipo livro: {self.tipo}\nNome: {self.nome}\nAno: {self.ano}\nPáginas: {self.paginas}\nAutor: {self.autor}")

    def spoiler(self):
        print("Não de spoilers!")

if __name__ == "__main__":
    l = Livro("A revolução dos bichos", 1945, 112, "George Orwell")
    print(l)

    print(isinstance(l, Livro))

    l.spoiler()