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