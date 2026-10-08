# IMPORTANDO MODULOS
from app.schemas import MovimentacaoCreate
from app.services.movimentacoes_service import *

# CRIANDO MOVIMENTAÇÃO

# nova_movimentacao = MovimentacaoCreate(
#   tipo= 'Saída',
#   produto_id= 1,
#   quantidade= 12.400,
#   valor= 0,
#   descricao= 'Doação'
# )

# movimentacao = registrar_movimentacao(nova_movimentacao)

# CANCELANDO MOVIMENTAÇÃO

cancelar_movimentacao(3)

movimentacoes = listar_movimentacoes()

for  movimentacao in movimentacoes:
  print('--------------------')
  print(f'ID: {movimentacao.id}')
  print(f'Tipo: {movimentacao.tipo}')
  print(f'Produto ID: {movimentacao.produto_id}')
  print(f'Quantidade: {movimentacao.quantidade}')
  print(f'Valor: {movimentacao.valor}')
  print(f'Descrição: {movimentacao.descricao}')
  print(f'Data: {movimentacao.data}')