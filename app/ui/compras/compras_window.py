# IMPORTANDO MODULOS

from datetime import date

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
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

from app.schemas import compra as compra_schema
from app.services import compra_service, produto_service


class ComprasWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setMinimumSize(650, 450)

        # Título
        titulo = QLabel("GERENCIAR COMPRAS")
        titulo.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        # Formulário
        self.fornecedor_input = QLineEdit()
        self.fornecedor_input.setPlaceholderText(
            "Nome do fornecedor (opcional)"
        )

        self.produto_input = QComboBox()

        self.quantidade_input = QDoubleSpinBox()
        self.quantidade_input.setRange(0.001, 999.999)
        self.quantidade_input.setDecimals(3)
        self.quantidade_input.setValue(1.000)

        self.valor_input = QDoubleSpinBox()
        self.valor_input.setRange(0.01, 999.99)
        self.valor_input.setDecimals(2)
        self.valor_input.setPrefix("R$ ")
        self.valor_input.setValue(1.00)

        self.data_input = QDateEdit()
        self.data_input.setCalendarPopup(True)
        self.data_input.setDisplayFormat("dd/MM/yyyy")
        self.data_input.setDate(QDate.currentDate())

        formulario = QFormLayout()
        formulario.addRow("Fornecedor:", self.fornecedor_input)
        formulario.addRow("Produto:", self.produto_input)
        formulario.addRow("Quantidade:", self.quantidade_input)
        formulario.addRow("Valor total:", self.valor_input)
        formulario.addRow("Data da compra:", self.data_input)

        # Botões
        self.registrar_button = QPushButton("Registrar compra")
        self.atualizar_button = QPushButton("Atualizar lista")
        self.cancelar_button = QPushButton("Cancelar compra")

        self.registrar_button.clicked.connect(
            self.registrar_compra
        )
        self.atualizar_button.clicked.connect(
            self.carregar_compras
        )
        self.cancelar_button.clicked.connect(
            self.cancelar_compra
        )

        botoes = QHBoxLayout()
        botoes.addWidget(self.registrar_button)
        botoes.addWidget(self.atualizar_button)
        botoes.addWidget(self.cancelar_button)

        # Tabela de compras
        self.tabela_compras = QTableWidget()
        self.tabela_compras.setColumnCount(6)
        self.tabela_compras.setHorizontalHeaderLabels([
            "ID",
            "Fornecedor",
            "Produto",
            "Quantidade",
            "Valor total",
            "Data",
        ])

        self.tabela_compras.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tabela_compras.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.tabela_compras.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )
        self.tabela_compras.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addLayout(formulario)
        layout.addLayout(botoes)
        layout.addWidget(self.tabela_compras)

        self.setLayout(layout)

        # Carregar dados
        self.carregar_produtos()
        self.carregar_compras()

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

            self.registrar_button.setEnabled(
                self.produto_input.count() > 0
            )

            if self.produto_input.count() == 0:
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

    def registrar_compra(self):
        try:
            produto_id = self.produto_input.currentData()

            if produto_id is None:
                QMessageBox.warning(
                    self,
                    "Atenção",
                    "Cadastre ou ative um produto antes de registrar uma compra."
                )
                return

            compra = compra_schema.CompraCreate(
                fornecedor=self.fornecedor_input.text().strip() or None,
                produto_id=produto_id,
                quantidade=self.quantidade_input.value(),
                valor=self.valor_input.value(),
                data=date.fromisoformat(
                    self.data_input.date().toString("yyyy-MM-dd")
                )
            )

            compra_service.registrar_compra(compra)

            self.carregar_compras()
            self.fornecedor_input.clear()
            self.quantidade_input.setValue(1.000)
            self.valor_input.setValue(1.00)
            self.data_input.setDate(QDate.currentDate())

            QMessageBox.information(
                self,
                "Sucesso",
                "Compra registrada com sucesso!"
            )

        except (ValueError, TypeError) as erro:
            QMessageBox.warning(
                self,
                "Dados inválidos",
                str(erro)
            )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível registrar a compra:\n{erro}"
            )

    def carregar_compras(self):
        try:
            compras = compra_service.listar_compras()

            self.tabela_compras.setRowCount(len(compras))

            for linha, compra in enumerate(compras):
                fornecedor = compra.fornecedor or "Não informado"
                produto = compra.produto.nome

                valores = [
                    str(compra.id),
                    fornecedor,
                    produto,
                    f"{compra.quantidade:.3f}",
                    f"R$ {compra.valor:.2f}",
                    compra.data.strftime("%d/%m/%Y"),
                ]

                for coluna, valor in enumerate(valores):
                    self.tabela_compras.setItem(
                        linha,
                        coluna,
                        QTableWidgetItem(valor)
                    )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível carregar as compras:\n{erro}"
            )

    def cancelar_compra(self):
        linha = self.tabela_compras.currentRow()

        if linha == -1:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma compra na tabela."
            )
            return

        compra_id = int(
            self.tabela_compras.item(linha, 0).text()
        )

        resposta = QMessageBox.question(
            self,
            "Confirmar cancelamento",
            f"Deseja realmente cancelar a compra de ID {compra_id}?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if resposta != QMessageBox.StandardButton.Yes:
            return

        try:
            compra_service.cancelar_compra(compra_id)
            self.carregar_compras()

            QMessageBox.information(
                self,
                "Sucesso",
                "Compra cancelada com sucesso!"
            )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível cancelar a compra:\n{erro}"
            )
