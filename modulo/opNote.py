# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opNote.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_opNote(object):
    def setupUi(self, opNote):
        opNote.setObjectName("opNote")
        opNote.resize(600, 400)
        opNote.setMinimumSize(QtCore.QSize(600, 400))
        opNote.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(opNote)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 161, 148);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageOpWin = QtWidgets.QWidget()
        self.pageOpWin.setObjectName("pageOpWin")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageOpWin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.pageOpWin)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setStyleSheet("background-image: url(:/button/windows.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.splitter_4 = QtWidgets.QSplitter(self.pageOpWin)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_8 = QtWidgets.QLabel(self.splitter_4)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.notLineWin = QtWidgets.QLineEdit(self.splitter_4)
        self.notLineWin.setMinimumSize(QtCore.QSize(406, 32))
        self.notLineWin.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.notLineWin.setFont(font)
        self.notLineWin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.notLineWin.setText("")
        self.notLineWin.setAlignment(QtCore.Qt.AlignCenter)
        self.notLineWin.setObjectName("notLineWin")
        self.label_9 = QtWidgets.QLabel(self.splitter_4)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.splitter_3 = QtWidgets.QSplitter(self.pageOpWin)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_6 = QtWidgets.QLabel(self.splitter_3)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.notButtonWin = QtWidgets.QPushButton(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notButtonWin.sizePolicy().hasHeightForWidth())
        self.notButtonWin.setSizePolicy(sizePolicy)
        self.notButtonWin.setMinimumSize(QtCore.QSize(0, 37))
        self.notButtonWin.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notButtonWin.setFont(font)
        self.notButtonWin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notButtonWin.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 53, 62);\n"
"    border: 1px;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 73, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 64, 74);\n"
"    color: rgb(98, 98, 98);\n"
"}\n"
"")
        self.notButtonWin.setObjectName("notButtonWin")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.notlabelWin = QtWidgets.QLabel(self.pageOpWin)
        self.notlabelWin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notlabelWin.setFont(font)
        self.notlabelWin.setStyleSheet("color: rgb(255, 255, 255)")
        self.notlabelWin.setText("")
        self.notlabelWin.setAlignment(QtCore.Qt.AlignCenter)
        self.notlabelWin.setObjectName("notlabelWin")
        self.verticalLayout_2.addWidget(self.notlabelWin)
        self.stackedWidget.addWidget(self.pageOpWin)
        self.pageOpOff = QtWidgets.QWidget()
        self.pageOpOff.setObjectName("pageOpOff")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pageOpOff)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.pageOpOff)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_4.setStyleSheet("background-image: url(:/button/office.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5.addWidget(self.frame_4)
        self.splitter_8 = QtWidgets.QSplitter(self.pageOpOff)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_18 = QtWidgets.QLabel(self.splitter_8)
        self.label_18.setText("")
        self.label_18.setObjectName("label_18")
        self.notLineOff = QtWidgets.QLineEdit(self.splitter_8)
        self.notLineOff.setMinimumSize(QtCore.QSize(406, 32))
        self.notLineOff.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.notLineOff.setFont(font)
        self.notLineOff.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.notLineOff.setText("")
        self.notLineOff.setAlignment(QtCore.Qt.AlignCenter)
        self.notLineOff.setObjectName("notLineOff")
        self.label_19 = QtWidgets.QLabel(self.splitter_8)
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_5.addWidget(self.splitter_8)
        self.splitter_7 = QtWidgets.QSplitter(self.pageOpOff)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_16 = QtWidgets.QLabel(self.splitter_7)
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.notButtonOff = QtWidgets.QPushButton(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notButtonOff.sizePolicy().hasHeightForWidth())
        self.notButtonOff.setSizePolicy(sizePolicy)
        self.notButtonOff.setMinimumSize(QtCore.QSize(0, 37))
        self.notButtonOff.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notButtonOff.setFont(font)
        self.notButtonOff.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notButtonOff.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 53, 62);\n"
