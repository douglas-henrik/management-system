# IMPORTANDO MODULOS

from datetime import date

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QDoubleSpinBox,
    QDateEdit,
    QHeaderView,
)

from app.schemas import venda as venda_schema
from app.services import venda_service, produto_service


class VendasWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("""
            QPushButton {
                font-size: 16px;
                font-weight: bold;
                padding: 5px;
            }

            QLineEdit {
                padding: 7px;
                font-size: 14px;
            }

            QComboBox {
                padding: 7px;
                font-size: 14px;
            }

            QDoubleSpinBox {
                padding: 5px;
                font-size: 14px;
            }

            QDateEdit {
                padding: 5px;
                font-size: 14px;
            }
        """)

        # Título
        titulo = QLabel("REGISTRAR VENDAS")
        titulo.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        # Formulário
        self.produto_input = QComboBox()

        self.quantidade_input = QDoubleSpinBox()
        self.quantidade_input.setRange(0.001, 999.999)
        self.quantidade_input.setDecimals(3)
        self.quantidade_input.setValue(1.000)

        self.valor_input = QDoubleSpinBox()
        self.valor_input.setRange(0.01, 99999.99)
        self.valor_input.setDecimals(2)
        self.valor_input.setPrefix("R$ ")
        self.valor_input.setValue(1.00)

        self.pagamento_input = QComboBox()
        self.pagamento_input.addItems([
            "PIX",
            "Dinheiro",
            "Cartão Débito",
            "Cartão Crédito",
        ])

        self.data_input = QDateEdit()
        self.data_input.setCalendarPopup(True)
        self.data_input.setDisplayFormat("dd/MM/yyyy")
        self.data_input.setDate(QDate.currentDate())

        formulario = QFormLayout()
        formulario.addRow("Produto:", self.produto_input)
        formulario.addRow("Quantidade:", self.quantidade_input)
        formulario.addRow("Valor total:", self.valor_input)
        formulario.addRow("Forma de pagamento:", self.pagamento_input)
        formulario.addRow("Data da venda:", self.data_input)

        for campo in [
            self.produto_input,
            self.quantidade_input,
            self.valor_input,
            self.pagamento_input,
            self.data_input
        ]:
            rotulo = formulario.labelForField(campo)
            if rotulo:
                rotulo.setStyleSheet("font-size: 16px; font-weight: bold;")

        # Botões
        self.registrar_button = QPushButton("Registrar venda")
        self.atualizar_button = QPushButton("Atualizar lista")
        self.cancelar_button = QPushButton("Cancelar venda")

        self.registrar_button.clicked.connect(
            self.registrar_venda
        )
        self.atualizar_button.clicked.connect(
            self.carregar_vendas
        )
        self.cancelar_button.clicked.connect(
            self.cancelar_venda
        )

        botoes = QHBoxLayout()
        botoes.addWidget(self.registrar_button)
        botoes.addWidget(self.atualizar_button)
        botoes.addWidget(self.cancelar_button)

        # Tabela
        self.tabela_vendas = QTableWidget()
        self.tabela_vendas.setColumnCount(6)
        self.tabela_vendas.setHorizontalHeaderLabels([
            "ID",
            "Produto",
            "Quantidade",
            "Valor total",
            "Pagamento",
            "Data",
        ])

        # Aumentar o tamanho da fonte das células
        self.tabela_vendas.setStyleSheet("""
            QTableWidget {
                font-size: 14px;
            }

            QHeaderView::section {
                font-size: 14px;
                font-weight: bold;
                padding: 6px;
            }
        """)

        # Aumentar a altura das linhas
        self.tabela_vendas.verticalHeader().setDefaultSectionSize(35)

        # Aumentar a altura do cabeçalho
        self.tabela_vendas.horizontalHeader().setMinimumHeight(35)

        self.tabela_vendas.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tabela_vendas.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.tabela_vendas.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )
        self.tabela_vendas.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addLayout(formulario)
        layout.addLayout(botoes)
        layout.addWidget(self.tabela_vendas)

        self.setLayout(layout)

        self.carregar_produtos()
        self.carregar_vendas()

    def carregar_produtos(self):
        try:
            produtos = produto_service.listar_produtos()

            self.produto_input.clear()

            for produto in produtos:
                if produto.ativo:
                    self.produto_input.addItem(
                        produto.nome,
                        produto.id
                    )

            tem_produtos = self.produto_input.count() > 0

            self.registrar_button.setEnabled(tem_produtos)

            if not tem_produtos:
                self.produto_input.addItem(
                    "Nenhum produto ativo cadastrado",
                    None
                )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível carregar os produtos:\n{erro}"
            )

    def registrar_venda(self):
        try:
            produto_id = self.produto_input.currentData()

            if produto_id is None:
                QMessageBox.warning(
                    self,
                    "Atenção",
                    "Cadastre ou ative um produto antes de registrar uma venda."
                )
                return

            venda = venda_schema.VendaCreate(
                produto_id=produto_id,
                quantidade=self.quantidade_input.value(),
                valor=self.valor_input.value(),
                forma_pagamento=self.pagamento_input.currentText(),
                data=date.fromisoformat(
                    self.data_input.date().toString("yyyy-MM-dd")
                )
            )

            venda_service.registrar_venda(venda)

            self.carregar_vendas()
            self.quantidade_input.setValue(1.000)
            self.valor_input.setValue(1.00)
            self.data_input.setDate(QDate.currentDate())

            QMessageBox.information(
                self,
                "Sucesso",
                "Venda registrada com sucesso!"
            )

        except (ValueError, TypeError) as erro:
            QMessageBox.warning(
                self,
                "Não foi possível registrar",
                str(erro)
            )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível registrar a venda:\n{erro}"
            )

    def carregar_vendas(self):
        try:
            vendas = venda_service.listar_vendas()

            self.tabela_vendas.setRowCount(len(vendas))

            for linha, venda in enumerate(vendas):
                valores = [
                    str(venda.id),
                    venda.produto.nome,
                    f"{venda.quantidade:.3f}",
                    f"R$ {venda.valor:.2f}",
                    venda.forma_pagamento,
                    venda.data.strftime("%d/%m/%Y"),
                ]

                for coluna, valor in enumerate(valores):
                    self.tabela_vendas.setItem(
                        linha,
                        coluna,
                        QTableWidgetItem(valor)
                    )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível carregar as vendas:\n{erro}"
            )

    def cancelar_venda(self):
        linha = self.tabela_vendas.currentRow()

        if linha == -1:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma venda na tabela."
            )
            return

        venda_id = int(
            self.tabela_vendas.item(linha, 0).text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmar cancelamento",
            f"Deseja realmente cancelar a venda de ID {venda_id}?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if resposta != QMessageBox.StandardButton.Yes:
            return

        try:
            venda_service.cancelar_venda(venda_id)
            self.carregar_vendas()

            QMessageBox.information(
                self,
                "Sucesso",
                "Venda cancelada com sucesso!"
            )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível cancelar a venda:\n{erro}"
            )
