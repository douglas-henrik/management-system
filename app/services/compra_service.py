# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import Compra, Produto
from app.schemas import CompraCreate

# REGISTANDO COMPRA
def registrar_compra(compra: CompraCreate):
  '''Essa função serve para cadastrar uma compra'''

  db = SessionLocal()

  try:
    if compra.quantidade <= 0 or compra.valor <= 0:
      raise ValueError('Valor e Quantidade não pode ser menor ou igual a zero')

    if compra.produto_id <= 0:
      raise ValueError('ID não pode ser menor ou igual a zero')

    produto = db.query(Produto).filter(Produto.id == compra.produto_id).first()

    if produto is None:
      raise ValueError('ID informado não corresponde a um produto')

    nova_compra = Compra(
      fornecedor = compra.fornecedor,
      quantidade = compra.quantidade,
      valor = compra.valor,
      data = compra.data,
      produto_id = compra.produto_id
    )

    db.add(nova_compra)
    db.commit()
    db.refresh(nova_compra)

    nova_compra.produto

    return nova_compra
  
  except Exception:
    db.rollback()
    raise
  
  finally:
    db.close()

# LISTAR TODAS AS COMPRAS
def listar_compras():
  '''Essa função serve para mostrar todas as compras registradas'''

  db = SessionLocal()

  try:
    compras = db.query(Compra).all()

    for compra in compras:
      compra.produto

    return compras

  finally:
    db.close()

# CANCELANDO COMPRAS
def cancelar_compra(id: int):
  '''Essa função cancela uma compra, e remove do banco de dados'''

  db = SessionLocal()

  try:
    if id <= 0:
      raise ValueError('O ID deve ser maior que zero')

    compra = db.query(Compra).filter(Compra.id == id).first()

    if compra is None:
      raise IndexError(f'Nenhuma compra com ID de valor {id} encontrada')

    db.delete(compra)
    db.commit()

    return compra

  finally:
    db.close()