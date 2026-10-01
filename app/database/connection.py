# IMPORTANDO MODULOS
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv

# CARREGANDO VARIAVEIS ENV
load_dotenv()

# CONEXÃO AO BANCO
database_url = os.getenv('DATABASE')

# CRIANDO ENGINE
engine = create_engine(database_url)

# CRIANDO BASE TABLE
class Base(DeclarativeBase):
  pass