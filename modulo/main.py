import pyodbc

from login import *
from estoqueTI import *
from entradaEstoque import *
import db
from datetime import date
import pandas as pd
from PyQt5.QtWidgets import QTableWidgetItem


# TRATAMENTO LOGIN ========================================================================
def login(ui):
    # Tratamento do POPUP -----------------------------------------------------------------
    ui.frame_erro.hide()
    ui.Button_quit.clicked.connect(lambda: ui.frame_erro.hide())

    def mensage(mensagem):
        ui.frame_erro.show()
        ui.label_erro.setText(mensagem)

    # VALIDAÇÃO DE DADOS -----------------------------------------------------------------
    def checkPassword():
        usuario = ui.lineEdit.text()
        password = ui.lineEdit_3.text()
        print(usuario, password)

        try:
            cursor = db.conectar_mssql()
            cursor.execute(f"""SELECT senha FROM cadastro WHERE usuario = '{usuario}';""")
            senha_bd = cursor.fetchall()
            print(senha_bd[0][0])
            cursor.close()

        except:
            texto1 = 'Usuário ou senha incorreto'
            mensage(texto1)
            return

        if password == senha_bd[0][0]:
            texto2 = 'Login efetuado com sucesso'
            mensage(texto2)
            print('Sucesso!!!')
            MainLogin.close()
            MainEstoque.showMaximized()

        else:
            texto3 = 'A senha esta incorreta'
            mensage(texto3)

    ui.ENTER.clicked.connect(checkPassword)


# # TRATAMENTO HOME ======================================================================
#
#
# def home(mw):
#     MainWindow.setWindowTitle('HOME')
#     # Acionamento Botão sair -----------------------------------------------------------
#     def callLogin():
#         MainWindow.close()
#         ui.frame_erro.close()
#         ui.lineEdit.clear()
#         ui.lineEdit_3.clear()
#         MainLogin.showMaximized()
#
#     mw.pushButton_sair.clicked.connect(callLogin)
#
#     # Acionamento Botão TI -------------------------------------------------------------
#     def callti():
#         MainWindow.close()
#         MainTI.showMaximized()
#
#     mw.pushButton_TI.clicked.connect(callti)


#
# # TRATAMENTO HOME TI =====================================================================
#
# def homeTi(mw):
#     MainTI.setWindowTitle('HOME TECNOLOGIA')
#
#     # Acionamento Botão sair -------------------------------------------------------------
#     def ButtonSair():
#         MainTI.close()
#         MainWindow.showMaximized()
#
#     # mt.pushButton_sair.clicked.connect(ButtonSair)
#
#     # tratamento de informações com o BANCO DE DADOS ------------------------------------


'''  TRATAMENTO ESTOQUE TI ================================================================== '''

