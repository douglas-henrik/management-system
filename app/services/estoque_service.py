# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import *

# CONSULTANDO ESTOQUE
def consultar_estoque(id: int):
  '''Essa função consulta o estoque atual de um produto, pelo ID solicitado'''
  db = SessionLocal()

  compras_produto = db.query(Compra).filter(Compra.produto_id == id).all()

  estoque = 0
  for compra in compras_produto:
    estoque += compra.quantidade

  db.close()

  return estoque