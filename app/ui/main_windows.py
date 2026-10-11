
# IMPORTANDO MODULOS

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QSizePolicy,
    QScrollArea
)

from PySide6.QtGui import QIcon
from pathlib import Path

from app.ui.produtos.produtos_window import ProdutosWindow
from app.ui.estoque.estoque_window import EstoqueWindow
from app.ui.compras.compras_window import ComprasWindow
from app.ui.vendas.vendas_window import VendasWindow
from app.ui.movimentacoes.movimentacoes_window import MovimentacoesWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        caminho_icone = (
            Path(__file__).resolve().parents[2]
            / "assets"
            / "icon.png"
        )

        self.setWindowIcon(QIcon(str(caminho_icone)))

        self.setWindowTitle("Stockly")
        self.setMinimumSize(1200, 600)

        self.setStyleSheet("""
            QLabel {
                font-size: 16px;
            }
        """)

        # ==================================
        # ÁREA DE CONTEÚDO
        # ==================================

        self.paginas = QStackedWidget()

        # Página inicial
        self.pagina_inicio = QWidget()
        layout_inicio = QVBoxLayout(self.pagina_inicio)

        titulo_inicio = QLabel("Bem-vindo ao Stockly")
        titulo_inicio.setStyleSheet(
            "font-size: 30px; font-weight: bold; margin: auto;"
        )

        self.descricao_inicio = QLabel(f"""
            O Stockly é um sistema de gerenciamento desenvolvido para facilitar o controle de produtos, estoque, compras,
            vendas e movimentações financeiras.

                COMO ULTILIZAR O SISTEMA

                1. PRODUTOS

            Cadastre os produtos que serão comercializados ou controlados pelo sistema. Informe o nome, a categoria e a
            unidade de gerenciamento (UN ou KG). Você também pode editar os dados e ativar ou desativar produtos.

                2. COMPRAS

            Registre as compras e reposições de mercadorias, informando o produto, a quantidade, o valor total, o fornecedor
            e a data. As compras registradas são consideradas no cálculo do estoque.

                3. VENDAS

            Registre as vendas realizadas, selecionando o produto, a quantidade vendida, o valor total, a forma de pagamento
            e a data. O sistema verifica a disponibilidade em estoque antes de concluir a venda.

                4. ESTOQUE

            Consulte a quantidade disponível de cada produto. O estoque é calculado considerando as compras, as vendas e as
            movimentações de entrada e saída de produtos.

                5. MOVIMENTAÇÕES

            Registre entradas e saídas adicionais de produtos ou movimentações financeiras, como despesas e outros recebimentos.
            Quando uma movimentação envolve um produto, ela pode alterar a quantidade disponível no estoque.

                RECOMENDAÇÕES DE USO

            - Cadastre os produtos antes de registrar compras e vendas.
            - Mantenha as quantidades, os valores e as datas corretos.
            - Registre as movimentações para manter o controle atualizado.
            - Antes de cancelar um registro, confira se ele foi selecionado corretamente.

            DICA: Utilize o menu lateral para navegar entre as funcionalidades.
        """)

        self.descricao_inicio.setWordWrap(True)
        self.descricao_inicio.setAlignment(
            Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft
        )
        self.descricao_inicio.setStyleSheet("""
            font-size: 16px;
            color: white;
            padding: 10px;
        """)

        # Área que permite rolar o conteúdo
        self.area_rolagem = QScrollArea()
        self.area_rolagem.setWidgetResizable(True)
        self.area_rolagem.setFrameShape(QScrollArea.Shape.NoFrame)
        self.area_rolagem.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.area_rolagem.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )

        # Coloca a descrição dentro da área rolável
        self.area_rolagem.setWidget(self.descricao_inicio)

        self.area_rolagem.setStyleSheet("""
            QScrollArea {
                background-color: #1a2838;
                border: none;
            }
        """)

        self.descricao_inicio.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: white;
                background-color: transparent;
                padding: 10px;
            }
        """)

        # Layout da página inicial
        layout_inicio.setContentsMargins(25, 20, 25, 20)
        layout_inicio.setSpacing(15)

        layout_inicio.addWidget(titulo_inicio)
        layout_inicio.addWidget(self.area_rolagem, 1)

        # Tela de produtos
        self.pagina_produtos = ProdutosWindow()

        # Tela de estoque de produtos
        self.pagina_estoque = EstoqueWindow()

        # Tela de compras
        self.pagina_compras = ComprasWindow()

        # Tela de vendas
        self.pagina_vendas = VendasWindow()

        # Tela de movimentações
        self.pagina_movimentacoes = MovimentacoesWindow()

        # Adicionando todas as páginas à área central
        self.paginas.addWidget(self.pagina_inicio)
        self.paginas.addWidget(self.pagina_produtos)
        self.paginas.addWidget(self.pagina_estoque)
        self.paginas.addWidget(self.pagina_compras)
        self.paginas.addWidget(self.pagina_vendas)
        self.paginas.addWidget(self.pagina_movimentacoes)

        # ==================================
        # MENU LATERAL
        # ==================================

        menu = QVBoxLayout()
        menu.setSpacing(10)

        titulo_menu = QLabel("☰")
        titulo_menu.setStyleSheet(
            "font-size: 20px; color: white;"
        )

        menu.addWidget(titulo_menu)
        menu.addSpacing(20)

        self.botao_inicio = QPushButton("Início")
        self.botao_produtos = QPushButton("Produtos")
        self.botao_estoque = QPushButton("Estoque")
        self.botao_compras = QPushButton("Compras")
        self.botao_vendas = QPushButton("Vendas")
        self.botao_movimentacoes = QPushButton("Movimentações")

        # Associando cada botão à sua página
        botoes_paginas = [
            (self.botao_inicio, self.pagina_inicio),
            (self.botao_produtos, self.pagina_produtos),
            (self.botao_estoque, self.pagina_estoque),
            (self.botao_compras, self.pagina_compras),
            (self.botao_vendas, self.pagina_vendas),
            (self.botao_movimentacoes, self.pagina_movimentacoes),
        ]

        for botao, pagina in botoes_paginas:
            botao.setCursor(Qt.CursorShape.PointingHandCursor)
            botao.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed
            )
            botao.setMinimumHeight(40)

            botao.clicked.connect(
                lambda checked=False, b=botao, p=pagina:
                self.selecionar_pagina(b, p)
            )

            menu.addWidget(botao)

        menu.addStretch()

        # ==================================
        # ORGANIZAÇÃO PRINCIPAL
        # ==================================

        menu_widget = QWidget()
        menu_widget.setLayout(menu)
        menu_widget.setFixedWidth(200)

        menu_widget.setStyleSheet("""
            QWidget {
                background-color: #1a2838;
            }

            QPushButton {
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px;
                text-align: left;
                font-size: 18px;
            }

            QPushButton:hover {
                background-color: #46627f;
            }
        """)

        self.paginas.setStyleSheet("""
            QStackedWidget {
                background-color: #243447;
            }

            QLabel {
                color: #fff;
            }
        """)

        layout_principal = QHBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        layout_principal.addWidget(menu_widget)
        layout_principal.addWidget(self.paginas)

        self.setLayout(layout_principal)

    # ==================================
    # CRIAR PÁGINAS TEMPORÁRIAS
    # ==================================

    def criar_pagina(self, titulo, descricao):
        pagina = QWidget()
        layout = QVBoxLayout(pagina)

        titulo_label = QLabel(titulo)
        titulo_label.setStyleSheet(
            "font-size: 24px; font-weight: bold;"
        )

        descricao_label = QLabel(descricao)

        layout.addWidget(titulo_label)
        layout.addWidget(descricao_label)
        layout.addStretch()

        return pagina

    def selecionar_pagina(self, botao, pagina):
        self.paginas.setCurrentWidget(pagina)

        botoes = [
            self.botao_inicio,
            self.botao_produtos,
            self.botao_estoque,
            self.botao_compras,
            self.botao_vendas,
            self.botao_movimentacoes,
        ]

        for item in botoes:
            item.setStyleSheet("")

        botao.setStyleSheet("""
            QPushButton {
                background-color: #4c6f91;
                color: white;
                border-left: 4px solid #60a5fa;
                font-weight: bold;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
