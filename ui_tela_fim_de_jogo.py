from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys


class Ui_tela_fim_de_jogo(object):
    def setupUi(self, tela_fim_de_jogo):
        if not tela_fim_de_jogo.objectName():
            tela_fim_de_jogo.setObjectName(u"tela_fim_de_jogo")
        tela_fim_de_jogo.resize(371, 181)
        tela_fim_de_jogo.setMaximumSize(371, 181)
        tela_fim_de_jogo.setMinimumSize(371, 181)
        tela_fim_de_jogo.setWindowTitle(u"Show do Milhão")
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_fim_de_jogo.setWindowIcon(icon)
        tela_fim_de_jogo.setStyleSheet(u"background-color: rgb(0, 0, 121);")
        self.centralwidget = QWidget(tela_fim_de_jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 331, 141))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.groupBox.setTitle(u"")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 311, 20))
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setText(u"Fim de jogo !")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_premio = QLabel(self.groupBox)
        self.label_premio.setObjectName(u"label_premio")
        self.label_premio.setGeometry(QRect(30, 40, 271, 21))
        self.label_premio.setFont(font)
        self.label_premio.setLayoutDirection(Qt.LeftToRight)
        self.label_premio.setText(u"Você ganhou xxxxx")
        self.label_premio.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.botao_sair = QPushButton(self.groupBox)
        self.botao_sair.setObjectName(u"botao_sair")
        self.botao_sair.setGeometry(QRect(30, 80, 121, 41))
        self.botao_sair.setFont(font)
        self.botao_sair.setStyleSheet(u"background-color: rgb(0, 0, 121);")
        self.botao_sair.setText(u"Sair")
        self.botao_novo_jogo = QPushButton(self.groupBox)
        self.botao_novo_jogo.setObjectName(u"botao_novo_jogo")
        self.botao_novo_jogo.setGeometry(QRect(180, 80, 121, 41))
        self.botao_novo_jogo.setFont(font)
        self.botao_novo_jogo.setStyleSheet(u"background-color: rgb(0, 0, 121);")
        self.botao_novo_jogo.setText(u"Novo Jogo")
        self.barra_progresso = QProgressBar(self.groupBox)
        self.barra_progresso.setObjectName(u"barra_progresso")
        self.barra_progresso.setGeometry(QRect(40, 40, 261, 21))
        self.barra_progresso.setFont(font)
        self.barra_progresso.setValue(0)
        self.barra_progresso.raise_()
        self.label_premio.raise_()
        self.label.raise_()
        self.botao_sair.raise_()
        self.botao_novo_jogo.raise_()
        tela_fim_de_jogo.setCentralWidget(self.centralwidget)

        self.botao_sair.clicked.connect(self.fechar_jogo)

        QMetaObject.connectSlotsByName(tela_fim_de_jogo)
    # setupUi

    def fechar_jogo(self):
        sys.exit()
    # fechar_jogo


class CriarTelaFimDeJogo(QtWidgets.QMainWindow, Ui_tela_fim_de_jogo):
    def __init__(self):
        super(CriarTelaFimDeJogo, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        sys.exit()
