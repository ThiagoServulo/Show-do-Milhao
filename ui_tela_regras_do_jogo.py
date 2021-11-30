from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets


class Ui_tela_regras_do_jogo(object):
    def setupUi(self, tela_regras_do_jogo):
        if not tela_regras_do_jogo.objectName():
            tela_regras_do_jogo.setObjectName(u"tela_regras_do_jogo")
        tela_regras_do_jogo.resize(931, 382)
        tela_regras_do_jogo.setMinimumSize(931, 382)
        tela_regras_do_jogo.setMaximumSize(931, 382)
        tela_regras_do_jogo.setWindowTitle(u"Show do Milhão")
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_regras_do_jogo.setWindowIcon(icon)
        tela_regras_do_jogo.setStyleSheet(u"background-color: rgb(0, 54, 100);")
        self.centralwidget = QWidget(tela_regras_do_jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 891, 31))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setText(u"Regras do Jogo")
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 70, 891, 301))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2.setText(
            u"Cada partida é composta por 24 perguntas onde o jogador precisa escolher a alternativa correta para"
            u" continuar avançando.\n"
            "As perguntas estão classificadas em três níveis de dificuldade.\n"
            "A cada resposta correta, o jogador aumenta o valor do seu prêmio. \n"
            "Se a resposta estiver errada, o jogador receberá o valor do prêmio da pergunta anterior.\n"
            "Se o jogador decidir parar, ele receberá metade do valor do prêmio da pergunta atual.\n"
            "Ao longo do jogo, o jogador poderá utilizar dois tipos de dica.\n"
            "A primeira delas é o botão de pular, que pode ser usado em até três oportunidades.\n"
            "Neste botão, a pergunta atual é descartada e uma nova pergunta é sorteada.\n"
            "A outra dica disponível é o botão meio a meio, que pode ser usado em até duas oportunidades.\n"
            "Neste botão, duas alternativas da pergunta atual são eliminadas, facilitando a decisão do jogador "
            "em relação a resposta correta.\n"
            "Na pergunta do milhão, as regras sofrem uma pequena alteração. \n"
            "Primeiro é que nenhuma opção de dica poderá ser usada nesta pergunta.\n"
            "Além disso, se o jogador errar a respota desta pergunta, ele não receberá nenhum valor "
            "financeiro como prêmio.\n"
            "Por fim, ressaltamos que o valor do prêmio é meramente fictício e não corresponde a um valor real.")
        self.label_2.setAlignment(Qt.AlignJustify|Qt.AlignVCenter)
        tela_regras_do_jogo.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(tela_regras_do_jogo)
    # setupUi


class CriarTelaRegrasDoJogo(QtWidgets.QMainWindow, Ui_tela_regras_do_jogo):
    def __init__(self):
        super(CriarTelaRegrasDoJogo, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
         self.hide()
