# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'opSaidaEstoqueTI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_opSaidaEstoqueTI(object):
    def setupUi(self, opSaidaEstoqueTI):
        opSaidaEstoqueTI.setObjectName("opSaidaEstoqueTI")
        opSaidaEstoqueTI.resize(600, 400)
        opSaidaEstoqueTI.setMinimumSize(QtCore.QSize(600, 400))
        opSaidaEstoqueTI.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(opSaidaEstoqueTI)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet("background-color: rgb(0, 161, 148);")
        self.stackedWidget.setObjectName("stackedWidget")
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
        self.opLineUser = QtWidgets.QLineEdit(self.splitter)
        self.opLineUser.setMinimumSize(QtCore.QSize(406, 32))
        self.opLineUser.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.opLineUser.setFont(font)
        self.opLineUser.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.opLineUser.setText("")
        self.opLineUser.setAlignment(QtCore.Qt.AlignCenter)
        self.opLineUser.setPlaceholderText("")
        self.opLineUser.setObjectName("opLineUser")
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
        self.opButtonUser = QtWidgets.QPushButton(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opButtonUser.sizePolicy().hasHeightForWidth())
        self.opButtonUser.setSizePolicy(sizePolicy)
        self.opButtonUser.setMinimumSize(QtCore.QSize(0, 37))
        self.opButtonUser.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opButtonUser.setFont(font)
        self.opButtonUser.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opButtonUser.setStyleSheet("QPushButton{\n"
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
        self.opButtonUser.setObjectName("opButtonUser")
        self.label_5 = QtWidgets.QLabel(self.splitter_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.splitter_2)
        self.opLabelUser = QtWidgets.QLabel(self.pageOpUser)
        self.opLabelUser.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opLabelUser.setFont(font)
        self.opLabelUser.setStyleSheet("color: rgb(255, 255, 255)")
        self.opLabelUser.setText("")
        self.opLabelUser.setAlignment(QtCore.Qt.AlignCenter)
        self.opLabelUser.setObjectName("opLabelUser")
        self.verticalLayout_3.addWidget(self.opLabelUser)
        self.stackedWidget.addWidget(self.pageOpUser)
        self.pageComputer = QtWidgets.QWidget()
        self.pageComputer.setObjectName("pageComputer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pageComputer)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.pageComputer)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_2.setStyleSheet("background-image: url(:/button/Com.png);\n"
"background-position:center;\n"
"background-repeat: no-repeat;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2.addWidget(self.frame_2)
        self.splitter_4 = QtWidgets.QSplitter(self.pageComputer)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.label_8 = QtWidgets.QLabel(self.splitter_4)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.opLineCom = QtWidgets.QLineEdit(self.splitter_4)
        self.opLineCom.setMinimumSize(QtCore.QSize(406, 32))
        self.opLineCom.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(9)
        self.opLineCom.setFont(font)
        self.opLineCom.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:1px;\n"
"border-radius: 10px")
        self.opLineCom.setText("")
        self.opLineCom.setAlignment(QtCore.Qt.AlignCenter)
        self.opLineCom.setPlaceholderText("")
        self.opLineCom.setObjectName("opLineCom")
        self.label_9 = QtWidgets.QLabel(self.splitter_4)
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.splitter_4)
        self.splitter_3 = QtWidgets.QSplitter(self.pageComputer)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_6 = QtWidgets.QLabel(self.splitter_3)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.opButtonCom = QtWidgets.QPushButton(self.splitter_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opButtonCom.sizePolicy().hasHeightForWidth())
        self.opButtonCom.setSizePolicy(sizePolicy)
        self.opButtonCom.setMinimumSize(QtCore.QSize(0, 37))
        self.opButtonCom.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opButtonCom.setFont(font)
        self.opButtonCom.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opButtonCom.setStyleSheet("QPushButton{\n"
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
        self.opButtonCom.setObjectName("opButtonCom")
        self.label_7 = QtWidgets.QLabel(self.splitter_3)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.splitter_3)
        self.opLabelCom = QtWidgets.QLabel(self.pageComputer)
        self.opLabelCom.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opLabelCom.setFont(font)
        self.opLabelCom.setStyleSheet("color: rgb(255, 255, 255)")
        self.opLabelCom.setText("")
        self.opLabelCom.setAlignment(QtCore.Qt.AlignCenter)
        self.opLabelCom.setObjectName("opLabelCom")
        self.verticalLayout_2.addWidget(self.opLabelCom)
        self.stackedWidget.addWidget(self.pageComputer)
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
        self.opBoxLocal = QtWidgets.QComboBox(self.splitter_6)
        self.opBoxLocal.setMinimumSize(QtCore.QSize(406, 32))
        self.opBoxLocal.setMaximumSize(QtCore.QSize(406, 32))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.opBoxLocal.setFont(font)
        self.opBoxLocal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.opBoxLocal.setAutoFillBackground(False)
        self.opBoxLocal.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.opBoxLocal.setObjectName("opBoxLocal")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.setItemText(0, "")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
        self.opBoxLocal.addItem("")
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
        self.opButtonLocal = QtWidgets.QPushButton(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.opButtonLocal.sizePolicy().hasHeightForWidth())
        self.opButtonLocal.setSizePolicy(sizePolicy)
        self.opButtonLocal.setMinimumSize(QtCore.QSize(0, 37))
        self.opButtonLocal.setMaximumSize(QtCore.QSize(115, 37))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.opButtonLocal.setFont(font)
        self.opButtonLocal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opButtonLocal.setStyleSheet("QPushButton{\n"
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
        self.opButtonLocal.setObjectName("opButtonLocal")
        self.label_12 = QtWidgets.QLabel(self.splitter_5)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.splitter_5)
        self.oplabelLocal = QtWidgets.QLabel(self.pageOpLocal)
        self.oplabelLocal.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Asap")
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.oplabelLocal.setFont(font)
        self.oplabelLocal.setStyleSheet("color: rgb(255, 255, 255)")
        self.oplabelLocal.setAlignment(QtCore.Qt.AlignCenter)
        self.oplabelLocal.setObjectName("oplabelLocal")
        self.verticalLayout_4.addWidget(self.oplabelLocal)
        self.stackedWidget.addWidget(self.pageOpLocal)
        self.verticalLayout.addWidget(self.stackedWidget)
        opSaidaEstoqueTI.setCentralWidget(self.centralwidget)

        self.retranslateUi(opSaidaEstoqueTI)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(opSaidaEstoqueTI)

    def retranslateUi(self, opSaidaEstoqueTI):
        _translate = QtCore.QCoreApplication.translate
        opSaidaEstoqueTI.setWindowTitle(_translate("opSaidaEstoqueTI", "MainWindow"))
        self.opButtonUser.setText(_translate("opSaidaEstoqueTI", "PESQUISAR"))
        self.opButtonCom.setText(_translate("opSaidaEstoqueTI", "PESQUISAR"))
        self.opBoxLocal.setItemText(1, _translate("opSaidaEstoqueTI", "ESTOQUE TI"))
        self.opBoxLocal.setItemText(2, _translate("opSaidaEstoqueTI", "ESTOQUE UAD"))
        self.opBoxLocal.setItemText(3, _translate("opSaidaEstoqueTI", "U. G. Pessoas"))
        self.opBoxLocal.setItemText(4, _translate("opSaidaEstoqueTI", "U. A. Rural"))
        self.opBoxLocal.setItemText(5, _translate("opSaidaEstoqueTI", "U. Cadastro"))
        self.opBoxLocal.setItemText(6, _translate("opSaidaEstoqueTI", "U. Cobrança"))
        self.opBoxLocal.setItemText(7, _translate("opSaidaEstoqueTI", "Conselho ADM"))
        self.opBoxLocal.setItemText(8, _translate("opSaidaEstoqueTI", "U. Controladoria"))
        self.opBoxLocal.setItemText(9, _translate("opSaidaEstoqueTI", "U. Crédito"))
        self.opBoxLocal.setItemText(10, _translate("opSaidaEstoqueTI", "D. Operacional"))
        self.opBoxLocal.setItemText(11, _translate("opSaidaEstoqueTI", "U. Financeiro"))
        self.opBoxLocal.setItemText(12, _translate("opSaidaEstoqueTI", "U. G. Riscos"))
        self.opBoxLocal.setItemText(13, _translate("opSaidaEstoqueTI", "U. P. Serviços"))
        self.opBoxLocal.setItemText(14, _translate("opSaidaEstoqueTI", "U. Retaguarda"))
        self.opBoxLocal.setItemText(15, _translate("opSaidaEstoqueTI", "S. Executiva"))
        self.opBoxLocal.setItemText(16, _translate("opSaidaEstoqueTI", "U. Tecnologia"))
        self.opBoxLocal.setItemText(17, _translate("opSaidaEstoqueTI", "D. Administrativa"))
        self.opBoxLocal.setItemText(18, _translate("opSaidaEstoqueTI", "G. Operacional"))
        self.opBoxLocal.setItemText(19, _translate("opSaidaEstoqueTI", "G. Administrativa"))
        self.opBoxLocal.setItemText(20, _translate("opSaidaEstoqueTI", "G. Comercial"))
        self.opBoxLocal.setItemText(21, _translate("opSaidaEstoqueTI", "Recepção"))
        self.opBoxLocal.setItemText(22, _translate("opSaidaEstoqueTI", "PA - Planaltina"))
        self.opBoxLocal.setItemText(23, _translate("opSaidaEstoqueTI", "PA - São João"))
        self.opBoxLocal.setItemText(24, _translate("opSaidaEstoqueTI", "PA - SIA"))
        self.opBoxLocal.setItemText(25, _translate("opSaidaEstoqueTI", "PA - Águas Claras"))
        self.opBoxLocal.setItemText(26, _translate("opSaidaEstoqueTI", "PA -Pad/DF"))
        self.opBoxLocal.setItemText(27, _translate("opSaidaEstoqueTI", "PA - Vicente Pires"))
        self.opBoxLocal.setItemText(28, _translate("opSaidaEstoqueTI", "PA - Formosa"))
        self.opBoxLocal.setItemText(29, _translate("opSaidaEstoqueTI", "PA - São Sebastião"))
        self.opBoxLocal.setItemText(30, _translate("opSaidaEstoqueTI", "PA- Digital"))
        self.opButtonLocal.setText(_translate("opSaidaEstoqueTI", "CONFIRMAR"))
        self.oplabelLocal.setText(_translate("opSaidaEstoqueTI", "(U. G.) Unidade de Gestão   |   (U. A.) Unidade de Assessoramento   |   (U.)  Unidade   |   (D.) Diretoria   |  \n"
" (U. P.) Unidade Produtos   |   (S.) Secretaria   |   (G.) Gerencia   |   (PA) Ponto de Atendimento "))

import buttonNote_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    opSaidaEstoqueTI = QtWidgets.QMainWindow()
    ui = Ui_opSaidaEstoqueTI()
    ui.setupUi(opSaidaEstoqueTI)
    opSaidaEstoqueTI.show()
    sys.exit(app.exec_())

