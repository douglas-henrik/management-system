# IMPORTANDO MODULOS
from sqlalchemy.orm import sessionmaker
from database.connection import engine

# CRIANDO SESSÃO COM DATABSE
SessionLocal = sessionmaker(bind=engine)