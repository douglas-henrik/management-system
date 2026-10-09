# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import *

# CONSULTANDO ESTOQUE
def consultar_estoque(db, id: int):
  '''Essa função consulta o estoque atual de um produto, pelo ID solicitado'''

  if id <= 0:
    raise ValueError('ID deve ser maior que zero')

  produto = db.query(Produto).filter(Produto.id == id).first()

  if produto is None:
    raise ValueError('ID informado não corresponde a um produto')

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

  return estoque

# LISTANDO ESTOQUE
def listar_estoque():
  '''Retorna o estoque de todos os produtos.'''

  db = SessionLocal()

  try:
    produtos = db.query(Produto).all()
    estoque_geral = []

    for produto in produtos:
      quantidade = consultar_estoque(db, produto.id)

      estoque_geral.append({
        'produto_id': produto.id,
        'produto': produto.nome,
        'unidade': produto.unidade_gerenciamento,
        'quantidade': quantidade
      })

    return estoque_geral

  finally:
    db.close()