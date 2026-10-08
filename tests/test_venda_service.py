# IMPORTANDO MODULOS
from app.schemas import VendaCreate
from app.services.venda_service import *
from app.models import *

# CRIANDO VENDA

# nova_venda = VendaCreate(
#   produto_id=1,
#   quantidade=0.123,
#   valor=9.5,
#   forma_pagamento='Cartão Credito'
# )

# venda = registrar_venda(nova_venda)

# LISTANDO VENDAS

vendas = listar_vendas()

for venda in vendas:
  print('--------------------')
  print(f'ID: {venda.id}')
  print(f'Produto: {venda.produto.nome}')
  print(f'Quantidade: {venda.quantidade}')
  print(f'Valor: {venda.valor}')
  print(f'Forma de Pagamento: {venda.forma_pagamento}')
  print(f'Data: {venda.data}')