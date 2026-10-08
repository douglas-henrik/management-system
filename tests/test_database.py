# TESTANDO CRIAÇÃO DE TABELAS

from app.database.connection import engine, Base
from app.models.produto import Produto
from app.models.compra import Compra
from app.models.venda import Venda
from app.models.movimentacoes import Movimentacao

try:
  Base.metadata.create_all(engine)
  print('Tabelas Criadas com sucesso!')
except Exception as error:
  print(f'Erro ao criar: {error}')