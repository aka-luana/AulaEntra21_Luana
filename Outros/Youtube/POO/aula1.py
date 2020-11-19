# https://www.youtube.com/watch?v=BALM_oJcJL4

# Abstração: tentar abstrair características que exitem em comum em alguma entidade (Passaros: bico, pata, asa, penas)
# Com isso, quando formos definir algum objeto em especídico, um Pica Pau por exemplo, é necessário definir apenas as 
# características que o diferem das outras espécies de pássaros

class Fila:
    fila = []

    def __init__(self): # Traz atributos dinâmicos (Ex: filas diferentes com suas respectivas listas - Supermercado, Banco, Loterica)
        self.fila = []

    def entrar(self, nome):
        self.fila.append(nome)
    
    def sair(self):
        self.fila.pop(0) # Vai retirar o primeiro

supermercado = Fila()

print(supermercado.fila)
supermercado.sair()
print(supermercado.fila)

