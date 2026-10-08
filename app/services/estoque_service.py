# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import *

# CONSULTANDO ESTOQUE
def consultar_estoque(id: int):
  '''Essa função consulta o estoque atual de um produto, pelo ID solicitado'''
  db = SessionLocal()

  compras_produto = db.query(Compra).filter(Compra.produto_id == id).all()
  vendas_produto = db.query(Venda).filter(Venda.produto_id == id).all()
  movimentacoes_produto = db.query(Movimentacao).filter(Movimentacao.produto_id == id).all()

  total_compra = 0
  for compra in compras_produto:
    total_compra += compra.quantidade

  total_venda = 0
  for venda in vendas_produto:
    total_venda += venda.quantidade

  total_movimentacao_entrada = 0
  for entrada in movimentacoes_produto:
    if entrada.tipo == 'Entrada':
      total_movimentacao_entrada += entrada.quantidade

  total_movimentacao_saida = 0
  for saida in movimentacoes_produto:
    if saida.tipo == 'Saída':
      total_movimentacao_saida += saida.quantidade

  estoque = (total_compra + total_movimentacao_entrada) - (total_venda + total_movimentacao_saida)

  db.close()

  return estoque