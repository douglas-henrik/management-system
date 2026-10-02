# IMPORTANTO MODULOS
from sqlalchemy import Column, Integer, String, Boolean
from app.database.connection import Base

# TABELA DE PRODUTOS
class Produto(Base):
  __tablename__ = 'produtos'
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  nome = Column(String, nullable=False)
  categoria = Column(String)
  unidade_gerenciamento = Column(String, nullable=False)
  ativo = Column(Boolean, nullable=False)