# https://www.youtube.com/watch?v=xWTNoTtA9V8&t=4s

'''
cls x self
    cls (@classmethod): manipulação da abstração (por um todo) de dado. 
    Parecida com uma global, pois está no escopo de todas.
    self: manipulação da instância (específico).
'''

class Fila:
    '''
    Abstração de qualuqer tipo de Fila:
        - supermercado
        - banco
        - ...
    '''

    # colocando c para deixar claro que pertente a classe
    # isso é manipulado sem um exemplo-instancia pq elas já
    # fazem parte da classe-molde
    c_fila = [] # dado geral, caso tenha várias filas (mesmo diferentes)
    # eles estariam concentrados aqui

    @classmethod
    def c_entrar(cls, obj):
        cls.c_fila.append(obj)
        print(cls.c_fila)
    # Ao colocar Fila. no powershel já estará disponível o
    # c_fila e o c_entrar. Entratanto, caso crie uma instancia
    # da classe eles não vão aparecer como sugestão pois são
    # do tipo self e não cls.

    
    # colocando s para deixar claro que é do self
    def __init__(self):
        self.s_fila = []

    # Ao criar esse def, cada instancia tera sua própria fila
    def s_entrar(self, obj):
        self.s_fila.append(obj)
        print(self.s_fila)