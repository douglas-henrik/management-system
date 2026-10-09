# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import Venda, Produto
from app.schemas import VendaCreate
from app.services import consultar_estoque

# REGISTRANDO VENDA
def registrar_venda(venda: VendaCreate):
  '''Essa função registra uma venda, e cadastra no banco de dados'''

  db = SessionLocal()

  try:
    if venda.quantidade <= 0 or venda.valor <= 0:
      raise ValueError('Valor e Quantidade não pode ser menor ou igual a zero')

    if venda.produto_id <= 0:
      raise ValueError('ID deve ser maior que zero')

    produto = db.query(Produto).filter(Produto.id == venda.produto_id).first()

    if produto is None:
      raise ValueError('ID informado não corresponde a um produto')

    if not produto.ativo:
      raise ValueError('Produto está desativado')

    if venda.quantidade > consultar_estoque(db=db, id=produto.id):
      raise ValueError('Produto não tem estoque suficiente')

    if venda.forma_pagamento not in ['PIX', 'Dinheiro', 'Cartão Débito', 'Cartão Crédito']:
      raise ValueError('Para forma de pagamento informe: PIX, Dinheiro, Cartão Débito, Cartão Crédito')

    nova_venda = Venda(
      produto_id = venda.produto_id,
      quantidade = venda.quantidade,
      valor = venda.valor,
      forma_pagamento = venda.forma_pagamento,
      data = venda.data
    )

    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)

    nova_venda.produto

    return nova_venda

  except Exception:
    db.rollback()
    raise

  finally:
    db.close()

# LISTANDO VENDAS REGISTRADAS
def listar_vendas():
  '''Essa função lista todas as vendas registradas no banco de dados'''

  db = SessionLocal()

  try:
    vendas = db.query(Venda).all()

    for venda in vendas:
      venda.produto

    return vendas

  finally:
    db.close()

# CANCELANDO VENDAS
def cancelar_venda(id: int):
  '''Essa função cancela uma venda resgistrada pelo ID da venda'''

  db = SessionLocal()

  try:
    if id <= 0:
      raise ValueError('ID deve ser maior que zero')

    venda = db.query(Venda).filter(Venda.id == id).first()

    if venda is None:
      raise ValueError(f'Nenhuma venda com ID de valor {id} encontrada')

    db.delete(venda)
    db.commit()

    return venda

  finally:
    db.close()