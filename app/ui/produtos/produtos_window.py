# IMPORTANDO MODULOS
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QFormLayout,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox
)
import sys
from app.schemas import produto as produto_schema
from app.services import produto_service

# CRIANDO JANELA
class ProdutosWindow(QWidget):
    # METODO CONTRUTOR
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Produtos")
        self.setMinimumSize(500, 400)

        # -------------------------
        # CAMPOS
        # -------------------------

        self.nome_input = QLineEdit()
        self.nome_input.setPlaceholderText("Digite o nome do produto")

        self.categoria_input = QLineEdit()
        self.categoria_input.setPlaceholderText("Digite a categoria")

        self.unidade_input = QComboBox()
        self.unidade_input.addItems(["UN", "KG"])

        # -------------------------
        # BOTÕES
        # -------------------------

        self.cadastrar_button = QPushButton("Cadastrar Produto")
        self.editar_button = QPushButton("Editar Produto")
        self.ativar_button = QPushButton("Ativar/Desativar")

        self.cadastrar_button.clicked.connect(
            self.cadastrar_produto
        )

        self.editar_button.clicked.connect(
            self.editar_produto
        )

        self.ativar_button.clicked.connect(
            self.ativar_desativar_produto
        )

        # -------------------------
        # TABELA
        # -------------------------

        self.tabela_produtos = QTableWidget()
        self.tabela_produtos.setColumnCount(5)
        self.tabela_produtos.setHorizontalHeaderLabels([
            "ID",
            "Produto",
            "Categoria",
            "Unidade",
            "Status"
        ])
        self.tabela_produtos.cellClicked.connect(
            self.selecionar_produto
        )

        # -------------------------
        # FORMULÁRIO
        # -------------------------

        formulario = QFormLayout()

        formulario.addRow("Nome:", self.nome_input)
        formulario.addRow("Categoria:", self.categoria_input)
        formulario.addRow("Unidade:", self.unidade_input)

        # -------------------------
        # LAYOUT PRINCIPAL
        # -------------------------

        layout = QVBoxLayout()

        titulo = QLabel("GERENCIAR PRODUTOS")

        layout.addWidget(titulo)
        layout.addLayout(formulario)
        layout.addWidget(self.cadastrar_button)
        layout.addWidget(self.editar_button)
        layout.addWidget(self.ativar_button)
        layout.addWidget(self.tabela_produtos)

        self.setLayout(layout)
        self.carregar_produtos()

    # METODO PARA CADASTRAR PRODUTOS
    def cadastrar_produto(self):
      nome = self.nome_input.text()
      categoria = self.categoria_input.text()
      unidade = self.unidade_input.currentText()

      if not nome:
        QMessageBox.warning(
            self,
            "Atenção",
            "Informe o nome do produto."
        )
        return

      produto = produto_schema.ProdutoCreate(
          nome=nome,
          categoria=categoria,
          unidade_gerenciamento=unidade,
          ativo=True
      )

      produto_service.cadastrar_produto(produto)

      self.carregar_produtos()

      self.nome_input.clear()
      self.categoria_input.clear()
      self.unidade_input.setCurrentIndex(0)

      QMessageBox.information(
          self,
          "Sucesso",
          "Produto cadastrado com sucesso!"
      )

    # METODO PARA BUSCAR TODOS OS PRODUTOS
    def carregar_produtos(self):

      produtos = produto_service.listar_produtos()

      self.tabela_produtos.setRowCount(len(produtos))

      for linha, produto in enumerate(produtos):

          self.tabela_produtos.setItem(
              linha,
              0,
              QTableWidgetItem(str(produto.id))
          )

          self.tabela_produtos.setItem(
              linha,
              1,
              QTableWidgetItem(produto.nome)
          )

          self.tabela_produtos.setItem(
              linha,
              2,
              QTableWidgetItem(produto.categoria)
          )

          self.tabela_produtos.setItem(
              linha,
              3,
              QTableWidgetItem(produto.unidade_gerenciamento)
          )

          status = "Ativo" if produto.ativo else "Inativo"

          self.tabela_produtos.setItem(
              linha,
              4,
              QTableWidgetItem(status)
          )

    # EDITAR PRODUTO
    def editar_produto(self):

      linha = self.tabela_produtos.currentRow()

      if linha == -1:
          QMessageBox.warning(
              self,
              "Atenção",
              "Selecione um produto na tabela."
          )
          return

      id_produto = int(
          self.tabela_produtos.item(linha, 0).text()
      )

      nome = self.nome_input.text()
      categoria = self.categoria_input.text()
      unidade = self.unidade_input.currentText()

      produto_editado = produto_schema.ProdutoCreate(
          nome=nome,
          categoria=categoria,
          unidade_gerenciamento=unidade,
          ativo=True
      )

      produto_service.editar_produto(
          id_produto,
          produto_editado
      )

      self.carregar_produtos()

      self.nome_input.clear()
      self.categoria_input.clear()

      QMessageBox.information(
          self,
          "Sucesso",
          "Produto editado com sucesso!"
      )

    # ATIVANDO E DESATIVANDO PRODUTOS
    def ativar_desativar_produto(self):
       
      linha = self.tabela_produtos.currentRow()

      if linha == -1:
          QMessageBox.warning(
              self,
              "Atenção",
              "Selecione um produto na tabela."
          )
          return

      id_produto = int(
          self.tabela_produtos.item(linha, 0).text()
      )

      produto_service.ativar_desativar_produtos(id_produto)
      
      self.carregar_produtos()

      self.nome_input.clear()
      self.categoria_input.clear()

      QMessageBox.information(
          self,
          "Sucesso",
          "Status do produto alterado!"
      )

    # SELECINANDO ITEM DA TABELA
    def selecionar_produto(self, linha, coluna):

      nome = self.tabela_produtos.item(linha, 1).text()
      categoria = self.tabela_produtos.item(linha, 2).text()
      unidade = self.tabela_produtos.item(linha, 3).text()

      self.nome_input.setText(nome)
      self.categoria_input.setText(categoria)

      indice = self.unidade_input.findText(unidade)

      if indice != -1:
          self.unidade_input.setCurrentIndex(indice)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = ProdutosWindow()
    window.show()

    sys.exit(app.exec())
