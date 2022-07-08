import pyodbc

from login import *
from estoqueTI import *
from entradaEstoque import *
import db
from datetime import date



# TRATAMENTO LOGIN =====================================================================================================
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



''' TRATAMENTO HOME ================================================================================================='''
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


''' TRATAMENTO ESTOQUE TI ==========================================================================================='''
def estoqueTi(mw,ee):
    MainEstoque.setWindowTitle('ESTOQUE')

    #  Acionamento Botões menu -----------------------------------------------------------------------------------------
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

    #  Acionamento Botões Submenu --------------------------------------------------------------------------------------
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

    #  Acionamento Botões de icones de TABELA --------------------------------------------------------------------------

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

    ''' Cadastro de Items do estoque no banco -----------------------------------------------------------------------'''
    # mudar o comboBox seletor dos items de cadastro
    ee.stackedWidgetCadastro.setCurrentIndex(0)
    ee.comboBoxSeletorGeral.activated['int'].connect(ee.stackedWidgetCadastro.setCurrentIndex)
    QtCore.QMetaObject.connectSlotsByName(MainEEstoque)

    # Cadastro de Notebook no banco ====================================================================================
    def cadastrarNotebook():
        imb = ee.lineEditIMBNote.text()
        marca = ee.lineEditMarcaNote.text().upper()
        modelo = ee.lineEditModeloNote.text().upper()
        condicao = ee.lineEditEstadoNote.text().upper()
        anoFab = ee.lineEditAnoFabriNote.text()
        cfg = ee.comboBoxCFGNote.currentText()
        tela = ee.comboBoxTelaNote.currentText()
        ssd = ee.comboBoxSSDNote.currentText()
        HDexp = ee.comboBoxExpancivelNote.currentText()
        preco = ee.lineEditPrecoNote.text()
        carregador = ee.comboBoxCarregadorNote.currentText()
        processador = ee.lineEditProcessadorNote.text().upper()
        marcaPro = ee.lineEditMarcaProcessadorNote.text().upper()
        frequenciaPro = ee.lineEditFrequenciaProNote.text().upper()
        geracaoPro = ee.comboBoxGeracaoNote.currentText()
        ram = ee.lineEditRAMNote.text().upper()
        ddr = ee.lineEditDDRNote.text().upper()
        frequenciaMemo = ee.lineEditFrequenciaMemoNote.text().upper()
        memoExp = ee.comboBoxExpancivelRamNote.currentText()
        chaveW = ee.lineEditWindowsNote.text().upper()
        chaveO = ee.lineEditOfficeNote.text().upper()
        windows = ee.comboBoxwindowsNote.currentText()
        office = ee.comboBoxOfficeNote.currentText()
        descricao = ee.lineEditDecricaoNote.text().upper()
        data = date.today()
        serviceTag = ee.lineEditServiceTag.text().upper()
        teamViewer = ee.lineEditTeamViewer.text().upper()
        anteVirus = ee.comboBoxAntevirus.currentText().upper()
        nomeRede = ee.lineEditNomeRede.text().upper()

        lista = [imb, marca, modelo, condicao, anoFab, cfg, tela, preco, serviceTag, teamViewer, ssd, HDexp, carregador,
        processador, nomeRede, marcaPro, frequenciaPro, geracaoPro, ram, ddr, frequenciaMemo, memoExp, chaveW, chaveO, windows,
        office, anteVirus, descricao, data]

        try:
            print(lista)
            cursor = db.conectar_mssql()
            cursor.execute(
                f"""INSERT INTO notebook VALUES ('{imb}','{marca}','{modelo}','{condicao}',{anoFab},'{cfg}','{tela}',
                '{preco}','{serviceTag}','{teamViewer}','{nomeRede}','{ssd}','{HDexp}','{carregador}',
                '{processador}','{marcaPro}','{frequenciaPro}','{geracaoPro}','{ram}','{ddr}','{frequenciaMemo}',
                '{anteVirus}','{memoExp}','{chaveW}','{chaveO}','{windows}','{office}','{descricao}','{data}');""")
            print(data)
            cursor.commit()
            cursor.close()
            limparCampsNote()
            return

        except pyodbc.Error as erro:
            print(erro)
            printe = ('O ITEM NÃO FOI CADASTRADO! certifique-se que os campos estão preenchidos corretamente.'
                      '\nNão ultilize caracteres especial  ( : . , - + = * )')

            ee.labelNotebook.setText(printe)

    def limparCampsNote():
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
        ee.lineEditServiceTag.clear()
        ee.lineEditTeamViewer.clear()
        ee.lineEditNomeRede.clear()
        ee.labelNotebook.clear()

    def cancelarCadNote():
        limparCampsNote()
        MainEEstoque.close()
    ee.pushButtonCancelarNote.clicked.connect(cancelarCadNote)
    ee.pushButtonSalvarNote.clicked.connect(cadastrarNotebook)

    # Cadastro de celular no banco =====================================================================================
    def cadastrarCelu():
        imei = ee.ImeiCelular.text()
        imei2 = ee.Imei2Celular.texto()
        # marca = ee.MarcaCelular.texto()
        # modelo = ee.modeloCelular.text()
        # condicao = ee.estadoCelular.text()
        # anofab = ee.anofabricaoCelular.text()
        # cor = ee.corCelular.text()
        # preco = ee.precoCelular.texto()
        # memoria = ee.memoCelular.text()
        # processador = ee.proCelular.text()
        # modeloPro = ee.modeloProCelular.texto()
        # frequencia = ee.frequenciaProCelular.text()
        # ram = ee.ramCelular.text()
        # bateria = ee.bateriaCelular.text()
        # sistema = ee.sistemaCelular.currentText()
        # microSD = ee.MicroCelular.currentText()
        # dual = ee.dualCelular.currentText()
        # chip1 = ee.chipCelular.currentText()
        # chip2 = ee.chip2celular.currentText()
        # numero1 = ee.nimeroCelularelular.text()
        # numero2 = ee.numero2celular.text()
        # data = date.today()

        # print(imei, imei2, marca, modelo, condicao, anofab, cor, preco, memoria, processador, modeloPro, frequencia,
        #       ram, bateria, sistema, microSD, dual, chip1, chip2, numero1, numero2, data)
        print('deu certo')
        texto = 'deu certo'
        ee.label_Celular.setText(texto)

    def limparCampsCelu():
        ee.lineEditImeiIMEICelular.clear()
        ee.lineEditImeiIMEICelular2.clear()
        ee.lineEditMarcaCelular.clear()
        ee.lineEditModeloModeloCelular.clear()
        ee.lineEditEstadoCelular.clear()
        ee.lineEditAnofabricaoCelular.clear()
        ee.lineEditCorCelular.clear()
        ee.lineEditprecoCelular.clear()
        ee.lineEditMemoCelular_2.clear()
        ee.lineEditProcessardorCelular.clear()
        ee.lineEditModeloModeloCelular.clear()
        ee.lineEditFrequenciaProCelular.clear()
        ee.lineEditRamCelular.clear()
        ee.lineEditBateriaCelular.clear()
        ee.lineEditNumerolCelular.clear()
        ee.lineEditNumero2Celular.clear()
        ee.label_Celular.clear()

    def cancelarCadCelu():
        limparCampsCelu()
        MainEEstoque.close()
    ee.pushButtonCadastraCelular.clicked.connect(cadastrarCelu)
    ee.pushButtonCancelarCelular.clicked.connect(cancelarCadCelu)

    # Cadastro de Memorias no banco ====================================================================================
    def cadastrarMemo():
        marca = ee.lineEditMarcaMemo.text()
        modelo = ee.lineEditModeloMemo.text()
        condicao = ee.lineEditCondicaoMemo.text()
        tamanho = ee.comboBoxTamanhoMemo.currentText()
        plataforma = ee.lineEditPlataformaMemo.text()
        valor = ee.lineEditValorMemo.text()
        descricao = ee.lineEditDescricaoMemo.text()

        listaItems = [marca, modelo, condicao, tamanho, plataforma, valor, descricao]

        print(listaItems)
        texto = 'deu certo'
        ee.label_Memoria.setText(texto)

    def limparCampsMemo():
        ee.lineEditMarcaMemo.clear()
        ee.lineEditModeloMemo.clear()
        ee.lineEditCondicaoMemo.clear()
        ee.comboBoxTamanhoMemo.clear()
        ee.lineEditPlataformaMemo.clear()
        ee.lineEditValorMemo.clear()
        ee.lineEditDescricaoMemo.clear()

    def cancelarCadMemo():
        limparCampsMemo()
        MainEEstoque.close()
    ee.pushButtonCadastraMemo.clicked.connect(cadastrarMemo)
    ee.pushButtonCancelarMemo.clicked.connect(cancelarCadMemo)

    # Cadastro de Disco no banco =======================================================================================
    def cadastrarDisco():
        marca = ee.lineEditMarcaDisco.text()
        modelo = ee.lineEditModeloDisco.text()
        condicao = ee.lineEditCondicaoDisco.text()
        tamanho = ee.comboBoxTamanhoDisco.currentText()
        plataforma = ee.lineEditPlataformaDisco.text()
        valor = ee.lineEditValorDisco.text()
        descricao = ee.lineEditDescricaoDisco.text()

        listaItems = [marca, modelo, condicao, tamanho, plataforma, valor, descricao]

        print(listaItems)
        texto = 'deu certo'
        ee.label_Disco.setText(texto)

    def limparCampsDisco():
        ee.lineEditMarcaDisco.clear()
        ee.lineEditModeloDisco.clear()
        ee.lineEditCondicaoDisco.clear()
        ee.lineEditPlataformaDisco.clear()
        ee.lineEditValorDisco.clear()
        ee.lineEditDescricaoDisco.clear()
        ee.label_Disco.clear()

    def cancelarCadDisco():
        limparCampsDisco()
        MainEEstoque.close()
    ee.pushButtonCadastraDisco.clicked.connect(cadastrarDisco)
    ee.pushButtonCancelarDisco.clicked.connect(cancelarCadDisco)

    # Cadastro de Mouse no banco =======================================================================================
    def cadastrarMouse():
        marca = ee.lineEditMarcaMouse.text()
        modelo = ee.lineEditModeloMouse.text()
        condicao = ee.lineEditCondicaoMouse.text()
        tipo = ee.comboBoxTipoMouse.currentText()
        valor = ee.lineEditValorMouse.text()
        descricao = ee.lineEditDescricaoMouse.text()

        listaItems = [marca, modelo, condicao, tipo, valor, descricao]

        print(listaItems)
        texto = 'deu certo'
        ee.label_Mouse.setText(texto)

    def limparCampsMouse():
        ee.lineEditMarcaMemo.clear()
        ee.lineEditModeloMouse.clear()
        ee.lineEditCondicaoMouse.clear()
        ee.lineEditValorMouse.clear()
        ee.lineEditDescricaoMouse.clear()
        ee.label_Mouse.clear()

    def cancelarCadMouse():
        limparCampsMouse()
        MainEEstoque.close()
    ee.pushButtonCadastraMouse.clicked.connect(cadastrarMouse)
    ee.pushButtonCancelarMouse.clicked.connect(cancelarCadMouse)

    # Cadastro de Mouse Pad no banco =======================================================================================
    def cadastrarPad():
        marca = ee.lineEditMarcaPad.text()
        modelo = ee.lineEditModeloPad.text()
        condicao = ee.lineEditCondicaoPad.text()
        valor = ee.lineEditValorPad.text()
        descricao = ee.lineEditDescricaoPad.text()

        listaItems = [marca, modelo, condicao, valor, descricao]

        print(listaItems)
        texto = 'deu certo'
        ee.label_Pad.setText(texto)

    def limparCampsPad():
        ee.lineEditMarcaPad.clear()
        ee.lineEditModeloPad.clear()
        ee.lineEditCondicaoPad.clear()
        ee.lineEditValorPad.clear()
        ee.lineEditDescricaoPad.clear()
        ee.label_Pad.clear()

    def cancelarCadPad():
        limparCampsPad()
        MainEEstoque.close()
    ee.pushButtonCadastraPad.clicked.connect(cadastrarPad)
    ee.pushButtonCancelarPad.clicked.connect(cancelarCadPad)

    # Cadastro de Teclado no banco =======================================================================================
    def cadastrarTeclado():
        marca = ee.lineEditMarcaTeclado.text()
        modelo = ee.lineEditModeloTeclado.text()
        condicao = ee.lineEditCondicaoTeclado.text()
        valor = ee.lineEditValorTeclado.text()
        descricao = ee.lineEditDescricaoTeclado.text()

        listaItems = [marca, modelo, condicao, valor, descricao]

        print(listaItems)
        texto = 'deu certo'
        ee.label_Teclado.setText(texto)

    def limparCampsTeclado():
        ee.lineEditMarcaTeclado.clear()
        ee.lineEditModeloTeclado.clear()
        ee.lineEditCondicaoTeclado.clear()
        ee.lineEditValorTeclado.clear()
        ee.lineEditDescricaoTeclado.clear()
        ee.label_Teclado.clear()

    def cancelarCadTeclado():
        limparCampsTeclado()
        MainEEstoque.close()
    ee.pushButtonCadastraTeclado.clicked.connect(cadastrarTeclado)
    ee.pushButtonCancelarTeclado.clicked.connect(cancelarCadTeclado)


















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
    # MainEEstoque.show()
    login(ui)
    estoqueTi(mw, ee)

    sys.exit(app.exec_())
