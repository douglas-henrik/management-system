# IMPORTANDO MODULOS
from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

# TABELA DE MOVIMENTAÇÕES
class Movimentacao(Base):
  __tablename__ = 'movimentacoes'
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  tipo = Column(String, nullable=False)
  produto_id = Column(Integer, ForeignKey('produtos.id'))
  quantidade = Column(Numeric(6, 3))
  valor = Column(Numeric(5, 2), nullable=False)
  descricao = Column(String)
  data = Column(Date, nullable=False)