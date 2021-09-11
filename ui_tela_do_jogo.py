from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtWidgets
from ui_tela_acertar import CriarTelaAcertar
from ui_tela_fim_de_jogo import CriarTelaFimDeJogo
import sys
import gspread
import random
import time

gc = gspread.service_account(filename='service_account.json')
sh = gc.open_by_key('1BLKHeJ-QNVctGtBB8pfwpOBo_2ppH0goBl9saBl4JwE')


class Ui_tela_jogo(object):
    flag_mudar_premio = True
    perguntas_sorteadas = []
    numero_pergunta = 1
    nivel = 'facil'
    questao = {'pergunta': '', 'alternativa_1': '', 'alternativa_2': '', 'alternativa_3': '', 'alternativa_4': '',
               'resposta': ''}
    premios = [500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000, 6000, 10000, 20000, 30000, 40000, 50000,
               60000, 100000, 200000, 300000, 400000, 500000, 600000, 1000000]

    def setupUi(self, tela_jogo):
        if not tela_jogo.objectName():
            tela_jogo.setObjectName(u"tela_jogo")
        tela_jogo.setEnabled(True)
        tela_jogo.resize(457, 712)
        tela_jogo.setMaximumSize(457, 712)
        tela_jogo.setMinimumSize(457, 712)
        tela_jogo.setWindowTitle(u"Show do Milhão")
        icon = QIcon()
        icon.addFile(u"logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        tela_jogo.setWindowIcon(icon)
        tela_jogo.setStyleSheet(u"background-color: rgb(0, 0, 121);")
        tela_jogo.setIconSize(QSize(48, 48))
        self.centralwidget = QWidget(tela_jogo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_pergunta = QLabel(self.centralwidget)
        self.label_pergunta.setObjectName(u"label_pergunta")
        self.label_pergunta.setGeometry(QRect(30, 20, 401, 201))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(18)
        self.label_pergunta.setFont(font)
        self.label_pergunta.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.label_pergunta.setText(u"")
        self.label_pergunta.setTextFormat(Qt.AutoText)
        self.label_pergunta.setAlignment(Qt.AlignCenter)
        self.label_pergunta.setWordWrap(True)
        self.label_pergunta.setMargin(0)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 240, 41, 41))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.label_3.setText(u"1")
        self.label_3.setTextFormat(Qt.AutoText)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setMargin(0)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 300, 41, 41))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.label_4.setText(u"2")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setMargin(0)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 360, 41, 41))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.label_6.setText(u"3")
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setMargin(0)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 420, 41, 41))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.label_7.setText(u"4")
        self.label_7.setTextFormat(Qt.AutoText)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.label_7.setMargin(0)
        self.botao_resposta_4 = QPushButton(self.centralwidget)
        self.botao_resposta_4.setObjectName(u"botao_resposta_4")
        self.botao_resposta_4.setGeometry(QRect(80, 420, 351, 41))
        self.botao_resposta_4.setFont(font1)
        self.botao_resposta_4.setLayoutDirection(Qt.LeftToRight)
        self.botao_resposta_4.setAutoFillBackground(False)
        self.botao_resposta_4.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_4.setText(u"")
        self.botao_resposta_4.setAutoExclusive(False)
        self.botao_resposta_4.setAutoRepeatInterval(-2)
        self.botao_resposta_3 = QPushButton(self.centralwidget)
        self.botao_resposta_3.setObjectName(u"botao_resposta_5")
        self.botao_resposta_3.setGeometry(QRect(80, 360, 351, 41))
        self.botao_resposta_3.setFont(font1)
        self.botao_resposta_3.setLayoutDirection(Qt.LeftToRight)
        self.botao_resposta_3.setAutoFillBackground(False)
        self.botao_resposta_3.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_3.setText(u"")
        self.botao_resposta_3.setAutoExclusive(False)
        self.botao_resposta_3.setAutoRepeatInterval(-2)
        self.botao_resposta_1 = QPushButton(self.centralwidget)
        self.botao_resposta_1.setObjectName(u"botao_resposta_1")
        self.botao_resposta_1.setGeometry(QRect(80, 240, 351, 41))
        self.botao_resposta_1.setFont(font1)
        self.botao_resposta_1.setLayoutDirection(Qt.LeftToRight)
        self.botao_resposta_1.setAutoFillBackground(False)
        self.botao_resposta_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_1.setText(u"")
        self.botao_resposta_1.setAutoExclusive(False)
        self.botao_resposta_1.setAutoRepeatInterval(-2)
        self.botao_resposta_2 = QPushButton(self.centralwidget)
        self.botao_resposta_2.setObjectName(u"botao_resposta_2")
        self.botao_resposta_2.setGeometry(QRect(80, 300, 351, 41))
        self.botao_resposta_2.setFont(font1)
        self.botao_resposta_2.setLayoutDirection(Qt.LeftToRight)
        self.botao_resposta_2.setAutoFillBackground(False)
        self.botao_resposta_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_2.setText(u"")
        self.botao_resposta_2.setAutoExclusive(False)
        self.botao_resposta_2.setAutoRepeatInterval(-2)
        self.botao_pular_1 = QPushButton(self.centralwidget)
        self.botao_pular_1.setObjectName(u"botao_pular_1")
        self.botao_pular_1.setEnabled(True)
        self.botao_pular_1.setGeometry(QRect(30, 480, 121, 51))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.botao_pular_1.setFont(font2)
        self.botao_pular_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_pular_1.setText(u"Pular")
        self.botao_pular_1.setIconSize(QSize(111, 61))
        self.botao_pular_1.setCheckable(False)
        self.botao_pular_2 = QPushButton(self.centralwidget)
        self.botao_pular_2.setObjectName(u"botao_pular_2")
        self.botao_pular_2.setEnabled(True)
        self.botao_pular_2.setGeometry(QRect(170, 480, 121, 51))
        self.botao_pular_2.setFont(font2)
        self.botao_pular_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_pular_2.setText(u"Pular")
        self.botao_pular_2.setIconSize(QSize(111, 61))
        self.botao_pular_2.setCheckable(False)
        self.botao_pular_3 = QPushButton(self.centralwidget)
        self.botao_pular_3.setObjectName(u"botao_pular_3")
        self.botao_pular_3.setEnabled(True)
        self.botao_pular_3.setGeometry(QRect(310, 480, 121, 51))
        self.botao_pular_3.setFont(font2)
        self.botao_pular_3.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_pular_3.setText(u"Pular")
        self.botao_pular_3.setIconSize(QSize(111, 61))
        self.botao_pular_3.setCheckable(False)
        self.botao_meio_a_meio_1 = QPushButton(self.centralwidget)
        self.botao_meio_a_meio_1.setObjectName(u"botao_meio_a_meio_1")
        self.botao_meio_a_meio_1.setEnabled(True)
        self.botao_meio_a_meio_1.setGeometry(QRect(30, 550, 121, 51))
        self.botao_meio_a_meio_1.setFont(font2)
        self.botao_meio_a_meio_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_meio_a_meio_1.setText(u"Meio a Meio")
        self.botao_meio_a_meio_1.setIconSize(QSize(111, 61))
        self.botao_meio_a_meio_1.setCheckable(False)
        self.botao_meio_a_meio_2 = QPushButton(self.centralwidget)
        self.botao_meio_a_meio_2.setObjectName(u"botao_meio_a_meio_2")
        self.botao_meio_a_meio_2.setEnabled(True)
        self.botao_meio_a_meio_2.setGeometry(QRect(170, 550, 121, 51))
        self.botao_meio_a_meio_2.setFont(font2)
        self.botao_meio_a_meio_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_meio_a_meio_2.setText(u"Meio a Meio")
        self.botao_meio_a_meio_2.setIconSize(QSize(111, 61))
        self.botao_meio_a_meio_2.setCheckable(False)
        self.botao_parar = QPushButton(self.centralwidget)
        self.botao_parar.setObjectName(u"botao_parar")
        self.botao_parar.setEnabled(True)
        self.botao_parar.setGeometry(QRect(310, 550, 121, 51))
        self.botao_parar.setFont(font2)
        self.botao_parar.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_parar.setText(u"Parar")
        self.botao_parar.setIconSize(QSize(111, 61))
        self.botao_parar.setCheckable(False)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 620, 401, 71))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.groupBox.setFont(font3)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox.setTitle(u"Prêmios")
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 20, 111, 20))
        self.label_12.setFont(font3)
        self.label_12.setLayoutDirection(Qt.LeftToRight)
        self.label_12.setText(u"Errar")
        self.label_12.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(140, 20, 111, 20))
        self.label_13.setFont(font3)
        self.label_13.setLayoutDirection(Qt.LeftToRight)
        self.label_13.setText(u"Parar")
        self.label_13.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(270, 20, 111, 20))
        self.label_14.setFont(font3)
        self.label_14.setLayoutDirection(Qt.LeftToRight)
        self.label_14.setText(u"Acertar")
        self.label_14.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.label_valor_errar = QLabel(self.groupBox)
        self.label_valor_errar.setObjectName(u"label_valor_errar")
        self.label_valor_errar.setGeometry(QRect(20, 40, 111, 20))
        self.label_valor_errar.setFont(font3)
        self.label_valor_errar.setLayoutDirection(Qt.LeftToRight)
        self.label_valor_errar.setText(u"1.000.000,00")
        self.label_valor_errar.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.label_valor_parar = QLabel(self.groupBox)
        self.label_valor_parar.setObjectName(u"label_valor_parar")
        self.label_valor_parar.setGeometry(QRect(140, 40, 111, 20))
        self.label_valor_parar.setFont(font3)
        self.label_valor_parar.setLayoutDirection(Qt.LeftToRight)
        self.label_valor_parar.setText(u"1.000.000,00")
        self.label_valor_parar.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        self.label_valor_acertar = QLabel(self.groupBox)
        self.label_valor_acertar.setObjectName(u"label_valor_acertar")
        self.label_valor_acertar.setGeometry(QRect(270, 40, 111, 20))
        self.label_valor_acertar.setFont(font3)
        self.label_valor_acertar.setLayoutDirection(Qt.LeftToRight)
        self.label_valor_acertar.setAlignment(Qt.AlignBottom | Qt.AlignHCenter)
        tela_jogo.setCentralWidget(self.centralwidget)

        self.timer = QTimer(self)
        self.tela_acertar = CriarTelaAcertar()
        self.tela_fim_de_jogo = CriarTelaFimDeJogo()
        self.botao_resposta_1.clicked.connect(self.arriscar_alternativa_1)
        self.botao_resposta_2.clicked.connect(self.arriscar_alternativa_2)
        self.botao_resposta_3.clicked.connect(self.arriscar_alternativa_3)
        self.botao_resposta_4.clicked.connect(self.arriscar_alternativa_4)
        self.botao_pular_1.clicked.connect(self.pular_pergunta_1)
        self.botao_pular_2.clicked.connect(self.pular_pergunta_2)
        self.botao_pular_3.clicked.connect(self.pular_pergunta_3)
        self.botao_meio_a_meio_1.clicked.connect(self.eliminar_duas_opcoes_1)
        self.botao_meio_a_meio_2.clicked.connect(self.eliminar_duas_opcoes_2)
        self.tela_fim_de_jogo.botao_novo_jogo.clicked.connect(self.novo_jogo)
        self.sortear_pergunta()
        self.preencher_campos()

        QMetaObject.connectSlotsByName(tela_jogo)
    # setupUi

    def pular_pergunta_1(self):
        self.botao_pular_1.setEnabled(False)
        self.botao_pular_1.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.pular_pergunta()
    # pular_pergunta_1

    def pular_pergunta_2(self):
        self.botao_pular_2.setEnabled(False)
        self.botao_pular_2.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.pular_pergunta()
    # pular_pergunta_1

    def pular_pergunta_3(self):
        self.botao_pular_3.setEnabled(False)
        self.botao_pular_3.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.pular_pergunta()
    # pular_pergunta_1

    def pular_pergunta(self):
        time.sleep(1)
        Ui_tela_jogo.flag_mudar_premio = False
        self.hide()
        self.tela_acertar.label.setText(u"Você pulou !")
        self.tela_acertar.barra_progresso.setValue(0)
        self.tela_acertar.show()
        self.timer.timeout.connect(self.incrementar_barra_progresso)
        self.timer.start(1000)
    # pular_pergunta_1

    def eliminar_duas_opcoes_1(self):
        self.botao_meio_a_meio_1.setEnabled(False)
        self.botao_meio_a_meio_1.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.eliminar_duas_opcoes()
    # eliminar_duas_opcoes_1

    def eliminar_duas_opcoes_2(self):
        self.botao_meio_a_meio_2.setEnabled(False)
        self.botao_meio_a_meio_2.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.eliminar_duas_opcoes()
    # eliminar_duas_opcoes_2

    def eliminar_duas_opcoes(self):
        opcoes = [0, 1, 2, 3]
        random.shuffle(opcoes)
        opcoes_eliminadas = 0
        while opcoes_eliminadas < 2:
            if len(opcoes) == 1:
                break
            opcao = opcoes.pop()
            alternativa = f'alternativa_{opcao + 1}'
            if Ui_tela_jogo.questao[alternativa] != Ui_tela_jogo.questao['resposta']:
                if opcao == 0 and self.botao_resposta_1.isEnabled():
                    opcoes_eliminadas += 1
                    self.botao_resposta_1.setEnabled(False)
                    self.botao_resposta_1.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
                elif opcao == 1 and self.botao_resposta_2.isEnabled():
                    opcoes_eliminadas += 1
                    self.botao_resposta_2.setEnabled(False)
                    self.botao_resposta_2.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
                elif opcao == 2 and self.botao_resposta_3.isEnabled():
                    opcoes_eliminadas += 1
                    self.botao_resposta_3.setEnabled(False)
                    self.botao_resposta_3.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
                elif opcao == 3 and self.botao_resposta_4.isEnabled():
                    opcoes_eliminadas += 1
                    self.botao_resposta_4.setEnabled(False)
                    self.botao_resposta_4.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
    # eliminar_duas_opcoes

    def sortear_pergunta(self):
        global sh
        Ui_tela_jogo.questao = {'pergunta': '', 'alternativa_1': '', 'alternativa_2': '', 'alternativa_3': '',
                                'alternativa_4': '', 'resposta': ''}
        if Ui_tela_jogo.numero_pergunta <= 10:
            pagina = sh.worksheet('Facil')
        elif Ui_tela_jogo.numero_pergunta <= 17:
            pagina = sh.worksheet('Medio')
        else:
            pagina = sh.worksheet('Dificil')
        while True:
            num = random.randint(1, 100)
            if num not in Ui_tela_jogo.perguntas_sorteadas:
                Ui_tela_jogo.perguntas_sorteadas.append(num)
                break
        if Ui_tela_jogo.flag_mudar_premio:
            Ui_tela_jogo.numero_pergunta += 1
        else:
            Ui_tela_jogo.flag_mudar_premio = True
        Ui_tela_jogo.questao['pergunta'] = pagina.acell(f'A{num}').value
        Ui_tela_jogo.questao['alternativa_1'] = pagina.acell(f'B{num}').value
        Ui_tela_jogo.questao['alternativa_2'] = pagina.acell(f'C{num}').value
        Ui_tela_jogo.questao['alternativa_3'] = pagina.acell(f'D{num}').value
        Ui_tela_jogo.questao['alternativa_4'] = pagina.acell(f'E{num}').value
        Ui_tela_jogo.questao['resposta'] = pagina.acell(f'F{num}').value
        # print(Ui_tela_jogo.questao)
    # sortear_pergunta

    def preencher_campos(self):
        self.label_pergunta.setText(Ui_tela_jogo.questao['pergunta'])
        self.botao_resposta_1.setText(Ui_tela_jogo.questao['alternativa_1'])
        self.botao_resposta_2.setText(Ui_tela_jogo.questao['alternativa_2'])
        self.botao_resposta_3.setText(Ui_tela_jogo.questao['alternativa_3'])
        self.botao_resposta_4.setText(Ui_tela_jogo.questao['alternativa_4'])
        pergunta = Ui_tela_jogo.numero_pergunta - 1
        if pergunta == 1 or pergunta == len(Ui_tela_jogo.premios):
            self.label_valor_errar.setText(self.formatar_valor_premio(0))
            self.label_valor_parar.setText(self.formatar_valor_premio(Ui_tela_jogo.premios[pergunta - 1] / 2))
            self.label_valor_acertar.setText(self.formatar_valor_premio(Ui_tela_jogo.premios[pergunta - 1]))
        else:
            self.label_valor_errar.setText(self.formatar_valor_premio(Ui_tela_jogo.premios[pergunta] / 2))
            self.label_valor_parar.setText(self.formatar_valor_premio(Ui_tela_jogo.premios[pergunta - 1]))
            self.label_valor_acertar.setText(self.formatar_valor_premio(Ui_tela_jogo.premios[pergunta]))
    # preencher_campos

    def novo_jogo(self):
        self.zerar_dados()
        self.botao_resposta_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_3.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_4.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_pular_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_pular_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_pular_3.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_meio_a_meio_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_meio_a_meio_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_parar.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
        self.botao_resposta_1.setEnabled(True)
        self.botao_resposta_2.setEnabled(True)
        self.botao_resposta_3.setEnabled(True)
        self.botao_resposta_4.setEnabled(True)
        self.botao_pular_1.setEnabled(True)
        self.botao_pular_2.setEnabled(True)
        self.botao_pular_3.setEnabled(True)
        self.botao_meio_a_meio_1.setEnabled(True)
        self.botao_meio_a_meio_2.setEnabled(True)
        self.botao_parar.setEnabled(True)
        self.tela_fim_de_jogo.hide()
        self.tela_acertar.label.setText(u"Iniciando Novo Jogo!")
        self.tela_acertar.barra_progresso.setValue(0)
        self.tela_acertar.show()
        self.timer.timeout.connect(self.incrementar_barra_progresso)
        self.timer.start(1000)
    # novo_jogo

    def zerar_dados(self):
        Ui_tela_jogo.flag_mudar_premio = True
        Ui_tela_jogo.perguntas_sorteadas = []
        Ui_tela_jogo.nivel = 'facil'
        Ui_tela_jogo.numero_pergunta = 1
        Ui_tela_jogo.questao = {'pergunta': '', 'alternativa_1': '', 'alternativa_2': '', 'alternativa_3': '',
                                'alternativa_4': '', 'resposta': ''}
    # zerar_dados

    def formatar_valor_premio(self, valor):
        texto_valor = f'{valor:_.2f}'
        texto_valor = texto_valor.replace('.', ',').replace('_', '.')
        return f'R$ {texto_valor}'
    # formatar_valor_premio

    def arriscar_alternativa_1(self):
        self.botao_resposta_1.setEnabled(False)
        self.botao_resposta_1.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.arriscar_alternativa(Ui_tela_jogo.questao['alternativa_1'])
    # arriscar_alternativa_1

    def arriscar_alternativa_2(self):
        self.botao_resposta_2.setEnabled(False)
        self.botao_resposta_2.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.arriscar_alternativa(Ui_tela_jogo.questao['alternativa_2'])
    # arriscar_alternativa_2

    def arriscar_alternativa_3(self):
        self.botao_resposta_3.setEnabled(False)
        self.botao_resposta_3.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.arriscar_alternativa(Ui_tela_jogo.questao['alternativa_3'])
    # arriscar_alternativa_3

    def arriscar_alternativa_4(self):
        self.botao_resposta_4.setEnabled(False)
        self.botao_resposta_4.setStyleSheet(u"background-color: rgb(100, 0, 0); color: rgb(200, 200, 200);")
        self.arriscar_alternativa(Ui_tela_jogo.questao['alternativa_4'])
    # arriscar_alternativa_4

    def arriscar_alternativa(self, resposta):
        if resposta == Ui_tela_jogo.questao['resposta']:  # Resposta Certa
            # Todo: Fazer condição do milhão
            self.hide()
            self.tela_acertar.label.setText(u"Você acertou !")
            self.tela_acertar.barra_progresso.setValue(0)
            self.tela_acertar.show()
            self.timer.timeout.connect(self.incrementar_barra_progresso)
            self.timer.start(1000)
        else:  # Resposta Errada
            pergunta = Ui_tela_jogo.numero_pergunta - 1
            if pergunta == 1 or pergunta == len(Ui_tela_jogo.premios):
                self.tela_fim_de_jogo.label_premio.setText(f'Você ganhou {self.formatar_valor_premio(0)}')
            else:
                self.tela_fim_de_jogo.label_premio.setText(
                    f'Você ganhou {self.formatar_valor_premio(Ui_tela_jogo.premios[pergunta] / 2)}')
            self.tela_fim_de_jogo.label_premio.raise_()
            self.hide()
            self.tela_fim_de_jogo.show()
    # arriscar_alternativa

    def incrementar_barra_progresso(self):
        self.timer.stop()
        self.tela_acertar.barra_progresso.setValue(self.tela_acertar.barra_progresso.value() + 1)
        if self.tela_acertar.barra_progresso.value() == 2:
            self.sortear_pergunta()
            self.timer.start(1)
            return
        if self.tela_acertar.barra_progresso.value() == 5:
            self.tela_acertar.hide()
            self.show()
            self.timer.stop()
            self.botao_resposta_1.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
            self.botao_resposta_2.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
            self.botao_resposta_3.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
            self.botao_resposta_4.setStyleSheet(u"background-color: rgb(170, 0, 0); color: rgb(255, 255, 255);")
            self.botao_resposta_1.setEnabled(True)
            self.botao_resposta_2.setEnabled(True)
            self.botao_resposta_3.setEnabled(True)
            self.botao_resposta_4.setEnabled(True)
            self.preencher_campos()
            return
        self.timer.start(1000)
    # incrementar_barra_progresso


class CriarTelaResultado(QtWidgets.QMainWindow, Ui_tela_jogo):
    def __init__(self):
        super(CriarTelaResultado, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        sys.exit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window_login = CriarTelaResultado()
    window_login.show()
    sys.exit(app.exec_())
