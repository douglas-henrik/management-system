# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import Produto
from app.schemas import ProdutoCreate

# CRIANDO PRODUTO
def cadastrar_produto(produto_criar: ProdutoCreate):
  '''Essa função serve para criação de produto'''

  db = SessionLocal()

  try:
    if produto_criar.unidade_gerenciamento not in ['UN', 'KG']:
      raise ValueError('Unidade: Iforme apenas UN (Unidade) ou KG (Peso)')
    
    novo_produto = Produto(
      nome = produto_criar.nome,
      categoria = produto_criar.categoria,
      unidade_gerenciamento = produto_criar.unidade_gerenciamento,
      ativo = produto_criar.ativo
    )

    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)

    return novo_produto

  except Exception:
    db.rollback()
    raise

  finally:
    db.close()

# LISTANDO PRODUTOS
def listar_produtos():
  '''Essa função retorna uma lista com todos os produtos'''

  db = SessionLocal()

  try:
    produtos = db.query(Produto).all()

    return produtos

  finally:
    db.close()

# BUSCANDO UM PRODUTO
def buscar_produto(id: int):
  '''Essa função retorna um produto, pelo ID soliciado'''

  db = SessionLocal()

  try:
    if id <= 0:
      raise ValueError('ID deve ser maior que zero')

    produto = db.query(Produto).filter(Produto.id == id).first()

    if produto is None:
      raise ValueError(f'ID informado não corresponde a um produto')

    return produto

  finally:
    db.close()

# EDITAR PRODUTO
def editar_produto(id: int, produto_editado: ProdutoCreate):
  ''' Essa função editar o produto, pelo ID informado'''

  db = SessionLocal()

  try:
    if produto_editado.unidade_gerenciamento not in ['UN', 'KG']:
      raise ValueError('Unidade: Iforme apenas UN (Unidade) ou KG (Peso)')

    if id <= 0:
      raise ValueError('ID deve ser maior que zero')

    produto_antigo = db.query(Produto).filter(Produto.id == id).first()

    if produto_antigo is None:
      raise ValueError(f'ID informado não corresponde a um produto')

    produto_antigo.nome = produto_editado.nome
    produto_antigo.categoria = produto_editado.categoria
    produto_antigo.unidade_gerenciamento = produto_editado.unidade_gerenciamento

    db.commit()
    db.refresh(produto_antigo)

    return produto_antigo
  
  except Exception:
    db.rollback()
    raise

  finally:
    db.close()

# ATIVAR E DESATIVAR PRODUTOS
def ativar_desativar_produtos(id: int):
  '''Essa função ativa o produto se ele estiver desativado,
     e desativa se ele estiver ativado'''

  db = SessionLocal()
  
  try:
    if id <= 0:
      raise ValueError('ID deve ser maior que zero')

    produto = db.query(Produto).filter(Produto.id == id).first()

    if produto is None:
      raise IndexError(f'ID informado não corresponde a um produto')

    produto.ativo = not produto.ativo

    db.commit()
    db.refresh(produto)

    return produto

  except Exception:
    db.rollback()
    raise

  finally:
    db.close()