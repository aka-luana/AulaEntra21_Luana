# Vídeo youtube: https://www.youtube.com/watch?v=tgJlGSy5IYk&list=PLesCEcYj003QiX5JaM24ytHrHiOJknwog&index=6

import sqlite3

conexao = sqlite3.connect("teste.db") # Todas vez que nos conectamos a um banco e o mesmo não exirtir o python irá criá-lo
cursor = conexao.cursor()

print(type(conexao))

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tabela(
        numero INTEGER BOT NULL,
        nome TEXT NOT NULL
        );
""")

conexao.close() # Python não permite excluir o db se ele não estiver fechado
