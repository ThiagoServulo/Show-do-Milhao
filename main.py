from PySide2 import QtWidgets
import sys
from ui_tela_inicio_jogo import CriarTelaInicioDeJogo

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_login = CriarTelaInicioDeJogo()
    window_login.show()
    sys.exit(app.exec_())
