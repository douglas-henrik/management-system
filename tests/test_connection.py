# TESTANDO CONECTIVIDADE COM BANCO

from app.database.connection import engine

try:
    with engine.connect() as connection:
        print("Conexão com o banco realizada com sucesso!")

except Exception as error:
    print(f"Erro na conexão: {error}")