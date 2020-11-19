# Dicionários e funções - Parte 2

# Dicionários
# Conjunto de dados
# Chave e não indice

# Função - typehinti
def cadastraAnimal(grupo:str, alimentacao:str, especie:str, habitat:str, voa:bool)->str:
    # escopo local ou de função
    animal = {}
    animal['grupo'] = grupo
    animal['alimentação'] = alimentacao
    animal['especie'] = especie
    animal['habitat'] = habitat
    animal['voa'] = voa
    animais.append(animal)
    return "animal cadastrado com sucesso"

animal1 = {'grupo':'ave', 'alimentação':'carnivoro', 'especie':'urubu', 'habitat':'mata atlantica', 'voa':True}
animal2 = {'grupo':'mamifero', 'alimentação':'onivoro', 'especie':'bizarro', 'habitat':'hidroseilaoque', 'voa':False}
animais = [animal1, animal2]

cadastraAnimal('ave', 'herbivoro', 'dinossauro', 'deserto', True)

for a in animais:
    print(a['especie'])

# Procedimento
# não há return
# executa um conjunto de instruções



