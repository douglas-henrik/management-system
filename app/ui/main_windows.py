
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

        if getattr(sys, "frozen", False):
            pasta_base = Path(sys._MEIPASS)
        else:
            pasta_base = Path(__file__).resolve().parents[2]

        caminho_icone = pasta_base / "assets" / "icon.png"
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
            vendas e movimentações financeiras (NÃO IMPLEMENTADO).

                COMO ULTILIZAR O SISTEMA

                1. PRODUTOS
                
            Cadastre os produtos comercializados pela empresa, preenchendo os campos solicitados: nome do produto,
            categoria e unidade de gerenciamento (UN ou KG). Após preencher os dados, selecione (Cadastrar Produto)
            para concluir o cadastro.

            Editar produto: para modificar um produto existente, selecione-o na tabela, altere os dados desejados e
            clique em (Editar Produto).

            Ativar/Desativar produto: selecione o produto desejado na tabela e clique em (Ativar/Desativar) para
            alterar seu status.

            Observação: produtos desativados não podem ser utilizados em operações de venda ou em movimentações de
            saída de estoque.

                2. COMPRAS

            Registre as compras e reposições de produtos realizadas pela empresa, preenchendo os campos solicitados,
            como produto, fornecedor, quantidade, valor e data da compra. Após preencher os dados, selecione a opção
            (Registrar Compra) para concluir a operação.

            Atualizar lista: selecionar a opção (Atualizar lista), busca alterações resgistradas e atualiza na
            tabela.

            Cancelar compra: selecione a compra que deseja cancelar e clique em (Cancelar compra) para remove-la da
            tabela.

            ATENÇÃO: compras registradas e compras canceladas de um deteminado produto, interferem no resultado do
            estoque atual do mesmo.

                3. VENDAS

            Registre as vendas realizadas pela empresa, preenchendo os campos solicitados, como produto, quantidade,
            valor, forma de pagamento e data da venda. Após preencher os dados, selecione (Registrar Venda) para concluir
            a operação.

            Atualizar lista: selecionar a opção (Atualizar lista), busca alterações resgistradas e atualiza na tabela.

            Cancelar venda: selecione a venda que deseja cancelar e clique em (Cancelar venda) para remove-la da tabela.

            Observação: somente produtos ativos podem ser utilizados nas vendas. Antes de registrar a operação, confira os
            dados informados e verifique se há estoque disponível para atender à quantidade vendida.

            ATENÇÃO: vendas registradas e vendas canceladas de um deteminado produto, interferem no resultado do estoque
            atual do mesmo.

                4. ESTOQUE

            Consulte o estoque atual dos produtos cadastrados na empresa, acompanhando as quantidades disponíveis para
            comercialização. As informações são atualizadas conforme as compras, vendas e movimentações de estoque
            registradas no sistema.

            Atualizar lista: selecione (Atualizar lista) quando houver modificações feitas, assim a tabela será atualizada.

            Observação: o estoque é calculado com base nas entradas e saídas registradas no sistema. Para manter as
            informações atualizadas, registre corretamente todas as compras, vendas e movimentações que alterem as
            quantidades dos produtos.

                5. MOVIMENTAÇÕES

            Registre as entradas e saídas financeiras da empresa, bem como as movimentações de produtos que não estejam
            relacionadas a uma venda. Preencha os campos solicitados de acordo com o tipo de movimentação, incluindo tipo,
            produto (quando aplicável), quantidade (quando aplicável), valor, descrição e data. Após preencher os dados,
            selecione (Registrar Movimentação) para concluir a operação.

            Movimentações financeiras: utilize esta funcionalidade para registrar entradas e saídas de dinheiro, contribuindo
            para o controle financeiro da empresa.

            Movimentações de estoque: registre entradas ou saídas de produtos quando necessário, como no recebimento de itens
            ou na retirada de produtos para consumo interno, perdas ou brindes.

            Atualizar lista: selecionar a opção (Atualizar lista), busca alterações resgistradas e atualiza na tabela.

            Cancelar movimentação: selecione a movimentação que deseja cancelar e clique em (Cancelar movimentação) para
            remove-la da tabela. 

            ATENÇÃO: movimentações que envolvem produtos podem alterar automaticamente o estoque. Confira o tipo de operação,
            a quantidade e os demais dados antes de registrar.

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
                background-color: #FFFFFF;
                border: none;
            }
        """)

        self.descricao_inicio.setStyleSheet("""
            QLabel {
                font-size: 16px;
                color: #0F172A;
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
                background-color: #0F172A;
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
                background-color: #2563EB;
            }
        """)

        self.paginas.setStyleSheet("""
            QStackedWidget {
                background-color: #F8FAFC;
            }

            QPushButton {
                background-color: #2563EB;
            }

            QPushButton:hover {
                background-color: #1D4ED8;
            }

            QLineEdit, QDoubleSpinBox, QDateEdit {
                background-color: #FFFFFF;
                color: #1E293B;
            }

            QComboBox {
                background-color: #FFFFFF;
                color: #1E293B;
                border: 1px solid #CBD5E1;
                border-radius: 6px;
                padding: 6px;
            }

            QComboBox QAbstractItemView {
                background-color: #FFFFFF;
                color: #1E293B;
                selection-background-color: #DBEAFE;
                selection-color: #0F172A;
            }

            QCheckBox {
                color: #1E293B;
                spacing: 8px;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                background-color: #FFFFFF;
                border: 1px solid #94A3B8;
                border-radius: 4px;
            }

            QCheckBox::indicator:hover {
                border: 1px solid #2563EB;
            }

            QCheckBox::indicator:checked {
                background-color: #2563EB;
                border: 1px solid #2563EB;
            }

            QCheckBox::indicator:unchecked {
                background-color: #FFFFFF;
            }
     
            /* Campos desabilitados */
            QComboBox:disabled,
            QLineEdit:disabled,
            QSpinBox:disabled,
            QDoubleSpinBox:disabled,
            QDateEdit:disabled {
                background-color: #E2E8F0;
                color: #64748B;
                border: 1px solid #CBD5E1;
            }

            /* Checkbox desabilitado */
            QCheckBox:disabled {
                color: #94A3B8;
            }

            QCheckBox::indicator:disabled {
                background-color: #E2E8F0;
                border: 1px solid #CBD5E1;
            }
       
            QMessageBox {
                background-color: #F8FAFC;
                color: #1E293B;
            }

            QMessageBox QLabel {
                color: #1E293B;
                background-color: transparent;
                font-size: 14px;
            }

            QMessageBox QPushButton {
                background-color: #2563EB;
                color: #FFFFFF;
                border: none;
                border-radius: 5px;
                padding: 7px 16px;
                min-width: 70px;
            }

            QMessageBox QPushButton:hover {
                background-color: #1D4ED8;
            }

            QLabel {
                color: #0F172A;
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
                background-color: #2563EB;
                color: white;
                border-left: 4px solid #93C5FD;
                font-weight: bold;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
