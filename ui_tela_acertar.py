from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
import sys


class Ui_tela_acertar(object):
    def setupUi(self, tela_acertar):
        if not tela_acertar.objectName():
            tela_acertar.setObjectName(u"tela_acertar")
        tela_acertar.setWindowTitle(u"Show do Milhão")
        tela_acertar.resize(371, 161)
        tela_acertar.setMaximumSize(371, 161)
        tela_acertar.setMinimumSize(371, 161)
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_acertar.setWindowIcon(icon)
        tela_acertar.setStyleSheet(u"background-color: rgb(0, 0, 121);")
        self.centralwidget = QWidget(tela_acertar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 331, 121))
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
        self.label.setText(u"Você acertou !")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.barra_progresso = QProgressBar(self.groupBox)
        self.barra_progresso.setObjectName(u"barra_progresso")
        self.barra_progresso.setGeometry(QRect(70, 80, 211, 23))
        self.barra_progresso.setFont(font)
        self.barra_progresso.setValue(0)
        self.barra_progresso.setMaximum(5)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 311, 20))
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setText(u"Carregando próxima pergunta")
        self.label_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        tela_acertar.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(tela_acertar)
    # setupUi


class CriarTelaAcertar(QtWidgets.QMainWindow, Ui_tela_acertar):
    def __init__(self):
        super(CriarTelaAcertar, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        sys.exit()
