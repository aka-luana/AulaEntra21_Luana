import os

print(os.getcwd()) # Diretório atual

print(os.path.abspath("jogoProfessor.py")) # Caminho absoluto

print(os.path.isdir("jogoProfessor.py")) # É um diretório?

print(os.listdir("/home")) # Lista arquivos

print (os.listdir(os.path.join("/home", "bruno"))) # Junta diretórios

# Ler arquivo
try:
    file = open("arquivo.txt")
except:
    print("ops, deu ruim!")

