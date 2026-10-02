# IMPORTANDO MODULOS
from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

# TABELA DE COMPRAS
class Compra(Base):
  __tablename__ = 'compras'
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  fornecedor = Column(String)
  quantidade = Column(Numeric(6, 3), nullable=False)
  valor = Column(Numeric(5, 2), nullable=False)
  data = Column(Date, nullable=False)
  produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
  produto = relationship('Produto')