"    border: 1px;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 73, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 64, 74);\n"
"    color: rgb(98, 98, 98);\n"
"}\n"
"")
        self.notButtonOff.setObjectName("notButtonOff")
        self.label_17 = QtWidgets.QLabel(self.splitter_7)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.splitter_7)
        self.notlabelOff = QtWidgets.QLabel(self.pageOpOff)
        self.notlabelOff.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notlabelOff.setFont(font)
        self.notlabelOff.setStyleSheet("color: rgb(255, 255, 255)")
        self.notlabelOff.setText("")
        self.notlabelOff.setAlignment(QtCore.Qt.AlignCenter)
        self.notlabelOff.setObjectName("notlabelOff")
        self.verticalLayout_5.addWidget(self.notlabelOff)
        self.stackedWidget.addWidget(self.pageOpOff)
        self.pageOpUser = QtWidgets.QWidget()
        self.pageOpUser.setObjectName("pageOpUser")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pageOpUser)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.pageOpUser)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame.setStyleSheet("background-image: url(:/button/user.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3.addWidget(self.frame)
        self.splitter = QtWidgets.QSplitter(self.pageOpUser)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.notLineUser = QtWidgets.QLineEdit(self.splitter)
        self.notLineUser.setMinimumSize(QtCore.QSize(406, 32))
        self.notLineUser.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.notLineUser.setFont(font)
        self.notLineUser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.notLineUser.setText("")
        self.notLineUser.setAlignment(QtCore.Qt.AlignCenter)
        self.notLineUser.setObjectName("notLineUser")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.splitter)
        self.splitter_2 = QtWidgets.QSplitter(self.pageOpUser)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.notButtonUser = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notButtonUser.sizePolicy().hasHeightForWidth())
        self.notButtonUser.setSizePolicy(sizePolicy)
        self.notButtonUser.setMinimumSize(QtCore.QSize(0, 37))
        self.notButtonUser.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notButtonUser.setFont(font)
        self.notButtonUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notButtonUser.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 53, 62);\n"
