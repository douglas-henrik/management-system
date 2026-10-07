# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import compra as compra_model
from app.schemas import compra as compra_schema

# REGISTANDO COMPRA
def registrar_compra(compra: compra_schema.CompraCreate):
  '''Essa função serve para cadastrar uma compra'''

  if compra.quantidade <= 0 or compra.valor <= 0:
    raise ValueError('ERROR: Valor e Quantidade não pode ser menor ou igual a zero')

  db = SessionLocal()

  nova_compra = compra_model.Compra(
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

  db.close()

  return nova_compra

# LISTAR TODAS AS COMPRAS
def listar_compras():
  '''Essa função serve para mostrar todas as compras registradas'''

  db = SessionLocal()

  compras = db.query(compra_model.Compra).all()

  if not compras:
    raise IndexError('ERROR: Nenhuma compra registrada')

  for compra in compras:
    compra.produto

  db.close()

  return compras

# CANCELANDO COMPRAS
def cancelar_compra(id: int):
  '''Essa função cancela uma compra, e remove do banco de dados'''

  db = SessionLocal()

  compra = db.query(compra_model.Compra).filter(compra_model.Compra.id == id).first()

  if not compra:
    raise IndexError(f'ERROR: Nenhuma compra com ID de valor {id} encontrada')

  db.delete(compra)
  db.commit()
  db.close()

  return compra