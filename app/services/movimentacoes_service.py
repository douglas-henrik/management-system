# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import Movimentacao
from app.schemas import MovimentacaoCreate

# CRIANDO UMA MOVIMENTAÇÃO
def registrar_movimentacao(movimentacao: MovimentacaoCreate):
  '''Essa função registrar uma movimentação no banco de dados, seja ela de entrada ou saída'''

  if movimentacao.tipo != 'Entrada' and movimentacao.tipo != "Saída":
    raise ValueError('ERROR: Tipo so pode ser de Entrada ou Saída')

  if movimentacao.valor < 0:
    raise ValueError('ERROR: Valor tem que ser maior ou igual a zero')

  db = SessionLocal()

  nova_movimentacao = Movimentacao(
    tipo= movimentacao.tipo,
    produto_id= movimentacao.produto_id,
    quantidade= movimentacao.quantidade,
    valor= movimentacao.valor,
    descricao= movimentacao.descricao,
    data= movimentacao.data
  )

  db.add(nova_movimentacao)
  db.commit()
  db.refresh(nova_movimentacao)
  db.close()

  return nova_movimentacao

# LISTANDO MOVIMENTAÇÕES
def listar_movimentacoes():
  '''Essa função mostra todo o historico de movimentações, no banco de dados'''

  db = SessionLocal()

  movimentacoes = db.query(Movimentacao).all()

  if not movimentacoes:
    raise IndexError('ERROR: Nenhuma movimentação registrada')

  db.close()

  return movimentacoes