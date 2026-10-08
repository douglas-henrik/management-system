# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import Venda
from app.schemas import VendaCreate

# REGISTRANDO VENDA
def registrar_venda(venda: VendaCreate):
  '''Essa função registra uma venda, e cadastra no banco de dados'''

  if venda.quantidade <= 0 or venda.valor <= 0:
    raise ValueError('ERROR: Valor e Quantidade não pode ser menor ou igual a zero')

  db = SessionLocal()

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

  db.close()

  return nova_venda

# LISTANDO VENDAS REGISTRADAS
def listar_vendas():
  '''Essa função lista todas as vendas registradas no banco de dados'''

  db = SessionLocal()

  vendas = db.query(Venda).all()

  if not vendas:
    raise IndexError('ERROR: Nenhuma venda registrada')

  for venda in vendas:
    venda.produto

  db.close()

  return vendas