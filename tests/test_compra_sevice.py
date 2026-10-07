# IMPORTANDO MODULOS
from app.schemas.compra import CompraCreate
from app.services.compra_service import *
from app.models import *

# REGISTANDO COMPRA

compra = CompraCreate(
  fornecedor='KIBON',
  quantidade=10,
  valor=100,
  produto_id=1
)

compra_criada = registrar_compra(compra)

print(f'''
  ID: {compra_criada.id}
  Produto: {compra_criada.produto.nome}
  Fornecedor: {compra_criada.fornecedor}
  Quantidade: {compra_criada.quantidade}
  Valor: R${compra_criada.valor}
  Data: {compra_criada.data}
''')