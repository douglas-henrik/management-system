# IMPORTANDO MODULOS
import sys

from PySide6.QtWidgets import QApplication

from app.database.connection import Base, engine
from app.ui.main_windows import MainWindow

# INICIANDO BANCO DE DADOS
def iniciar_banco():
    # Importa os modelos para registrar todas as tabelas
    from app.models import Produto
    from app.models import Compra
    from app.models import Venda
    from app.models import Movimentacao

    Base.metadata.create_all(bind=engine)

# FUNÇÃO PRINCIPAL
def main():
    iniciar_banco()

    app = QApplication(sys.argv)

    janela = MainWindow()
    janela.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()