"    border: 1px;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 73, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 64, 74);\n"
"    color: rgb(98, 98, 98);\n"
"}\n"
"")
        self.notButtonUser.setObjectName("notButtonUser")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.notlabelUser = QtWidgets.QLabel(self.pageOpUser)
        self.notlabelUser.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notlabelUser.setFont(font)
        self.notlabelUser.setStyleSheet("color: rgb(255, 255, 255)")
        self.notlabelUser.setText("")
        self.notlabelUser.setAlignment(QtCore.Qt.AlignCenter)
        self.notlabelUser.setObjectName("notlabelUser")
        self.verticalLayout_3.addWidget(self.notlabelUser)
        self.stackedWidget.addWidget(self.pageOpUser)
        self.pageOpLocal = QtWidgets.QWidget()
        self.pageOpLocal.setObjectName("pageOpLocal")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pageOpLocal)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_3 = QtWidgets.QFrame(self.pageOpLocal)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_3.setStyleSheet("background-image: url(:/button/local.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4.addWidget(self.frame_3)
        self.splitter_6 = QtWidgets.QSplitter(self.pageOpLocal)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_13 = QtWidgets.QLabel(self.splitter_6)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.notBoxLocal = QtWidgets.QComboBox(self.splitter_6)
        self.notBoxLocal.setMinimumSize(QtCore.QSize(406, 32))
        self.notBoxLocal.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.notBoxLocal.setFont(font)
        self.notBoxLocal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.notBoxLocal.setAutoFillBackground(False)
        self.notBoxLocal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.notBoxLocal.setObjectName("notBoxLocal")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.setItemText(0, "")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.notBoxLocal.addItem("")
        self.label_14 = QtWidgets.QLabel(self.splitter_6)
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.splitter_6)
        self.splitter_5 = QtWidgets.QSplitter(self.pageOpLocal)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_11 = QtWidgets.QLabel(self.splitter_5)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.notButtonLocal = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notButtonLocal.sizePolicy().hasHeightForWidth())
        self.notButtonLocal.setSizePolicy(sizePolicy)
        self.notButtonLocal.setMinimumSize(QtCore.QSize(0, 37))
        self.notButtonLocal.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.notButtonLocal.setFont(font)
        self.notButtonLocal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.notButtonLocal.setStyleSheet("QPushButton{\n"
"    background-color: rgb(0, 53, 62);\n"
"    border: 1px;\n"
"    border-radius: 10px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 73, 85);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(0, 64, 74);\n"
"    color: rgb(98, 98, 98);\n"
"}\n"
"")
        self.notButtonLocal.setObjectName("notButtonLocal")
        self.label_12 = QtWidgets.QLabel(self.splitter_5)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.splitter_5)
        self.notlabelLocal = QtWidgets.QLabel(self.pageOpLocal)
        self.notlabelLocal.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.notlabelLocal.setFont(font)
        self.notlabelLocal.setStyleSheet("color: rgb(255, 255, 255)")
        self.notlabelLocal.setAlignment(QtCore.Qt.AlignCenter)
        self.notlabelLocal.setObjectName("notlabelLocal")
        self.verticalLayout_4.addWidget(self.notlabelLocal)
        self.stackedWidget.addWidget(self.pageOpLocal)
        self.verticalLayout.addWidget(self.stackedWidget)
        opNote.setCentralWidget(self.centralwidget)

        self.retranslateUi(opNote)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(opNote)

    def retranslateUi(self, opNote):
        _translate = QtCore.QCoreApplication.translate
        opNote.setWindowTitle(_translate("opNote", "MainWindow"))
        self.notLineWin.setPlaceholderText(_translate("opNote", "TND98-PM9HM-QB6BR-KFGX9-2YT4C"))
        self.notButtonWin.setText(_translate("opNote", "PESQUISAR"))
        self.notLineOff.setPlaceholderText(_translate("opNote", "TND98-PM9HM-QB6BR-KFGX9-2YT4C"))
        self.notButtonOff.setText(_translate("opNote", "PESQUISAR"))
        self.notLineUser.setPlaceholderText(_translate("opNote", "SIDE HENRIQUE DA SILVA PAES LANDIM"))
        self.notButtonUser.setText(_translate("opNote", "PESQUISAR"))
        self.notBoxLocal.setItemText(1, _translate("opNote", "ESTOQUE TI"))
        self.notBoxLocal.setItemText(2, _translate("opNote", "ESTOQUE UAD"))
        self.notBoxLocal.setItemText(3, _translate("opNote", "U. G. Pessoas"))
        self.notBoxLocal.setItemText(4, _translate("opNote", "U. A. Rural"))
        self.notBoxLocal.setItemText(5, _translate("opNote", "U. Cadastro"))
        self.notBoxLocal.setItemText(6, _translate("opNote", "U. Cobrança"))
        self.notBoxLocal.setItemText(7, _translate("opNote", "Conselho ADM"))
        self.notBoxLocal.setItemText(8, _translate("opNote", "U. Controladoria"))
        self.notBoxLocal.setItemText(9, _translate("opNote", "U. Crédito"))
        self.notBoxLocal.setItemText(10, _translate("opNote", "D. Operacional"))
        self.notBoxLocal.setItemText(11, _translate("opNote", "U. Financeiro"))
        self.notBoxLocal.setItemText(12, _translate("opNote", "U. G. Riscos"))
        self.notBoxLocal.setItemText(13, _translate("opNote", "U. P. Serviços"))
        self.notBoxLocal.setItemText(14, _translate("opNote", "U. Retaguarda"))
        self.notBoxLocal.setItemText(15, _translate("opNote", "S. Executiva"))
        self.notBoxLocal.setItemText(16, _translate("opNote", "U. Tecnologia"))
        self.notBoxLocal.setItemText(17, _translate("opNote", "D. Administrativa"))
        self.notBoxLocal.setItemText(18, _translate("opNote", "G. Operacional"))
        self.notBoxLocal.setItemText(19, _translate("opNote", "G. Administrativa"))
        self.notBoxLocal.setItemText(20, _translate("opNote", "G. Comercial"))
        self.notBoxLocal.setItemText(21, _translate("opNote", "Recepção"))
        self.notBoxLocal.setItemText(22, _translate("opNote", "PA - Planaltina"))
        self.notBoxLocal.setItemText(23, _translate("opNote", "PA - São João"))
        self.notBoxLocal.setItemText(24, _translate("opNote", "PA - SIA"))
        self.notBoxLocal.setItemText(25, _translate("opNote", "PA - Águas Claras"))
        self.notBoxLocal.setItemText(26, _translate("opNote", "PA -Pad/DF"))
        self.notBoxLocal.setItemText(27, _translate("opNote", "PA - Vicente Pires"))
        self.notBoxLocal.setItemText(28, _translate("opNote", "PA - Formosa"))
        self.notBoxLocal.setItemText(29, _translate("opNote", "PA - São Sebastião"))
        self.notBoxLocal.setItemText(30, _translate("opNote", "PA- Digital"))
        self.notButtonLocal.setText(_translate("opNote", "CONFIRMAR"))
        self.notlabelLocal.setText(_translate("opNote", "(U. G.) Unidade de Gestão   |   (U. A.) Unidade de Assessoramento   |   (U.)  Unidade   |   (D.) Diretoria   |  \n"
" (U. P.) Unidade Produtos   |   (S.) Secretaria   |   (G.) Gerencia   |   (PA) Ponto de Atendimento "))

import buttonNote_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    opNote = QtWidgets.QMainWindow()
    ui = Ui_opNote()
    ui.setupUi(opNote)
    opNote.show()
    sys.exit(app.exec_())

