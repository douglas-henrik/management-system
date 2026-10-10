# IMPORTANDO MODULOS

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QHeaderView
)

from app.services import estoque_service


class EstoqueWindow(QWidget):

    def __init__(self):
        super().__init__()

        # Título
        titulo = QLabel("CONSULTA DE ESTOQUE")
        titulo.setStyleSheet(
            "font-size: 22px; font-weight: bold;"
        )

        # Botão de atualização
        self.atualizar_button = QPushButton("Atualizar estoque")
        self.atualizar_button.clicked.connect(
            self.carregar_estoque
        )

        # Tabela
        self.tabela_estoque = QTableWidget()
        self.tabela_estoque.setColumnCount(4)

        self.tabela_estoque.setHorizontalHeaderLabels([
            "ID",
            "Produto",
            "Unidade",
            "Estoque atual"
        ])

        self.tabela_estoque.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )

        self.tabela_estoque.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )

        self.tabela_estoque.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        # Layout
        layout = QVBoxLayout()

        layout.addWidget(titulo)
        layout.addWidget(self.atualizar_button)
        layout.addWidget(self.tabela_estoque)

        self.setLayout(layout)

        # Carrega os dados ao abrir a página
        self.carregar_estoque()

    def carregar_estoque(self):
        try:
            estoque = estoque_service.listar_estoque()

            self.tabela_estoque.setRowCount(len(estoque))

            for linha, item in enumerate(estoque):

                quantidade = item["quantidade"]
                unidade = item["unidade"]

                # UN é exibida como número inteiro.
                # KG é exibido com três casas decimais.
                if unidade == "UN":
                    quantidade_formatada = f"{quantidade:.0f}"
                else:
                    quantidade_formatada = f"{quantidade:.3f}"

                valores = [
                    str(item["produto_id"]),
                    item["produto"],
                    unidade,
                    quantidade_formatada
                ]

                for coluna, valor in enumerate(valores):
                    celula = QTableWidgetItem(valor)
                    self.tabela_estoque.setItem(
                        linha,
                        coluna,
                        celula
                    )

        except Exception as erro:
            QMessageBox.critical(
                self,
                "Erro",
                f"Não foi possível carregar o estoque:\n{erro}"
            )
