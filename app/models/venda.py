# IMPORTANDO MODULOS
from sqlalchemy import Column, Integer, Numeric, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database.connection import Base

# TABELA DE VENDAS
class Venda(Base):
  __tablename__ = 'vendas'
  id = Column(Integer, primary_key=True, index=True, autoincrement=True)
  produto_id = Column(Integer, ForeignKey('produtos.id'), nullable=False)
  produto = relationship('Produto')
  quantidade = Column(Numeric(6, 3), nullable=False)
  valor = Column(Numeric(5, 2), nullable=False)
  forma_pagamento = Column(String, nullable=False)
  data = Column(Date,nullable=False)