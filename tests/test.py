
# IMPORTANDO MODULOS
from app.schemas import *
from app.services import *
import os


# MENU PARA TESTE
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("""
    ========================================
          SISTEMA DE GESTÃO - TERMINAL
    ========================================

      1  - Cadastrar produto
      2  - Listar produtos
      3  - Buscar produto por ID
      4  - Editar produto
      5  - Ativar/Desativar produto

      6  - Registrar compra
      7  - Listar compras
      8  - Cancelar compra

      9  - Registrar venda
      10 - Listar vendas
      11 - Cancelar venda

      12 - Consultar estoque

      13 - Registrar movimentação
      14 - Listar movimentações
      15 - Cancelar movimentação

      0  - Sair

    ========================================
    """)

    try:
        return int(input('Escolha uma opção: '))
    except ValueError:
        return -1


# TRATANDO OPCAO
def caso(op: int):

    match op:

        # PRODUTOS
        case 1:
            print('CADASTRAR PRODUTO')

            nome = input('Nome: ')
            categoria = input('Categoria: ')
            unidade = input('Unidade (UN/KG): ').upper()

            produto = ProdutoCreate(
                nome=nome,
                categoria=categoria,
                unidade_gerenciamento=unidade,
                ativo=True
            )

            cadastrar_produto(produto)
            print('Produto cadastrado com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        case 2:
            print('LISTAR PRODUTOS')

            produtos = listar_produtos()

            for produto in produtos:
                print(
                    f'ID: {produto.id} | '
                    f'Nome: {produto.nome} | '
                    f'Categoria: {produto.categoria} | '
                    f'Unidade: {produto.unidade_gerenciamento} | '
                    f'Ativo: {produto.ativo}'
                )

            input('Pressione Enter para continuar...')
            caso(menu())

        case 3:
            print('BUSCAR PRODUTO POR ID')

            id_produto = int(input('Informe o ID do produto: '))
            produto = buscar_produto(id_produto)

            print(f'ID: {produto.id}')
            print(f'Nome: {produto.nome}')
            print(f'Categoria: {produto.categoria}')
            print(f'Unidade: {produto.unidade_gerenciamento}')
            print(f'Ativo: {produto.ativo}')

            input('Pressione Enter para continuar...')
            caso(menu())

        case 4:
            print('EDITAR PRODUTO')

            id_produto = int(input('ID do produto: '))
            nome = input('Nome: ')
            categoria = input('Categoria: ')
            unidade = input('Unidade (UN/KG): ').upper()

            produto = ProdutoCreate(
                nome=nome,
                categoria=categoria,
                unidade_gerenciamento=unidade,
                ativo=True
            )

            editar_produto(id_produto, produto)
            print('Produto editado com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        case 5:
            print('ATIVAR/DESATIVAR PRODUTO')

            id_produto = int(input('Informe o ID do produto: '))
            produto = ativar_desativar_produtos(id_produto)

            print(f'Produto: {produto.nome}')
            print(f'Ativo: {produto.ativo}')

            input('Pressione Enter para continuar...')
            caso(menu())

        # COMPRAS
        case 6:
            print('REGISTRAR COMPRA')

            produto_id = int(input('ID do produto: '))
            fornecedor = input('Fornecedor: ')
            quantidade = float(input('Quantidade: '))
            valor = float(input('Valor total da compra: R$ ').replace(',', '.'))

            compra = CompraCreate(
                produto_id=produto_id,
                fornecedor=fornecedor,
                quantidade=quantidade,
                valor=valor
            )

            registrar_compra(compra)
            print('Compra registrada com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        case 7:
            print('LISTAR COMPRAS')

            compras = listar_compras()

            for compra in compras:
                print(f'ID: {compra.id}')
                print(f'Produto: {compra.produto.nome}')
                print(f'Fornecedor: {compra.fornecedor}')
                print(f'Quantidade: {compra.quantidade}')
                print(f'Valor: R$ {compra.valor}')
                print(f'Data: {compra.data}')
                print('-' * 30)

            input('Pressione Enter para continuar...')
            caso(menu())

        case 8:
            print('CANCELAR COMPRA')

            id_compra = int(input('Informe o ID da compra: '))
            cancelar_compra(id_compra)

            print('Compra cancelada com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        # VENDAS
        case 9:
            print('REGISTRAR VENDA')

            produto_id = int(input('ID do produto: '))
            quantidade = float(input('Quantidade: '))
            valor = float(input('Valor da venda: R$ ').replace(',', '.'))
            pagamento = input('Forma de pagamento: ')

            venda = VendaCreate(
                produto_id=produto_id,
                quantidade=quantidade,
                valor=valor,
                forma_pagamento=pagamento
            )

            registrar_venda(venda)
            print('Venda registrada com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        case 10:
            print('LISTAR VENDAS')

            vendas = listar_vendas()

            for venda in vendas:
                print(f'ID: {venda.id}')
                print(f'Produto: {venda.produto.nome}')
                print(f'Quantidade: {venda.quantidade}')
                print(f'Valor: R$ {venda.valor}')
                print(f'Pagamento: {venda.forma_pagamento}')
                print(f'Data: {venda.data}')
                print('-' * 30)

            input('Pressione Enter para continuar...')
            caso(menu())

        case 11:
            print('CANCELAR VENDA')

            id_venda = int(input('Informe o ID da venda: '))
            cancelar_venda(id_venda)

            print('Venda cancelada com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        # ESTOQUE
        case 12:
            print('CONSULTAR ESTOQUE')

            produtos = listar_produtos()

            for produto in produtos:
                estoque = consultar_estoque(produto.id)

                if produto.unidade_gerenciamento == 'UN':
                    quantidade = f'{estoque:.0f}'
                else:
                    quantidade = f'{estoque:.3f}'

                print(
                    f'{produto.id} - {produto.nome}: '
                    f'{quantidade} {produto.unidade_gerenciamento}'
                )

            input('Pressione Enter para continuar...')
            caso(menu())

        # MOVIMENTAÇÕES
        case 13:
            print('REGISTRAR MOVIMENTAÇÃO')

            tipo = input('Tipo (Entrada/Saída): ').strip().capitalize()
            produto_id = input(
                'ID do produto (Enter se for apenas financeira): '
            ).strip()

            if produto_id:
                produto_id = int(produto_id)
                quantidade = float(input('Quantidade: '))
            else:
                produto_id = None
                quantidade = None

            valor = float(input('Valor: R$ ').replace(',', '.'))
            descricao = input('Descrição: ')

            movimentacao = MovimentacaoCreate(
                tipo=tipo,
                produto_id=produto_id,
                quantidade=quantidade,
                valor=valor,
                descricao=descricao
            )

            registrar_movimentacao(movimentacao)
            print('Movimentação registrada com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        case 14:
            print('LISTAR MOVIMENTAÇÕES')

            movimentacoes = listar_movimentacoes()

            for movimentacao in movimentacoes:
                print(f'ID: {movimentacao.id}')
                print(f'Tipo: {movimentacao.tipo}')
                print(f'ID do produto: {movimentacao.produto_id}')
                print(f'Quantidade: {movimentacao.quantidade}')
                print(f'Valor: R$ {movimentacao.valor}')
                print(f'Descrição: {movimentacao.descricao}')
                print(f'Data: {movimentacao.data}')
                print('-' * 30)

            input('Pressione Enter para continuar...')
            caso(menu())

        case 15:
            print('CANCELAR MOVIMENTAÇÃO')

            id_movimentacao = int(
                input('Informe o ID da movimentação: ')
            )

            cancelar_movimentacao(id_movimentacao)
            print('Movimentação cancelada com sucesso!')

            input('Pressione Enter para continuar...')
            caso(menu())

        # SAIR
        case 0:
            print('Saindo do sistema...')

        case _:
            print('Opção inválida!')
            input('Pressione Enter para continuar...')
            caso(menu())


if __name__ == '__main__':
    caso(menu())