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
    QCheckBox,
    QLineEdit,
)

from app.schemas import movimentacoes as movimentacao_schema
from app.services import movimentacoes_service, produto_service


class MovimentacoesWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(750, 500)

        titulo = QLabel("MOVIMENTAÇÕES")
        titulo.setStyleSheet("font-size: 22px; font-weight: bold;")

        subtitulo = QLabel(
            "Registre entradas e saídas de dinheiro ou de produtos."
        )

        # Tipo de movimentação
        self.tipo_input = QComboBox()
        self.tipo_input.addItems(["Entrada", "Saída"])

        # Opção de movimentação apenas financeira
        self.financeira_input = QCheckBox(
            "Movimentação financeira sem produto"
        )
        self.financeira_input.toggled.connect(
            self.alternar_movimentacao_financeira
        )

        # Produto
        self.produto_input = QComboBox()

        # Quantidade de produtos
        self.quantidade_input = QDoubleSpinBox()
        self.quantidade_input.setRange(0.001, 999.999)
        self.quantidade_input.setDecimals(3)
        self.quantidade_input.setValue(1.000)

        # Valor da movimentação
        self.valor_input = QDoubleSpinBox()
        self.valor_input.setRange(0.00, 999.99)
        self.valor_input.setDecimals(2)
        self.valor_input.setPrefix("R$ ")
        self.valor_input.setValue(0.00)

        # Descrição
        self.descricao_input = QLineEdit()
        self.descricao_input.setPlaceholderText(
            "Ex.: aluguel, internet, perda de produto..."
        )

        # Data
        self.data_input = QDateEdit()
        self.data_input.setCalendarPopup(True)
        self.data_input.setDisplayFormat("dd/MM/yyyy")
        self.data_input.setDate(QDate.currentDate())

        # Formulário
        formulario = QFormLayout()
        formulario.addRow("Tipo:", self.tipo_input)
        formulario.addRow("", self.financeira_input)
        formulario.addRow("Produto:", self.produto_input)
        formulario.addRow("Quantidade:", self.quantidade_input)
        formulario.addRow("Valor:", self.valor_input)
        formulario.addRow("Descrição:", self.descricao_input)
        formulario.addRow("Data:", self.data_input)

        # Botões
        self.registrar_button = QPushButton("Registrar movimentação")
        self.atualizar_button = QPushButton("Atualizar lista")
        self.cancelar_button = QPushButton("Cancelar movimentação")

        self.registrar_button.clicked.connect(
            self.registrar_movimentacao
        )
        self.atualizar_button.clicked.connect(self.atualizar_tela)
        self.cancelar_button.clicked.connect(
            self.cancelar_movimentacao
        )

        botoes = QHBoxLayout()
        botoes.addWidget(self.registrar_button)
        botoes.addWidget(self.atualizar_button)
        botoes.addWidget(self.cancelar_button)

        # Tabela de movimentações
        self.tabela = QTableWidget()
        self.tabela.setColumnCount(7)
        self.tabela.setHorizontalHeaderLabels([
            "ID",
            "Tipo",
            "Produto",
            "Quantidade",
            "Valor",
            "Descrição",
            "Data",
        ])
        self.tabela.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )
        self.tabela.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )
        self.tabela.setSelectionMode(
            QTableWidget.SelectionMode.SingleSelection
        )
        self.tabela.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)
        layout.addLayout(formulario)
        layout.addLayout(botoes)
        layout.addWidget(self.tabela)

        self.setLayout(layout)

        self.atualizar_tela()

    def alternar_movimentacao_financeira(self, marcada):
        """
        Quando marcada, a movimentação não terá produto
        nem quantidade e não alterará o estoque.
        """
        self.produto_input.setEnabled(not marcada)
        self.quantidade_input.setEnabled(not marcada)

        if marcada:
            self.produto_input.setCurrentIndex(-1)

    def carregar_produtos(self):
        produtos = produto_service.listar_produtos()

        self.produto_input.clear()

        produtos_ativos = [
            produto for produto in produtos if produto.ativo
        ]

        for produto in produtos_ativos:
            self.produto_input.addItem(
                produto.nome,
                produto.id
            )

        if not produtos_ativos:
            self.produto_input.addItem(
                "Nenhum produto ativo cadastrado",
                None
            )

        if self.financeira_input.isChecked():
            self.produto_input.setEnabled(False)
        else:
            self.produto_input.setEnabled(bool(produtos_ativos))

        self.registrar_button.setEnabled(
            bool(produtos_ativos)
            or self.financeira_input.isChecked()
        )

    def atualizar_tela(self):
        try:
            self.carregar_produtos()
            self.carregar_movimentacoes()
        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível atualizar a tela:\n{erro}"
            )

    def registrar_movimentacao(self):
        financeira = self.financeira_input.isChecked()
        produto_id = None
        quantidade = None

        if not financeira:
            produto_id = self.produto_input.currentData()

            if produto_id is None:
                QMessageBox.warning(
                    self,
                    "Atenção",
                    "Selecione um produto para movimentar o estoque."
                )
                return

            quantidade = self.quantidade_input.value()

        descricao = self.descricao_input.text().strip()

        if not descricao:
            QMessageBox.warning(
                self,
                "Atenção",
                "Informe uma descrição para a movimentação."
            )
            return

        try:
            movimentacao = movimentacao_schema.MovimentacaoCreate(
                tipo=self.tipo_input.currentText(),
                produto_id=produto_id,
                quantidade=quantidade,
                valor=self.valor_input.value(),
                descricao=descricao,
                data=date.fromisoformat(
                    self.data_input.date().toString("yyyy-MM-dd")
                ),
            )

            movimentacoes_service.registrar_movimentacao(
                movimentacao
            )

            self.carregar_movimentacoes()

            self.quantidade_input.setValue(1.000)
            self.valor_input.setValue(0.00)
            self.descricao_input.clear()
            self.data_input.setDate(QDate.currentDate())

            QMessageBox.information(
                self,
                "Sucesso",
                "Movimentação registrada com sucesso!"
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
                f"Erro ao registrar movimentação:\n{erro}"
            )

    def carregar_movimentacoes(self):
        movimentacoes = (
            movimentacoes_service.listar_movimentacoes()
        )

        self.tabela.setRowCount(0)

        for movimentacao in movimentacoes:
            linha = self.tabela.rowCount()
            self.tabela.insertRow(linha)

            produto = getattr(movimentacao, "produto", None)

            if produto is None:
                nome_produto = "Financeira"
            else:
                nome_produto = produto.nome

            quantidade = movimentacao.quantidade

            if quantidade is None:
                quantidade_texto = "—"
            else:
                quantidade_texto = f"{quantidade:.3f}"

            valor = float(movimentacao.valor)

            data_movimentacao = movimentacao.data
            if hasattr(data_movimentacao, "strftime"):
                data_texto = data_movimentacao.strftime("%d/%m/%Y")
            else:
                data_texto = str(data_movimentacao)

            valores = [
                str(movimentacao.id),
                movimentacao.tipo,
                nome_produto,
                quantidade_texto,
                f"R$ {valor:.2f}",
                movimentacao.descricao or "",
                data_texto,
            ]

            for coluna, valor_celula in enumerate(valores):
                self.tabela.setItem(
                    linha,
                    coluna,
                    QTableWidgetItem(valor_celula)
                )

    def cancelar_movimentacao(self):
        linha = self.tabela.currentRow()

        if linha < 0:
            QMessageBox.warning(
                self,
                "Atenção",
                "Selecione uma movimentação na tabela."
            )
            return

        id_item = self.tabela.item(linha, 0)

        if id_item is None:
            return

        movimentacao_id = int(id_item.text())

        resposta = QMessageBox.question(
            self,
            "Confirmar cancelamento",
            f"Deseja cancelar a movimentação "
            f"ID {movimentacao_id}?",
            QMessageBox.StandardButton.Yes
            | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No,
        )

        if resposta != QMessageBox.StandardButton.Yes:
            return

        try:
            movimentacoes_service.cancelar_movimentacao(
                movimentacao_id
            )

            self.carregar_movimentacoes()

            QMessageBox.information(
                self,
                "Sucesso",
                "Movimentação cancelada com sucesso!"
            )

        except (ValueError, TypeError) as erro:
            QMessageBox.warning(
                self,
                "Não foi possível cancelar",
                str(erro)
            )
        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Erro ao cancelar movimentação:\n{erro}"
            )
