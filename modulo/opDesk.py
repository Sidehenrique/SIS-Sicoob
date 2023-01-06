# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opDesk.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_opDesk(object):
    def setupUi(self, opDesk):
        opDesk.setObjectName("opDesk")
        opDesk.resize(600, 400)
        opDesk.setMinimumSize(QtCore.QSize(600, 400))
        opDesk.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(opDesk)
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
        self.topLineWin = QtWidgets.QLineEdit(self.splitter_4)
        self.topLineWin.setMinimumSize(QtCore.QSize(406, 32))
        self.topLineWin.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.topLineWin.setFont(font)
        self.topLineWin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.topLineWin.setText("")
        self.topLineWin.setAlignment(QtCore.Qt.AlignCenter)
        self.topLineWin.setObjectName("topLineWin")
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
        self.topButtonWin = QtWidgets.QPushButton(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topButtonWin.sizePolicy().hasHeightForWidth())
        self.topButtonWin.setSizePolicy(sizePolicy)
        self.topButtonWin.setMinimumSize(QtCore.QSize(0, 37))
        self.topButtonWin.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topButtonWin.setFont(font)
        self.topButtonWin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.topButtonWin.setStyleSheet("QPushButton{\n"
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
        self.topButtonWin.setObjectName("topButtonWin")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.toplabelWin = QtWidgets.QLabel(self.pageOpWin)
        self.toplabelWin.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toplabelWin.setFont(font)
        self.toplabelWin.setStyleSheet("color: rgb(255, 255, 255)")
        self.toplabelWin.setText("")
        self.toplabelWin.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabelWin.setObjectName("toplabelWin")
        self.verticalLayout_2.addWidget(self.toplabelWin)
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
        self.topLineOff = QtWidgets.QLineEdit(self.splitter_8)
        self.topLineOff.setMinimumSize(QtCore.QSize(406, 32))
        self.topLineOff.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.topLineOff.setFont(font)
        self.topLineOff.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.topLineOff.setText("")
        self.topLineOff.setAlignment(QtCore.Qt.AlignCenter)
        self.topLineOff.setObjectName("topLineOff")
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
        self.topButtonOff = QtWidgets.QPushButton(self.splitter_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topButtonOff.sizePolicy().hasHeightForWidth())
        self.topButtonOff.setSizePolicy(sizePolicy)
        self.topButtonOff.setMinimumSize(QtCore.QSize(0, 37))
        self.topButtonOff.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topButtonOff.setFont(font)
        self.topButtonOff.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.topButtonOff.setStyleSheet("QPushButton{\n"
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
        self.topButtonOff.setObjectName("topButtonOff")
        self.label_17 = QtWidgets.QLabel(self.splitter_7)
        self.label_17.setText("")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_5.addWidget(self.splitter_7)
        self.toplabelOff = QtWidgets.QLabel(self.pageOpOff)
        self.toplabelOff.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toplabelOff.setFont(font)
        self.toplabelOff.setStyleSheet("color: rgb(255, 255, 255)")
        self.toplabelOff.setText("")
        self.toplabelOff.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabelOff.setObjectName("toplabelOff")
        self.verticalLayout_5.addWidget(self.toplabelOff)
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
        self.topLineUser = QtWidgets.QLineEdit(self.splitter)
        self.topLineUser.setMinimumSize(QtCore.QSize(406, 32))
        self.topLineUser.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.topLineUser.setFont(font)
        self.topLineUser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.topLineUser.setText("")
        self.topLineUser.setAlignment(QtCore.Qt.AlignCenter)
        self.topLineUser.setObjectName("topLineUser")
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
        self.topButtonUser = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topButtonUser.sizePolicy().hasHeightForWidth())
        self.topButtonUser.setSizePolicy(sizePolicy)
        self.topButtonUser.setMinimumSize(QtCore.QSize(0, 37))
        self.topButtonUser.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topButtonUser.setFont(font)
        self.topButtonUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.topButtonUser.setStyleSheet("QPushButton{\n"
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
        self.topButtonUser.setObjectName("topButtonUser")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.toplabelUser = QtWidgets.QLabel(self.pageOpUser)
        self.toplabelUser.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.toplabelUser.setFont(font)
        self.toplabelUser.setStyleSheet("color: rgb(255, 255, 255)")
        self.toplabelUser.setText("")
        self.toplabelUser.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabelUser.setObjectName("toplabelUser")
        self.verticalLayout_3.addWidget(self.toplabelUser)
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
        self.topBoxLocal = QtWidgets.QComboBox(self.splitter_6)
        self.topBoxLocal.setMinimumSize(QtCore.QSize(406, 32))
        self.topBoxLocal.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.topBoxLocal.setFont(font)
        self.topBoxLocal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.topBoxLocal.setAutoFillBackground(False)
        self.topBoxLocal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.topBoxLocal.setObjectName("topBoxLocal")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.setItemText(0, "")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
        self.topBoxLocal.addItem("")
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
        self.topButtonLocal = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topButtonLocal.sizePolicy().hasHeightForWidth())
        self.topButtonLocal.setSizePolicy(sizePolicy)
        self.topButtonLocal.setMinimumSize(QtCore.QSize(0, 37))
        self.topButtonLocal.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.topButtonLocal.setFont(font)
        self.topButtonLocal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.topButtonLocal.setStyleSheet("QPushButton{\n"
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
        self.topButtonLocal.setObjectName("topButtonLocal")
        self.label_12 = QtWidgets.QLabel(self.splitter_5)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.splitter_5)
        self.toplabelLocal = QtWidgets.QLabel(self.pageOpLocal)
        self.toplabelLocal.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.toplabelLocal.setFont(font)
        self.toplabelLocal.setStyleSheet("color: rgb(255, 255, 255)")
        self.toplabelLocal.setAlignment(QtCore.Qt.AlignCenter)
        self.toplabelLocal.setObjectName("toplabelLocal")
        self.verticalLayout_4.addWidget(self.toplabelLocal)
        self.stackedWidget.addWidget(self.pageOpLocal)
        self.verticalLayout.addWidget(self.stackedWidget)
        opDesk.setCentralWidget(self.centralwidget)

        self.retranslateUi(opDesk)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(opDesk)

    def retranslateUi(self, opDesk):
        _translate = QtCore.QCoreApplication.translate
        opDesk.setWindowTitle(_translate("opDesk", "MainWindow"))
        self.topLineWin.setPlaceholderText(_translate("opDesk", "TND98-PM9HM-QB6BR-KFGX9-2YT4C"))
        self.topButtonWin.setText(_translate("opDesk", "PESQUISAR"))
        self.topLineOff.setPlaceholderText(_translate("opDesk", "TND98-PM9HM-QB6BR-KFGX9-2YT4C"))
        self.topButtonOff.setText(_translate("opDesk", "PESQUISAR"))
        self.topLineUser.setPlaceholderText(_translate("opDesk", "SIDE HENRIQUE DA SILVA PAES LANDIM"))
        self.topButtonUser.setText(_translate("opDesk", "PESQUISAR"))
        self.topBoxLocal.setItemText(1, _translate("opDesk", "ESTOQUE TI"))
        self.topBoxLocal.setItemText(2, _translate("opDesk", "ESTOQUE UAD"))
        self.topBoxLocal.setItemText(3, _translate("opDesk", "U. G. Pessoas"))
        self.topBoxLocal.setItemText(4, _translate("opDesk", "U. A. Rural"))
        self.topBoxLocal.setItemText(5, _translate("opDesk", "U. Cadastro"))
        self.topBoxLocal.setItemText(6, _translate("opDesk", "U. Cobrança"))
        self.topBoxLocal.setItemText(7, _translate("opDesk", "Conselho ADM"))
        self.topBoxLocal.setItemText(8, _translate("opDesk", "U. Controladoria"))
        self.topBoxLocal.setItemText(9, _translate("opDesk", "U. Crédito"))
        self.topBoxLocal.setItemText(10, _translate("opDesk", "D. Operacional"))
        self.topBoxLocal.setItemText(11, _translate("opDesk", "U. Financeiro"))
        self.topBoxLocal.setItemText(12, _translate("opDesk", "U. G. Riscos"))
        self.topBoxLocal.setItemText(13, _translate("opDesk", "U. P. Serviços"))
        self.topBoxLocal.setItemText(14, _translate("opDesk", "U. Retaguarda"))
        self.topBoxLocal.setItemText(15, _translate("opDesk", "S. Executiva"))
        self.topBoxLocal.setItemText(16, _translate("opDesk", "U. Tecnologia"))
        self.topBoxLocal.setItemText(17, _translate("opDesk", "D. Administrativa"))
        self.topBoxLocal.setItemText(18, _translate("opDesk", "G. Operacional"))
        self.topBoxLocal.setItemText(19, _translate("opDesk", "G. Administrativa"))
        self.topBoxLocal.setItemText(20, _translate("opDesk", "G. Comercial"))
        self.topBoxLocal.setItemText(21, _translate("opDesk", "Recepção"))
        self.topBoxLocal.setItemText(22, _translate("opDesk", "PA - Planaltina"))
        self.topBoxLocal.setItemText(23, _translate("opDesk", "PA - São João"))
        self.topBoxLocal.setItemText(24, _translate("opDesk", "PA - SIA"))
        self.topBoxLocal.setItemText(25, _translate("opDesk", "PA - Águas Claras"))
        self.topBoxLocal.setItemText(26, _translate("opDesk", "PA -Pad/DF"))
        self.topBoxLocal.setItemText(27, _translate("opDesk", "PA - Vicente Pires"))
        self.topBoxLocal.setItemText(28, _translate("opDesk", "PA - Formosa"))
        self.topBoxLocal.setItemText(29, _translate("opDesk", "PA - São Sebastião"))
        self.topBoxLocal.setItemText(30, _translate("opDesk", "PA- Digital"))
        self.topButtonLocal.setText(_translate("opDesk", "CONFIRMAR"))
        self.toplabelLocal.setText(_translate("opDesk", "(U. G.) Unidade de Gestão   |   (U. A.) Unidade de Assessoramento   |   (U.)  Unidade   |   (D.) Diretoria   |  \n"
" (U. P.) Unidade Produtos   |   (S.) Secretaria   |   (G.) Gerencia   |   (PA) Ponto de Atendimento "))

import buttonNote_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    opDesk = QtWidgets.QMainWindow()
    ui = Ui_opDesk()
    ui.setupUi(opDesk)
    opDesk.show()
    sys.exit(app.exec_())

