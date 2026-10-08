# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import *

# CONSULTANDO ESTOQUE
def consultar_estoque(id: int):
  '''Essa função consulta o estoque atual de um produto, pelo ID solicitado'''
  db = SessionLocal()

  compras_produto = db.query(Compra).filter(Compra.produto_id == id).all()
  vendas_produto = db.query(Venda).filter(Venda.produto_id == id).all()

  total_compra = 0
  for compra in compras_produto:
    total_compra += compra.quantidade

  total_venda = 0
  for venda in vendas_produto:
    total_venda += venda.quantidade

  estoque = total_compra - total_venda

  db.close()

  return estoque