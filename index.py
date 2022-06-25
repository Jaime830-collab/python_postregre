import psycopg2
#
#configurações
"""
host = 'localhost'
dbname = 'teste'
user = 'postgres'
password = 'postgres'
sslmode = 'require'

#conexão
conn_string = 'host={0} user={1} dbname={2} password={3} sslmode={4}'.format(host, user, dbname, password, sslmode)
"""
conn = psycopg2.connect(dbname = 'teste', user = 'postgres', password = 'postgres')
inserir_usuario = """INSERT INTO usuario (id, nome, email, senha) VALUES (3, 'carlos', 'carlao@gmail.com', '1236')"""

cursor = conn.cursor()
cursor.execute(inserir_usuario)
conn.commit()
print(cursor.rowcount, "registros inseridos na tabela")
cursor.close()

resultado = cursor.fecthall()
for res in resultado:
    print(res)

"""
def create_user(nome, email, senha):
    cursor.execute("INSERT INTO usuario (nome, email, senha) VALUES (%s, %s, %s); ", (nome, email, senha))

create_user("novo usuario", "user@gmail.com", "1234")

conn.commit()
cursor.close()
conn.close()
"""