def estoqueTi(mw):
    MainEstoque.setWindowTitle('ESTOQUE')

    #  Acionamento Botões menu ------------------------------------------------------------
    def ButtonVoltar():
        mw.lineEdit_pesquisar.clear()
        mw.lineEdit_pesquisarTable_3.clear()
        MainEstoque.close()
        MainLogin.showMaximized()
    mw.pushButtonVoltar.clicked.connect(ButtonVoltar)

    def ButtonChamados():
        mw.lineEdit_pesquisar.clear()
        mw.lineEdit_pesquisarTable_3.clear()
        pass
    mw.pushButtonChamados.clicked.connect(ButtonChamados)

    def ButtonControle():
        mw.lineEdit_pesquisar.clear()
        mw.lineEdit_pesquisarTable_3.clear()
        pass
    mw.pushButtonControle.clicked.connect(ButtonControle)

    def ButtonEstoque():
        mw.lineEdit_pesquisar.clear()
        mw.lineEdit_pesquisarTable_3.clear()
        pass
    mw.pushButtonEstoque.clicked.connect(ButtonEstoque)

    #  Acionamento Botões Submenu ---------------------------------------------------------
    def ButtonInicio():
        mw.lineEdit_pesquisarTable_3.clear()
        mw.stackedWidget.setCurrentWidget(mw.pageHome)
    mw.pushButton_Inicio.clicked.connect(ButtonInicio)

    def ButtonEntrada():
        MainEEstoque.show()
    mw.pushButtonEntrada.clicked.connect(ButtonEntrada)

    def ButtonSaida():
        pass

    def ButtonHistorico():
        pass

    #  Acionamento Botões de icones de TABELA ---------------------------------------------

    mw.ButtonNotebook.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageNotebook))
    mw.ButtonCelular.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageCelular))
    mw.ButtonMemoria.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMemoria))
    mw.ButtonSSD.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget())
    mw.ButtonMouse.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget())

    #  Tratamento info home ---------------------------------------------------------------

    # def chekQuantidade(entrada):
    #     cursor = db.conectar_mssql()
    #     cursor.execute(f"""SELECT * FROM {entrada};""")
    #     quantidade = cursor.fetchall()
    #     q = (len(quantidade))
    #     print(q)
    #     cursor.close()
    #     return q
    # chekQuantidade('cadastro')

    # mw.labelNotebook.setText(chekQuantidade)


    # def tabelaNote():
    #     mw.tableWidgetCelular.setStyleSheet("")
    #
    #     cursor = db.conectar_mssql()
    #     cursor.execute(f"""SELECT * FROM cadastro;""")
    #     quantidade = cursor.fetchall()
    #
    #
    #
    # mw.tableWidgetCelular.setSortingEnabled(True)


        # mw.tableWidgetCelular.setColumnCount(15)
        # mw.tableWidgetCelular.setRowCount(30)

    ''' Cadastro de Items do estoque no banco ---------------------------------------------'''

    ee.stackedWidgetCadastro.setCurrentIndex(0)
    ee.comboBoxSeletorGeral.activated['int'].connect(ee.stackedWidgetCadastro.setCurrentIndex)
    QtCore.QMetaObject.connectSlotsByName(MainEEstoque)

    def cadastrarNotebook():
        imb = ee.lineEditIMBNote.text()
        marca = ee.lineEditMarcaNote.text()
        modelo = ee.lineEditModeloNote.text()
        condicao = ee.lineEditEstadoNote.text()
        anoFab = ee.lineEditAnoFabriNote.text()
        cfg = ee.comboBoxCFGNote.currentText()
        tela = ee.comboBoxTelaNote.currentText()
        ssd = ee.comboBoxSSDNote.currentText()
        HDexp = ee.comboBoxExpancivelNote.currentText()
        preco = ee.lineEditPrecoNote.text()
        carregador = ee.comboBoxCarregadorNote.currentText()
        processador = ee.lineEditProcessadorNote.text()
        marcaPro = ee.lineEditMarcaProcessadorNote.text()
        frequenciaPro = ee.lineEditFrequenciaProNote.text()
        geracaoPro = ee.comboBoxGeracaoNote.currentText()
        ram = ee.lineEditRAMNote.text()
        ddr = ee.lineEditDDRNote.text()
        frequenciaMemo = ee.lineEditFrequenciaMemoNote.text()
        memoExp = ee.comboBoxExpancivelRamNote.currentText()
        chaveW = ee.lineEditWindowsNote.text()
        chaveO = ee.lineEditOfficeNote.text()
        windows = ee.comboBoxwindowsNote.currentText()
        office = ee.comboBoxOfficeNote.currentText()
        descricao = ee.lineEditDecricaoNote.text()
        data = date.today()
        serviceTag = ee.lineEditPrecoNote_3.text()
        teamViewer = ee.lineEditPrecoNote_2.text()
        anteVirus = ee.comboBoxCarregadorNote_2.currentText()


        def liparCampsNote():
            ee.lineEditIMBNote.clear()
            ee.lineEditMarcaNote.clear()
            ee.lineEditModeloNote.clear()
            ee.lineEditEstadoNote.clear()
            ee.lineEditAnoFabriNote.clear()
            ee.lineEditPrecoNote.clear()
            ee.lineEditProcessadorNote.clear()
            ee.lineEditMarcaProcessadorNote.clear()
            ee.lineEditFrequenciaProNote.clear()
            ee.lineEditRAMNote.clear()
            ee.lineEditDDRNote.clear()
            ee.lineEditFrequenciaMemoNote.clear()
            ee.lineEditWindowsNote.clear()
            ee.lineEditOfficeNote.clear()
            ee.lineEditDecricaoNote.clear()

        lista = [imb, marca, modelo, condicao, anoFab, cfg, tela, preco, serviceTag, teamViewer, ssd, HDexp, carregador,
        processador, marcaPro, frequenciaPro, geracaoPro, ram, ddr, frequenciaMemo, memoExp, chaveW, chaveO, windows,
        office, anteVirus, descricao, data]

        try:
            print(lista)
            cursor = db.conectar_mssql()
            cursor.execute(
                f"""INSERT INTO teste8 VALUES ('{imb}','{marca}','{modelo}','{condicao}',{anoFab},'{cfg}','{tela}',
                '{preco}','{serviceTag}','{teamViewer}','{ssd}','{HDexp}','{carregador}',
                '{processador}','{marcaPro}','{frequenciaPro}','{geracaoPro}','{ram}','{ddr}','{frequenciaMemo}',
                '{anteVirus}','{memoExp}','{chaveW}','{chaveO}','{windows}','{office}','{descricao}','{data}');""")
            print(data)
            cursor.commit()
            cursor.close()
            liparCampsNote()

        except pyodbc.Error:
            print()
            printe = ('Item não cadastrado, favor revisar os dados. / Não ultilizar caracteres especial  ( : . , - + = * )')
            ee.labelNotebook.setText(printe)




    def cancelarCadastro():
        MainEEstoque.clearFocus()
        MainEEstoque.close()
    ee.pushButtonSalvarNote.clicked.connect(cadastrarNotebook)
    ee.pushButtonCancelarNote.clicked.connect(cancelarCadastro)




















if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    MainEstoque = QtWidgets.QMainWindow()
    MainEEstoque = QtWidgets.QMainWindow()

    ui = Ui_MainLogin()
    mw = Ui_MainEstoque()
    ee = Ui_MainEEstoque()

    ui.setupUi(MainLogin)
    mw.setupUi(MainEstoque)
    ee.setupUi(MainEEstoque)


    MainLogin.showMaximized()

    login(ui)
    estoqueTi(mw)

    sys.exit(app.exec_())
