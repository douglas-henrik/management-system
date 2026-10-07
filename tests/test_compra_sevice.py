# IMPORTANDO MODULOS
from app.schemas.compra import CompraCreate
from app.services.compra_service import *
from app.models import *

# REGISTANDO COMPRA

compra = CompraCreate(
  quantidade=10,
  valor=60,
  produto_id=6
)

compra_criada = registrar_compra(compra)

# print(f'''
#   ID: {compra_criada.id}
#   Produto: {compra_criada.produto.nome}
#   Fornecedor: {compra_criada.fornecedor}
#   Quantidade: {compra_criada.quantidade}
#   Valor: R${compra_criada.valor}
#   Data: {compra_criada.data}
# ''')

# DELETENDO COMPRAS

# cancelar_compra(1)

# LISTANDO TODAS AS COMPRAS

compras = listar_compras()

for compra in compras:
  print('---------------------')
  print(f'ID: {compra.id}')
  print(f'Produto; {compra.produto.nome}')
  print(f'Fornecedor: {compra.fornecedor}')
  print(f'Quantidade: {compra.quantidade}')
  print(f'Valor: R${compra.valor}')
  print(f'Data: {compra.data}')