# Vídeo youtube: https://www.youtube.com/watch?v=c43-mTD-8XM&list=PLesCEcYj003QiX5JaM24ytHrHiOJknwog

import sqlite3

conexao = sqlite3.connect('C:\Users\Luana M. B. Sales\Documents\Aula Python\AulaEntra21_Luana\Outros\Youtube\SQlite_Python/bdEstudo.db') # instância de acesso ao banco de dados
cursor = conexao.execute('select * from estados')
rows = cursor.fetchall() # Atribuindo todos os elementos de cursor para rows
print(rows)
