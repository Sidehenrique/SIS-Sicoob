from PyQt5.QtWidgets import *
import sys
import numpy as np
import pyqtgraph as pg
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets

from entradaEstoque import *

teste = ''
teste2 = ''
teste3 = ''

if teste == '' or teste2 == '' or teste3 == '':
    print('argumento faltando')

else:
    print('tudo certo')



#
# imb = 16333
# marca = 'ACER'
# modelo = 'NITRO'
# condicao = 'NOVO'
# anoFab = 2020
# cfg = 'SIM'
# tela = 16
# ssd = 'SIM'
# HDexp = 'SIM'
# preco = 3000
# carregador = 'SIM'
# processador = 'Core I3'
# marcaPro = 'intel'
# frequenciaPro = '3.3'
# geracaoPro = '1G'
# ram = 8
# ddr = 'DDR4'
# frequenciaMemo = 1600
# memoExp = 'SIM'
# chaveW = 789456132
# chaveO = 123456798
# windows = 'ATIVO'
# office = 'ATIVO'
# descricao = 'descrição'
# data = date.today()
# serviceTag = 12315464
# teamViewer = '13213wqewedff'
# anteVirus = 'SIM'
#
#
#
# print(data)
#
# cursor = db.conectar_mssql()
# cursor.execute(
#     f"""INSERT INTO teste7 VALUES ({imb},'{marca}','{modelo}','{condicao}',{anoFab},'{cfg}',{tela},
#     {preco},'{serviceTag}','{teamViewer}','{ssd}','{HDexp}','{carregador}',
#     '{processador}','{marcaPro}','{frequenciaPro}','{geracaoPro}',{ram},'{ddr}',{frequenciaMemo},
#     '{anteVirus}','{memoExp}','{chaveW}','{chaveO}','{windows}','{office}','{descricao}',{data});""")
# print(data)
# cursor.commit()
# cursor.close()
# # liparCampsNote()










# class Window(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("PyQtGraph")
#         self.setGeometry(100, 100, 600, 500)
#         icon = QIcon("skin.png")
#         self.setWindowIcon(icon)
#         self.UiComponents()  # <------------------------------------------- Grafico dentro da janela
#         self.show()
#
#     def UiComponents(self):
#         widget = QWidget()
#         label = QLabel("Geeksforgeeks Scatter Plot")
#         label.setWordWrap(True)
#         plot = pg.plot()
#         n = 300
#
#         scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(30, 255, 35, 255))
#         x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         y_data = [5, 4, 6, 4, 3, 5, 6, 6, 7, 8]
#         scatter.setData(x_data, y_data)
#
#         plot.addItem(scatter)
#         layout = QGridLayout()
#         label.setMinimumWidth(130)
#         widget.setLayout(layout)
#         layout.addWidget(label, 1, 0)
#         layout.addWidget(plot, 0, 1, 3, 1)
#         self.setCentralWidget(widget)
#         scatter.setScale(1000)
#
# App = QApplication(sys.argv)
# window = Window()
# sys.exit(App.exec())


#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(600, 300)
#         self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
#         self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout.setSpacing(0)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.graphicsView = PlotWidget(Form)
#         self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.graphicsView.setObjectName("graphicsView")
#         self.horizontalLayout.addWidget(self.graphicsView)
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
# from pyqtgraph import PlotWidget
#
#


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = createTable()
#     ui.setupUi(Form)
#     Form.show(ui)
#     sys.exit(app.exec_())

