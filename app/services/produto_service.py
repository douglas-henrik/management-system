# IMPORTANDO MODULOS
from app.database.session import SessionLocal
from app.models import produto as produto_model
from app.schemas import produto as produto_schema

# CRIANDO PRODUTO
def cadastrar_produto(produto_criar: produto_schema.ProdutoCreate):
  '''Essa função serve para criação de produto'''
  
  db = SessionLocal()
  
  data_produto = produto_model.Produto(
    nome = produto_criar.nome,
    categoria = produto_criar.categoria,
    unidade_gerenciamento = produto_criar.unidade_gerenciamento,
    ativo = produto_criar.ativo
  )

  db.add(data_produto)
  db.commit()
  db.refresh(data_produto)
  db.close()

  return data_produto

# LISTANDO PRODUTOS
def listar_produtos():
  '''Essa função retorna uma lista com todos os produtos'''

  db = SessionLocal()

  produtos = db.query(produto_model.Produto).all()

  db.close()

  return produtos

# BUSCANDO UM PRODUTO
def buscar_produto(id: int):
  '''Essa função retorna um produto, pelo ID soliciado'''

  db = SessionLocal()

  produto = db.query(produto_model.Produto).filter(produto_model.Produto.id == id).first()

  db.close()

  return produto

# EDITAR PRODUTO
def editar_produto(id: int, produto_editado: produto_schema.ProdutoCreate):
  ''' Essa função editar o produto, pelo ID informado'''

  db = SessionLocal()

  produto_antigo = db.query(produto_model.Produto).filter(produto_model.Produto.id == id).first()
  produto_antigo.nome = produto_editado.nome
  produto_antigo.categoria = produto_editado.categoria
  produto_antigo.unidade_gerenciamento = produto_editado.unidade_gerenciamento

  db.commit()
  db.refresh(produto_antigo)
  db.close()

  return produto_antigo

# ATIVAR E DESATIVAR PRODUTOS
def ativar_desativar_produtos(id: int):
  '''Essa função ativa o produto se ele estiver desativado,
     e desativa se ele estiver ativado'''

  db = SessionLocal()

  produto = db.query(produto_model.Produto).filter(produto_model.Produto.id == id).first()
  produto.ativo = not produto.ativo

  db.commit()
  db.refresh(produto)
  db.close()

  return produto