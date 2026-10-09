# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import Movimentacao, Produto
from app.schemas import MovimentacaoCreate
from app.services import consultar_estoque

# CRIANDO UMA MOVIMENTAÇÃO
def registrar_movimentacao(movimentacao: MovimentacaoCreate):
  '''Essa função registrar uma movimentação no banco de dados, seja ela de entrada ou saída'''

  db = SessionLocal()

  try:
    if movimentacao.tipo not in ['Entrada', 'Saída']:
      raise ValueError('Tipo: Informe apenas Entrada ou Saída')

    if movimentacao.produto_id is not None:
      if movimentacao.produto_id <= 0:
        raise ValueError('ID deve ser maior que zero')

      produto = db.query(Produto).filter(Produto.id == movimentacao.produto_id).first()

      if produto is None:
        raise ValueError('ID informado não corresponde a um produto')

      if movimentacao.quantidade is None:
        raise ValueError('Informar quantidade é obrigatório, se houver produto')

      if movimentacao.quantidade <= 0:
        raise ValueError('Quantidade deve ser maior que zero')

      if movimentacao.tipo == 'Saída':
        if movimentacao.quantidade > consultar_estoque(db=db, id=produto.id):
          raise ValueError('Produto não tem estoque suficiente')

    if movimentacao.produto_id is None:
      if movimentacao.quantidade is not None:
          raise ValueError('Não informe quantidade quando não houver produto.')

    if movimentacao.valor < 0:
      raise ValueError('ERROR: Valor tem que ser maior ou igual a zero')

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

    return nova_movimentacao

  except Exception:
    db.rollback()
    raise

  finally:
    db.close()

# LISTANDO MOVIMENTAÇÕES
def listar_movimentacoes():
  '''Essa função mostra todo o historico de movimentações, no banco de dados'''

  db = SessionLocal()

  try:
    movimentacoes = db.query(Movimentacao).all()

    return movimentacoes

  finally:
    db.close()

# CANCELANDO MOVIMENTAÇÕES
def cancelar_movimentacao(id: int):
  '''Essa função cancela uma movimentação pelo ID, registrado no banco de dados'''

  db = SessionLocal()

  try:
    if id <= 0:
      raise ValueError('ID deve ser maior que zero')

    movimentacao = db.query(Movimentacao).filter(Movimentacao.id == id).first()

    if movimentacao is None:
      raise ValueError(f'Nenhuma movimentação com ID de {id} encontrada')

    db.delete(movimentacao)
    db.commit()

    return movimentacao

  except Exception:
    db.rollback()
    raise

  finally:
    db.close()