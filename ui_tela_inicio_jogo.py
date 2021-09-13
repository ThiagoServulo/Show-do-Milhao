from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from ui_tela_do_jogo import CriarTelaDoJogo
import sys


class Ui_tela_inicio_jogo(object):
    def setupUi(self, tela_inicio_jogo):
        if not tela_inicio_jogo.objectName():
            tela_inicio_jogo.setObjectName(u"tela_inicio_jogo")
        tela_inicio_jogo.resize(448, 260)
        tela_inicio_jogo.setMinimumSize(448, 260)
        tela_inicio_jogo.setMaximumSize(448, 260)
        tela_inicio_jogo.setStyleSheet(u"background-color: rgb(0, 54, 100);")
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_inicio_jogo.setWindowIcon(icon)
        self.centralwidget = QWidget(tela_inicio_jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 411, 151))
        self.label.setText(u"")
        self.label.setPixmap(QPixmap(u"logo.jpg"))
        self.botao_novo_jogo = QPushButton(self.centralwidget)
        self.botao_novo_jogo.setObjectName(u"botao_novo_jogo")
        self.botao_novo_jogo.setGeometry(QRect(240, 200, 191, 41))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botao_novo_jogo.setFont(font)
        self.botao_novo_jogo.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_novo_jogo.setText(u"Novo Jogo")
        self.botao_regras = QPushButton(self.centralwidget)
        self.botao_regras.setObjectName(u"botao_regras")
        self.botao_regras.setGeometry(QRect(10, 200, 191, 41))
        self.botao_regras.setFont(font)
        self.botao_regras.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_regras.setText(u"Regras")
        tela_inicio_jogo.setCentralWidget(self.centralwidget)

        self.tela_jogo = CriarTelaDoJogo()
        self.botao_novo_jogo.clicked.connect(self.novo_jogo)

        QMetaObject.connectSlotsByName(tela_inicio_jogo)
    # setupUi

    def novo_jogo(self):
        self.hide()
        self.tela_jogo.novo_jogo()
    # novo_jogo


class CriarTelaInicioDeJogo(QtWidgets.QMainWindow, Ui_tela_inicio_jogo):
    def __init__(self):
        super(CriarTelaInicioDeJogo, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        sys.exit()
