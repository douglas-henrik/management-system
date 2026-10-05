# IMPORTANDO MODULOS
from app.schemas.produto import ProdutoCreate
from app.services.produto_service import *

# CRIANDO PRODUTO

# produto = ProdutoCreate(
#    nome="Picolé Morango",
#    categoria="Picolé",
#    unidade_gerenciamento="UN"
# )

# produto_criado = cadastrar_produto(produto)

# print("Produto criado com sucesso!")
# print(f"ID: {produto_criado.id}")
# print(f"Nome: {produto_criado.nome}")
# print(f"Categoria: {produto_criado.categoria}")
# print(f"Unidade: {produto_criado.unidade_gerenciamento}")
# print(f"Ativo: {produto_criado.ativo}")

# ATIVANDO E DESATIVANDO PRODUTOS
# ativar_desativar_produtos(4)

# LISTANDO PRODUTOS

# produtos = listar_produtos()

# for produto in produtos:
#    print(f"ID: {produto.id}")
#    print(f"Nome: {produto.nome}")
#    print(f"Categoria: {produto.categoria}")
#    print(f"Unidade: {produto.unidade_gerenciamento}")
#    print(f"Ativo: {produto.ativo}")
#    print("--------------------")

# BUSCANDO PRODUTO

# produto = buscar_produto(5)

# print(f"ID: {produto.id}")
# print(f"Nome: {produto.nome}")
# print(f"Categoria: {produto.categoria}")
# print(f"Unidade: {produto.unidade_gerenciamento}")
# print(f"Ativo: {produto.ativo}")
# print("--------------------")

# EDITANDO PRODUTO

# produto = ProdutoCreate(
#   nome='Milkshake Chocolate',
#   categoria='Milkshake',
#   unidade_gerenciamento='UN'
# )

# produto_editado = editar_produto(4, produto)

# print(f"ID: {produto_editado.id}")
# print(f"Nome: {produto_editado.nome}")
# print(f"Categoria: {produto_editado.categoria}")
# print(f"Unidade: {produto_editado.unidade_gerenciamento}")
# print(f"Ativo: {produto_editado.ativo}")
# print("--------------------")