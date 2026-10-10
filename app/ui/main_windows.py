# IMPORTANDO MODULOS

import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QSizePolicy
)

from app.ui.produtos.produtos_window import ProdutosWindow
from app.ui.estoque.estoque_window import EstoqueWindow


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Gestão - Sorveteria")
        self.setMinimumSize(900, 600)

        # ==================================
        # ÁREA DE CONTEÚDO
        # ==================================

        self.paginas = QStackedWidget()

        # Página inicial
        self.pagina_inicio = QWidget()
        layout_inicio = QVBoxLayout(self.pagina_inicio)

        titulo_inicio = QLabel("Bem-vindo ao Sistema de Gestão")
        titulo_inicio.setStyleSheet(
            "font-size: 24px; font-weight: bold;"
        )

        descricao_inicio = QLabel(
            "Selecione um módulo no menu lateral para começar."
        )

        layout_inicio.addWidget(titulo_inicio)
        layout_inicio.addWidget(descricao_inicio)
        layout_inicio.addStretch()

        # Tela de produtos
        self.pagina_produtos = ProdutosWindow()

        # Tela de estoque de produtos
        self.pagina_estoque = EstoqueWindow()

        self.pagina_compras = self.criar_pagina(
            "Compras",
            "Aqui ficará o registro de compras e reposições."
        )

        self.pagina_vendas = self.criar_pagina(
            "Vendas",
            "Aqui ficará o registro de vendas."
        )

        self.pagina_movimentacoes = self.criar_pagina(
            "Movimentações",
            "Aqui ficarão as entradas e saídas."
        )

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

        titulo_menu = QLabel("MENU")
        titulo_menu.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: white;"
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
            botao.setCursor(__import__("PySide6.QtCore", fromlist=["Qt"]).Qt.CursorShape.PointingHandCursor)
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
                background-color: #243447;
            }

            QPushButton {
                background-color: #34495e;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px;
                text-align: left;
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
