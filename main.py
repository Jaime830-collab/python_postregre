import psycopg2

#configurações
host = 'localhost'
dbname = 'teste'
user = 'postgres'
password = 'postgres'
sslmode = 'require'

#conexão
conn_string = 'host={0} user={1} dbname={2 }password={2} sslmode'