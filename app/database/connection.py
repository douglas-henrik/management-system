# IMPORTANDO MODULOS
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from pathlib import Path
import os
from dotenv import load_dotenv

# CARREGANDO VARIAVEIS ENV
load_dotenv()

# CAMINHO DO BANCO DE DAOS
pasta_db = Path(os.getenv('LOCALAPPDATA', Path.home())) / 'Stockly'
pasta_db.mkdir(parents=True, exist_ok=True)

caminho_banco = pasta_db / 'database.db'

# CONEXÃO AO BANCO
database_url = f'sqlite:///{caminho_banco.as_posix()}'

# CRIANDO ENGINE
engine = create_engine(database_url)

# CRIANDO BASE TABLE
class Base(DeclarativeBase):
  pass