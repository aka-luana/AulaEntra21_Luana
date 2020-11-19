import sqlite3

conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# adicionando uma nova coluna na tabela clientes
cursor.execute("""
ALTER TABLE clientes
ADD COLUMN bloqueado BOOLEAN;
""") # Para o campo novo é interessante colocar "DEFAULT True", assim ele insere True em todos automaticamente

conn.commit()

print('Novo campo adicionado com sucesso.')

conn.close()
