import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from login import *
from ControleTI import *
from EstoqueTI import *
from entradaEstoque import *
from Dialog import *
from DialogEntrada import *
from DialogSaida import *
from DialogBaixa import *
from DialogCondicional import *
from Positive import *
from opNote import *
from opDesk import *
from opCell import *
from opSaidaEstoqueTI import *
import db
import datetime
import pymysql


########################################################################################################################
        ################################################ LOGIN ################################################
########################################################################################################################

def login(ui):
    MainLogin.setWindowTitle('LOGIN')

    # TRATAMENTO DE POPUP -----------------------------------------------------------------
    ui.frame_erro.hide()
    ui.Button_quit.clicked.connect(lambda: ui.frame_erro.hide())

    def mensage(mensagem):
        ui.frame_erro.show()
        ui.label_erro.setText(mensagem)
  
    # VALIDAÇÃO DE DADOS -----------------------------------------------------------------
    def checkPassword():
        global Usuario
        Usuario = ui.lineEdit.text()
        password = ui.lineEdit_3.text()
        print(Usuario, password + '<--- entrada do Usuário')

        if Usuario == '' or password == '':
            text = 'CAMPOS NÃO PREENCHIDOS'
            mensage(text)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(f"""SELECT password FROM usuarios WHERE user = '{Usuario}';""")
                senha_bd = cursor.fetchall()
                print(senha_bd[0][0] + '<--- banco de dados')
                cursor.close()

                if password == senha_bd[0][0]:
                    texto = 'BEM-VINDO ' + Usuario.upper()
                    mw.labelGeralUsuario.setText(texto)

                    print(texto)
                    mensage(texto)
                    ui.lineEdit.clear()
                    ui.lineEdit_3.clear()
                    MainLogin.close()
                    MainEstoque.showMaximized()
                    mw.stackedWidget.setCurrentIndex(0)

                else:
                    texto = 'SENHA INCORRETA'
                    mensage(texto)

            except:
                texto = 'NOME DE USUÁRIO INCORRETO'
                mensage(texto)
                return

    ui.ENTER.clicked.connect(checkPassword)

    # VERSÃO DE SOFTWARE -----------------------------------------------------------------

    # NOTIFICAÇÕES -----------------------------------------------------------------------




########################################################################################################################
      ################################################ CONTROLE TI ################################################
########################################################################################################################

def controle():

    MainControle.setWindowTitle('PAINEL DE CONTROLE TI')

    def datAT():
        data = datetime.datetime.now()
        d = datetime.datetime.strftime(data, "%d-%m-%Y %H:%M")
        return d

    # BUTÕES DE NAVEGAÇÃO DO MENU ######################################################################################
    def buttonEstoqueTI():
        MainEstoque.showMaximized()
        mw.stackedWidget.setCurrentWidget(mw.pageHome)
        MainControle.close()
    mc.pushButtonEstoque.clicked.connect(buttonEstoqueTI)

    def buttonVoltar():
        MainLogin.showMaximized()
        MainEstoque.close()
    mc.pushButtonVoltar.clicked.connect(buttonVoltar)

    # BUTÕES DE NAVEGAÇÃO DO SUB MENU ##################################################################################
    # def buttonCad():
    #     mc.stackedWidget.setCurrentWidget(mc.pageCad)
    #
    # mc.pushButtonCadastro.clicked.connect(buttonCad)

    def buttonUser():
        mc.stackedWidget.setCurrentWidget(mc.pageUser)

    mc.pushButtonUser.clicked.connect(buttonUser)

    def buttonInicio():
        mc.stackedWidget.setCurrentWidget(mc.pageHome)

    mc.pushButtonInicio.clicked.connect(buttonInicio)

    def buttonHistorico():
        mc.stackedWidget.setCurrentWidget(mc.pageHistorico)
        historico()

    mc.pushButtonHistorico.clicked.connect(buttonHistorico)

    # TRATAMENTO PAGE CADASTRO # <<< ------------------------------------------
    def cadNovo():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
    mc.pushButtonNovo.clicked.connect(cadNovo)



    # PAGE HISTORICO ###################################################################################################
    def historico():
        con = db.conMySQL()
        con.execute("""select * from historico order by data desc LIMIT 20;""")
        result = con.fetchall()

        mc.tableWidgetHistorico.clearContents()
        header = mc.tableWidgetHistorico.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # -------------------------------------------------------
        mc.tableWidgetHistorico.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mc.tableWidgetHistorico.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        con.close()

    historico()
    mc.ButtonHistoricoAtualizar.clicked.connect(historico)

########################################################################################################################
      ################################################ ESTOQUE TI ###############################################
########################################################################################################################

def estoqueTi():

    def datAT():
        data = datetime.datetime.now()
        d = datetime.datetime.strftime(data, "%d-%m-%Y %H:%M")
        return d

    MainEstoque.setWindowTitle('ESTOQUE')

    #  Acionamento Botões menu -----------------------------------------------------------------------------------------
    def ButtonVoltar():
        MainEstoque.close()
        ui.frame_erro.hide()
        MainLogin.showMaximized()

    mw.pushButtonVoltar.clicked.connect(ButtonVoltar)

    def ButtonChamados():
        pass

    mw.pushButtonChamados.clicked.connect(ButtonChamados)

    def ButtonControleTI():
        MainEstoque.close()
        MainControle.showMaximized()
        mc.stackedWidget.setCurrentWidget(mc.pageHome)
    mw.pushButtonControle.clicked.connect(ButtonControleTI)

    def ButtonEstoque():
        MainEstoque.showMaximized()
        MainControle.close()
        mw.stackedWidget.setCurrentWidget(mw.pageHome)
        quantiTable()
        # carregarDados()

    mw.pushButtonEstoque.clicked.connect(ButtonEstoque)

    #  Acionamento Botões Submenu --------------------------------------------------------------------------------------
    def ButtonInicio():
        quantiTable()
        mw.stackedWidget.setCurrentWidget(mw.pageHome)

    mw.pushButton_Inicio.clicked.connect(ButtonInicio)

    def ButtonGestao():
        mw.stackedWidget.setCurrentWidget(mw.PageGestao)

    mw.pushButtonGestao.clicked.connect(ButtonGestao)

    def ButtonHistorico():
        mw.stackedWidget.setCurrentWidget(mw.pageHistorico)
        infoHistorico()
    mw.pushButtonHistorico.clicked.connect(ButtonHistorico)

    #  Acionamento Botões PAGE GESTÃO-----------------------------------------------------------------------------------
    def cadNovo():
        mw.stackedWidget.setCurrentWidget(mw.pageCad)
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
    mw.pushButtonNovo.clicked.connect(cadNovo)

    def ButtonEntrada():
        mw.stackedWidget.setCurrentWidget(mw.pageEntrada)
    mw.pushButtonEntrada.clicked.connect(ButtonEntrada)

    def ButtonSaida():
        mw.stackedWidget.setCurrentWidget(mw.pageSaida)
    mw.pushButtonSaida.clicked.connect(ButtonSaida)

    def ButtonBaixa():
        mw.stackedWidget.setCurrentWidget(mw.pageBaixa)
    mw.pushButtonBaixa.clicked.connect(ButtonBaixa)

    def ButtonVisualizar():
        pass
    mw.pushButtonVisualizar.clicked.connect(ButtonVisualizar)


    # TRATAMENTO PAGE NOVO # <<< ------------------------------------------
    def note():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNotebookCad)
    mw.buttonNote.clicked.connect(note)

    def desk():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageDesktopCad)
    mw.buttonDesk.clicked.connect(desk)

    def cell():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageCelularCad)
    mw.buttonCel.clicked.connect(cell)

    def Monitor():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageMonitorCad)
    mw.buttonMon.clicked.connect(Monitor)

    def perifericos():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
    mw.buttonPeri.clicked.connect(perifericos)

    def Windows():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageWindowsCad)
    mw.buttonWin.clicked.connect(Windows)

    def Office():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageOfficeCad)
    mw.buttonOff.clicked.connect(Office)

    def Memoria():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageMemoriaCad)
    mw.buttonMemo.clicked.connect(Memoria)

    def disco():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageDiscoCad)
    mw.buttonDisco.clicked.connect(disco)

    def mouse():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageMouseCad)
    mw.buttonMouse.clicked.connect(mouse)

    def pad():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePadCad)
    mw.buttonPad.clicked.connect(pad)

    def teclado():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageTecladoCad)
    mw.buttonTeclado.clicked.connect(teclado)

    def suport():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageSuporteCad)
    mw.buttonUporte.clicked.connect(suport)

    def outros():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageOutrosCad)
    mw.buttonOutros.clicked.connect(outros)


#####  TRATAMENTO PAGES VISUALIZAÇÕES ##################################################################################
    def quantiTable():
        cursor = db.conMySQL()
        cursor.execute(f"""SELECT * FROM computer;""")
        notebook = len(cursor.fetchall())
        mw.labelNotebook.setText(str(notebook))
        #mw.labelTotalnotebook.setText(str(notebook))

        cursor.execute(f"""SELECT * FROM celular;""")
        celular = len(cursor.fetchall())
        mw.labelCelular.setText(str(celular))
        #mw.labelTotalcelular.setText(str(celular))

        cursor.execute(f"""SELECT * FROM memoria;""")
        memoria = len(cursor.fetchall())
        mw.labelMemoria.setText(str(memoria))
        #mw.labelTotalmemoria.setText(str(memoria))

        cursor.execute(f"""SELECT * FROM disco;""")
        disco = len(cursor.fetchall())
        mw.labelSSD.setText(str(disco))
        #mw.labelTotaldisco.setText(str(disco))

        cursor.execute(f"""SELECT * FROM mouse;""")
        mouse = len(cursor.fetchall())
        mw.labelMouse.setText(str(mouse))
        #mw.labelTotalMouse.setText(str(mouse))

        cursor.execute(f"""SELECT * FROM mousePad;""")
        pad = len(cursor.fetchall())
        mw.labelMousepad.setText(str(pad))
        #mw.labelTotalPad.setText(str(pad))

        cursor.execute(f"""SELECT * FROM teclado;""")
        teclado = len(cursor.fetchall())
        mw.labelTeclado.setText(str(teclado))
        #mw.labelTotalTeclado.setText(str(teclado))

        cursor.execute(f"""SELECT * FROM suporte;""")
        suporte = len(cursor.fetchall())
        mw.labelSuporte.setText(str(suporte))
        #mw.labelTotalSuporte.setText(str(suporte))

        cursor.execute(f"""SELECT * FROM monitor;""")
        monitor = len(cursor.fetchall())
        mw.labelEmail.setText(str(monitor))
        #mw.labelTotalEmail.setText(str(monitor))

        cursor.execute(f"""SELECT * FROM office;""")
        office = len(cursor.fetchall())
        mw.labelOffice.setText(str(office))
        #mw.labelTotalOffice.setText(str(office))

        cursor.execute(f"""SELECT * FROM windows;""")
        windows = len(cursor.fetchall())
        mw.labelWindows.setText(str(windows))
        #mw.labelTotalWindows.setText(str(windows))

        cursor.execute(f"""SELECT * FROM outros;""")
        outros = len(cursor.fetchall())
        mw.labelOutros.setText(str(outros))
        #mw.labelTotalOutros.setText(str(outros))

        cursor.close()
    quantiTable()

    # HISTORICO  -------------------------------------------------------------------------------------------------------

    def pesHistorico():
        pesquisa = mw.LineEditPesHistorico.text()

        con = db.conMySQL()
        con.execute(f"""SELECT * FROM historico WHERE id like '%{pesquisa}%';""")
        result = con.fetchall()
        print(result)

        mw.tableWidgetHistorico.clearContents()
        header = mw.tableWidgetHistorico.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetHistorico.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetHistorico.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
    mw.hisPesButton.clicked.connect(pesHistorico)

    def infoHistorico():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM historico', con)
        con.close()

        total = len(result)
        novo = result[(result['status'] == 'NOVO') & (result['local'] == 'ESTOQUE')].shape[0]
        saidas = result[(result['status'] == 'SAIDA. ESTOQUE TI')].shape[0]
        entradas = result[(result['status'] == 'ENT. ESTOQUE TI') & (result['local'] == 'ESTOQUE')].shape[0]
        baixas = result[(result['status'] == 'BAIXA ESTOQUE TI') & (result['local'] == 'ESTOQUE')].shape[0]
        trans = result[(result['status'] == 'TRANS. ESTOQUE TI')].shape[0]

        print(total, novo, saidas, entradas, baixas, trans)

        mw.hislabel01.setText(str(total))
        mw.hislabel02.setText(str(entradas))
        mw.hislabel03.setText(str(saidas))
        mw.label_82.setText(str(trans))
        mw.label_105.setText(str(baixas))
        mw.label_103.setText(str(novo))

        con = db.conMySQL()
        con.execute("""select * from historico order by data desc LIMIT 20;""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetHistorico.clearContents()
        header = mw.tableWidgetHistorico.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # -------------------------------------------------------
        mw.tableWidgetHistorico.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetHistorico.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        con.close()

    # NOTEBOOK  --------------------------------------------------------------------------------------------------------

    def pesquisa_Note():
        pesquisa = mw.notPes.text()

        con = db.conMySQL()
        con.execute(f"""SELECT * FROM computer WHERE idComputer like '%{pesquisa}%';""")
        result = con.fetchall()
        print(result)

        mw.tableWidgetNotebook.clearContents()
        mw.tableWidgetNotebook.horizontalHeader()
        # header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetNotebook.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetNotebook.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    def informacao_Note():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM computer', con)
        con.close()

        total = len(result)
        notebook = result[(result['TIPO'] == 'Notebook')].shape[0]
        desktop = result[(result['TIPO'] == 'Desktop')].shape[0]
        ssd = result[(result['SSD'] == 'SIM')].shape[0]

        print(total, notebook, desktop)

        mw.hislabel01_2.setText(str(total))
        mw.hislabel02_2.setText(str(notebook))
        mw.hislabel03_3.setText(str(desktop))

        con = db.conMySQL()
        con.execute("""select * from computer;""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetNotebook.clearContents()
        mw.tableWidgetNotebook.horizontalHeader()
        # header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # -------------------------------------------------------
        mw.tableWidgetNotebook.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetNotebook.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        con.close()

    def get_info_table():
        ret = mw.tableWidgetNotebook.currentRow()
        cod = mw.tableWidgetNotebook.item(ret, 0).text()

        ssd = mw.tableWidgetNotebook.item(ret, 11).text()
        processador = mw.tableWidgetNotebook.item(ret, 14).text()
        frequencia_pro = mw.tableWidgetNotebook.item(ret, 16).text()
        geracao = mw.tableWidgetNotebook.item(ret, 17).text()
        ram = mw.tableWidgetNotebook.item(ret, 18).text()
        tela = mw.tableWidgetNotebook.item(ret, 6).text()
        estado = mw.tableWidgetNotebook.item(ret, 4).text()

        print(ssd, processador[0:2], frequencia_pro, geracao[0:2], ram[0:1], tela, estado)

        def avaliacao_ssd():
            if ssd != '':
                if ssd == 'SIM': return 1
                if ssd == 'NÃO': return 0

        def avaliacao_pro_gera():
            if processador[0:2] == 'I3':
                if processador[0:2] == 'I3' and geracao[0:2] == '3ª': return 0
                if processador[0:2] == 'I3' and geracao[0:2] == '4ª': return 0
                if processador[0:2] == 'I3' and geracao[0:2] == '5ª': return 0
                if processador[0:2] == 'I3' and geracao[0:2] == '6ª': return 0
                if processador[0:2] == 'I3' and geracao[0:2] == '7ª': return 1
                if processador[0:2] == 'I3' and geracao[0:2] == '8ª': return 1
                if processador[0:2] == 'I3' and geracao[0:2] == '9ª': return 1
                if processador[0:2] == 'I3' and geracao[0:3] == '10ª': return 1
                if processador[0:2] == 'I3' and geracao[0:3] == '11ª': return 1
                if processador[0:2] == 'I3' and geracao[0:3] == '12ª': return 1
                if processador[0:2] == 'I3' and geracao[0:3] == '13ª': return 1

            if processador[0:2] == 'I5':
                if processador[0:2] == 'I5' and geracao[0:2] == '3ª': return 0
                if processador[0:2] == 'I5' and geracao[0:2] == '4ª': return 0
                if processador[0:2] == 'I5' and geracao[0:2] == '5ª': return 0
                if processador[0:2] == 'I5' and geracao[0:2] == '6ª': return 1
                if processador[0:2] == 'I5' and geracao[0:2] == '7ª': return 1
                if processador[0:2] == 'I5' and geracao[0:2] == '8ª': return 1
                if processador[0:2] == 'I5' and geracao[0:2] == '9ª': return 1
                if processador[0:2] == 'I5' and geracao[0:3] == '10ª': return 1
                if processador[0:2] == 'I5' and geracao[0:3] == '11ª': return 1
                if processador[0:2] == 'I5' and geracao[0:3] == '12ª': return 1
                if processador[0:2] == 'I5' and geracao[0:3] == '13ª': return 1

            if processador[0:2] == 'I7':
                if processador[0:2] == 'I7' and geracao[0:2] == '3ª': return 0
                if processador[0:2] == 'I7' and geracao[0:2] == '4ª': return 0
                if processador[0:2] == 'I7' and geracao[0:2] == '5ª': return 1
                if processador[0:2] == 'I7' and geracao[0:2] == '6ª': return 1
                if processador[0:2] == 'I7' and geracao[0:2] == '7ª': return 1
                if processador[0:2] == 'I7' and geracao[0:2] == '8ª': return 1
                if processador[0:2] == 'I7' and geracao[0:2] == '9ª': return 1
                if processador[0:2] == 'I7' and geracao[0:3] == '10ª': return 1
                if processador[0:2] == 'I7' and geracao[0:3] == '11ª': return 1
                if processador[0:2] == 'I7' and geracao[0:3] == '12ª': return 1
                if processador[0:2] == 'I7' and geracao[0:3] == '13ª': return 1

            if processador[0:2] == 'I9':
                if processador[0:2] == 'I9' and geracao[0:2] == '3ª': return 0
                if processador[0:2] == 'I9' and geracao[0:2] == '4ª': return 0
                if processador[0:2] == 'I9' and geracao[0:2] == '5ª': return 1
                if processador[0:2] == 'I9' and geracao[0:2] == '6ª': return 1
                if processador[0:2] == 'I9' and geracao[0:2] == '7ª': return 1
                if processador[0:2] == 'I9' and geracao[0:2] == '8ª': return 1
                if processador[0:2] == 'I9' and geracao[0:2] == '9ª': return 1
                if processador[0:2] == 'I9' and geracao[0:3] == '10ª': return 1
                if processador[0:2] == 'I9' and geracao[0:3] == '11ª': return 1
                if processador[0:2] == 'I9' and geracao[0:3] == '12ª': return 1
                if processador[0:2] == 'I9' and geracao[0:3] == '13ª': return 1

        def avaliacao_ram():
            if ram[0:1] == '2': return 0
            if ram[0:1] == '4': return 0
            if ram[0:1] == '6': return 1
            if ram[0:1] == '8': return 1
            if ram[0:1] == '10': return 1
            if ram[0:1] == '12': return 1
            if ram[0:1] == '16': return 1
            if ram[0:1] == '32': return 1

        def avaliacao_tela():
            if tela != '':
                if tela == '14': return 0
                else: return 1

        def avaliacao_Estado():
            if estado == 'PÉSSIMO': return 0
            if estado == 'RUIM': return 0
            if estado == 'MÉDIO': return 0
            if estado == 'BOM': return 1
            if estado == 'ÓTIMO': return 1

        result = avaliacao_ssd(), avaliacao_pro_gera(), avaliacao_ram(), avaliacao_tela(), avaliacao_Estado()
        print(sum(result))

        if sum(result) == 5:
            mw.labelAvaliacao.setText('NÍVEL ÓTIMO')
            mw.frameNotAvaliacao.setStyleSheet('background-image: url'
        '(:/Viws/estoque/Viws/avaliacao_5.png);background-position: center; background-repeat: no-repeat;')


        if sum(result) == 4:
            mw.labelAvaliacao.setText('NÍVEL BOM')
            mw.frameNotAvaliacao.setStyleSheet('background-image: url'
        '(:/Viws/estoque/Viws/avaliacao_4.png);background-position: center; background-repeat: no-repeat;')


        if sum(result) == 3:
            mw.labelAvaliacao.setText('MEDIANO')
            mw.frameNotAvaliacao.setStyleSheet('background-image: url'
        '(:/Viws/estoque/Viws/avaliacao_3.png);background-position: center; background-repeat: no-repeat;')


        if sum(result) == 2:
            mw.labelAvaliacao.setText('NÍVEL BAIXO')
            mw.frameNotAvaliacao.setStyleSheet('background-image: url'
        '(:/Viws/estoque/Viws/avaliacao_2.png);background-position: center; background-repeat: no-repeat;')


        if sum(result) == 1:
            mw.labelAvaliacao.setText('PÉSSIMO')
            mw.frameNotAvaliacao.setStyleSheet('background-image: url'
        '(:/Viws/estoque/Viws/avaliacao_1.png);background-position: center; background-repeat: no-repeat;')

    mw.tableWidgetNotebook.itemSelectionChanged.connect(get_info_table)
    mw.ButtonNotebook.clicked.connect(informacao_Note)
    mw.notPesButton.clicked.connect(pesquisa_Note)

    # OFFICE  ----------------------------------------------------------------------------------------------------------

    def pesOffice():
        pesquisa = mw.officePes.text()

        if len(pesquisa) <= 5:

            con = db.conMySQL()
            con.execute(f"""SELECT * FROM office WHERE idOffice like '%{pesquisa}%' and LOCAL like '%estoque%';""")
            result = con.fetchall()
            print(result)

            mw.tableWidgetOffice.clearContents()
            header = mw.tableWidgetOffice.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            mw.tableWidgetOffice.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    mw.tableWidgetOffice.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        else:
            con = db.conMySQL()
            con.execute(f"""SELECT * FROM office WHERE chave like '%{pesquisa}%' and LOCAL like '%estoque%';""")
            result = con.fetchall()
            print(result)

            mw.tableWidgetOffice.clearContents()
            header = mw.tableWidgetOffice.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            mw.tableWidgetOffice.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    mw.tableWidgetOffice.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    def informacao_Off():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM office', con)
        con.close()

        total = len(result)
        office_treze = result[(result['VERSAO'] == 'Office 2013')].shape[0]
        office_dezeseis = result[(result['VERSAO'] == 'Office 2016')].shape[0]
        office_dezenove = result[(result['VERSAO'] == 'Office 2019')].shape[0]
        office_365 = result[(result['VERSAO'] == 'Office 365')].shape[0]

        print(total, office_treze, office_dezeseis, office_dezenove, office_365)

        mw.hislabel01_11.setText(str(total))
        mw.hislabel02_11.setText(str(office_treze))
        mw.hislabel03_11.setText(str(office_dezeseis))
        mw.label_382.setText(str(office_dezenove))
        mw.label_384.setText(str(office_365))

        con = db.conMySQL()
        con.execute("""select * from office;""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetOffice.clearContents()
        header = mw.tableWidgetOffice.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetOffice.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetOffice.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonOffice.clicked.connect(informacao_Off)
    mw.officePesButton.clicked.connect(pesOffice)

    # CELULAR  ---------------------------------------------------------------------------------------------------------

    def informacao_Cell():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM celular', con)
        con.close()

        total = len(result)
        mw.hislabel01_3.setText(str(total))

        con = db.conMySQL()
        con.execute("""SELECT * FROM celular""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetCelular.clearContents()
        mw.tableWidgetCelular.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetCelular.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonCelular.clicked.connect(informacao_Cell)

    # MEMORIA  ---------------------------------------------------------------------------------------------------------

    def informacao_Memo():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM memoria', con)
        con.close()

        total = len(result)

        memoria_not = result[(result['PLATAFORMA'] == 'NOTEBOOK')].shape[0]
        memoria_desk = result[(result['PLATAFORMA'] == 'DESKTOP')].shape[0]


        mw.hislabel01_4.setText(str(total))
        mw.hislabel02_4.setText(str(memoria_not))
        mw.hislabel03_4.setText(str(memoria_desk))

        con = db.conMySQL()
        con.execute("""SELECT * FROM memoria""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetMemo.clearContents()
        header = mw.tableWidgetMemo.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        mw.tableWidgetMemo.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetMemo.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonMemoria.clicked.connect(informacao_Memo)

    # DISCO  -----------------------------------------------------------------------------------------------------------

    def informacao_Disc():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM disco', con)
        con.close()

        total = len(result)
        ssd = result[(result['TIPO'] == 'SSD')].shape[0]
        hd = result[(result['TIPO'] == 'HD')].shape[0]

        mw.hislabel01_5.setText(str(total))
        mw.hislabel02_5.setText(str(ssd))
        mw.hislabel03_5.setText(str(hd))

        con = db.conMySQL()
        con.execute("""SELECT * FROM disco""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetDis.clearContents()
        header = mw.tableWidgetDis.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetDis.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetDis.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonSSD.clicked.connect(informacao_Disc)

    # MOUSE  ---------------------------------------------------------------------------------------------------------

    def informacao_Mouse():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM mouse', con)
        con.close()

        total = len(result)
        wireless = result[(result['TIPO'] == 'WIRELESS')].shape[0]
        no_wireless = result[(result['TIPO'] == 'NO-WIRELESS')].shape[0]

        mw.hislabel01_6.setText(str(total))
        mw.hislabel02_6.setText(str(wireless))
        mw.hislabel03_6.setText(str(no_wireless))

        con = db.conMySQL()
        con.execute("""SELECT * FROM mouse""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetMouse.clearContents()
        header = mw.tableWidgetMouse.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetMouse.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetMouse.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonMouse.clicked.connect(informacao_Mouse)

    # PAD  -------------------------------------------------------------------------------------------------------------

    def informacao_Pad():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM mousepad', con)
        con.close()

        total = len(result)

        mw.hislabel01_7.setText(str(total))

        con = db.conMySQL()
        con.execute("""SELECT * FROM mousepad""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetPad.clearContents()
        header = mw.tableWidgetPad.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetPad.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetPad.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonMousePad.clicked.connect(informacao_Pad)

    # TECLADO  ---------------------------------------------------------------------------------------------------------

    def informacao_Tec():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM teclado', con)
        con.close()

        total = len(result)
        wireless = result[(result['TIPO'] == 'WIRELESS')].shape[0]
        no_wireless = result[(result['TIPO'] == 'NO-WIRELESS')].shape[0]

        mw.hislabel01_8.setText(str(total))
        mw.hislabel02_8.setText(str(wireless))
        mw.hislabel03_8.setText(str(no_wireless))

        con = db.conMySQL()
        con.execute("""SELECT * FROM teclado""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetTec.clearContents()
        header = mw.tableWidgetTec.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetTec.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetTec.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonTeclado.clicked.connect(informacao_Tec)

    # SUPORTE  ---------------------------------------------------------------------------------------------------------

    def informacao_Sup():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM suporte', con)
        con.close()

        total = len(result)

        mw.hislabel01_9.setText(str(total))

        con = db.conMySQL()
        con.execute("""SELECT * FROM suporte""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetSuporte.clearContents()
        header = mw.tableWidgetSuporte.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetSuporte.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetSuporte.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonSuporte.clicked.connect(informacao_Sup)

    # MONITOR  ---------------------------------------------------------------------------------------------------------

    def informacao_Mo():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM monitor', con)
        con.close()

        total = len(result)

        mw.hislabel01_10.setText(str(total))

        con = db.conMySQL()
        con.execute("""SELECT * FROM monitor""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetEmail.clearContents()
        header = mw.tableWidgetEmail.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetEmail.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetEmail.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonEmail.clicked.connect(informacao_Mo)

    # WINDOWS  ---------------------------------------------------------------------------------------------------------

    def pesWindows():
        pesquisa = mw.windowsPes.text()

        con = db.conMySQL()
        con.execute(f"""SELECT * FROM windows WHERE chave like '%{pesquisa}%' and LOCAL like '%estoque%';""")
        result = con.fetchall()
        print(result)

        mw.tableWidgetWindows.clearContents()
        header = mw.tableWidgetWindows.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetWindows.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetWindows.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    def informacao_Win():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM windows', con)
        con.close()

        total = len(result)
        pro = result[(result['VERSAO'] == 'Windows 10')].shape[0]
        seven = result[(result['VERSAO'] == 'Windows 7')].shape[0]
        xp = result[(result['VERSAO'] == 'Windows XP')].shape[0]
        server = result[(result['VERSAO'] == 'Windows Server')].shape[0]

        mw.hislabel01_12.setText(str(total))
        mw.hislabel02_12.setText(str(pro))
        mw.hislabel03_12.setText(str(seven))
        mw.label_395.setText(str(xp))
        mw.label_397.setText(str(server))

        con = db.conMySQL()
        con.execute("""select * from windows;""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetWindows.clearContents()
        header = mw.tableWidgetWindows.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetWindows.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetWindows.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonWindows.clicked.connect(informacao_Win)
    mw.windowsPesButton.clicked.connect(pesWindows)

    # OUTROS  ----------------------------------------------------------------------------------------------------------

    def informacao_Outros():
        con = db.conPandasSQL()
        result = pd.read_sql('SELECT * FROM outros', con)
        con.close()

        total = len(result)

        mw.hislabel01_13.setText(str(total))

        con = db.conMySQL()
        con.execute("""SELECT * FROM outros""")
        result = con.fetchall()
        con.close()

        mw.tableWidgetOutros.clearContents()
        header = mw.tableWidgetOutros.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetOutros.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetOutros.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.ButtonOutros.clicked.connect(informacao_Outros)



    #  Acionamento Botões de icones de TABELA --------------------------------------------------------------------------

    mw.ButtonNotebook.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageNotebook))
    mw.ButtonCelular.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageCelular))
    mw.ButtonMemoria.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMemoria))
    mw.ButtonSSD.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageDisco))
    mw.ButtonMouse.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMouse))
    mw.ButtonMousePad.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pagePad))
    mw.ButtonTeclado.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageTeclado))
    mw.ButtonSuporte.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageSuporte))
    mw.ButtonEmail.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMonitor))
    mw.ButtonOffice.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageOffice))
    mw.ButtonWindows.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageWindows))
    mw.ButtonOutros.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageOutros))













    # TRATAMENTO PAGE ENTRADA ESTOQUE ----------------------------------------------------------------------------------
    def pesEntrada():
        boxTipo = mw.entradaComboBoxTipo.currentText()
        boxCampo = mw.entradaComboBoxCampo.currentText()
        inputUser = mw.entradalineEditPes.text()

        print(boxTipo, boxCampo, inputUser)

        if boxTipo == '' or boxCampo == '' or inputUser == '':
            mw.entradaComboBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193);')
            mw.entradaComboBoxCampo.setStyleSheet('background-color: rgb(255, 192, 193);')
            mw.entradalineEditPes.setStyleSheet('background-color: rgb(255, 192, 193);')

            texto = 'Campos obrigatórios não preenchidos'
            mw.entradalabelDialog.setText(texto)

        else:
            mw.entradaComboBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.entradaComboBoxCampo.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.entradalineEditPes.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.entradalabelDialog.clear()

            tabela = tabCod()[0]
            coluna = tabCod()[1]
            print(tabela, coluna)

            if boxCampo == 'CÓDIGO':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE idOffice LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE idWindows LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {tabela}
                                        WHERE {coluna} LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'MARCA':
                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE VERSAO LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE VERSAO LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE MARCA LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'CHAVE':
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT {coluna}, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA
                                    FROM {boxTipo}
                                    WHERE CHAVE LIKE '%{inputUser}%'""")
                    result = con.fetchall()
                    print(result)

                    mw.entradaTableWidget.clearContents()
                    header = mw.entradaTableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    mw.entradaTableWidget.setRowCount(
                        len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                    for row, text in enumerate(result):
                        for column, data in enumerate(text):
                            mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                    con.close()

                except pymysql.Error as erro:
                    texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                    # mw.entradalabelDialog.setText(texto)
                    print(str(erro) + texto)

            if boxCampo == 'LOCAL':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE LOCAL LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE LOCAL LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE LOCAL LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'DATA':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE DATA LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        #mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE DATA LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.entradaTableWidget.clearContents()
                        header = mw.entradaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.entradaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                    FROM {boxTipo}
                                    WHERE DATA LIKE '%{inputUser}%'""")
                    result = con.fetchall()
                    print(result)

                    mw.entradaTableWidget.clearContents()
                    header = mw.entradaTableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    mw.entradaTableWidget.setRowCount(
                        len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                    for row, text in enumerate(result):
                        for column, data in enumerate(text):
                            mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                    con.close()

                except pymysql.Error as erro:
                    texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                    mw.entradalabelDialog.setText(texto)
                    print(str(erro) + texto)

    def tabCod():
        teste = mw.entradaComboBoxTipo.currentText().lower()

        if teste == 'celular':
            ret = ('celular', 'idCelular')
            return ret

        if teste == 'computer':
            ret = ('computer', 'idComputer')
            return ret

        if teste == 'disco':
            ret = ('disco', 'idDisco')
            return ret

        if teste == 'memoria':
            ret = ('memoria', 'idMemoria')
            return ret

        if teste == 'monitor':
            ret = ('monitor', 'idMonitor')
            return ret

        if teste == 'mouse':
            ret = ('mouse', 'idMouse')
            return ret

        if teste == 'mousepad':
            ret = ('mousepad', 'idMousePad')
            return ret

        if teste == 'office':
            ret = ('office', 'idOffice')
            return ret

        if teste == 'outros':
            ret = ('outros', 'idOutros')
            return ret

        if teste == 'suporte':
            ret = ('suporte', 'idSuporte')
            return ret

        if teste == 'windows':
            ret = ('windows', 'idWindows')
            return ret

        else:
            teste = None
            return teste

    def motiEntrada():

        if mw.entradaRadioTransferencia.isChecked() == True:
            ret = mw.entradaRadioTransferencia.text()
            return ret

        elif mw.entradaRadioDevolucao.isChecked() == True:
            ret = mw.entradaRadioDevolucao.text()
            return ret

        elif mw.entradaRadioManutencao.isChecked() == True:
            ret = mw.entradaRadioManutencao.text()
            return ret

        elif mw.entradaRadioDeposito.isChecked() == True:
            ret = mw.entradaRadioDeposito.text()
            return ret

        elif mw.entradaRadioRecolhimento.isChecked() == True:
            ret = mw.entradaRadioRecolhimento.text()
            return ret

        elif mw.entradaRadioOutro.isChecked() == True:
            ret = mw.entradaRadioOutro.text()
            return ret

        else:
            return None

    def addItem():
        get = getIDTable()
        pic = getIDCod()[0:2]
        print(get, pic)

        # Teclado 21000
        if pic == '21':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 960.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Suporte 20000
        elif pic == '20':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 961.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Memoria 19000
        elif pic == '19':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 957.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Disco 18000
        elif pic == '18':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 958.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Celular 17000
        elif pic == '17':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 950.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet('background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Monitor 16000
        elif pic == '16':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 952.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Mouse 15000
        elif pic == '15':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 956.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # MousePad 14000
        elif pic == '14':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 959.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Windows 13000
        elif pic == '13':
            mw.entradaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 955.png);\n'
                                                     ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet('background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Office 12000
        elif pic == '12':
            mw.entradaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 954.png);\n'
                                                     ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet('background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Desktop Notebook 11000
        elif pic == '11':
            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 951.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Outros 10000
        elif pic == '10':
            mw.entradaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                                                     ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet('background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        else:
            print('Não entrou na condicional')

            mw.entradaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.entradaTableWidget.item(get, 0).text()
            tipo = mw.entradaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.entradaTableWidget.item(get, 2).text()
            modelo = mw.entradaTableWidget.item(get, 3).text()
            local = mw.entradaTableWidget.item(get, 4).text()
            preco = mw.entradaTableWidget.item(get, 5).text()

            mw.entradalabelCod.setText(cod)
            mw.entradalabelMarca.setText(marca)
            mw.entradalabelModelo.setText(modelo)
            mw.entradalabelLocal.setText(local)
            mw.entradalabelPreco.setText(preco)

            mw.entradaFrameItem.setStyleSheet('background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

    def getIDTable():
        ret = mw.entradaTableWidget.currentRow()
        return ret

    def getIDCod():
        ret = mw.entradaTableWidget.item(getIDTable(), 0)
        return ret.text() if not ret is None else ret

    def limpPageEntrada():
        try:
            con = db.conMySQL()
            con.execute(f"""SELECT idCelular, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                            FROM celular
                            WHERE LOCAL LIKE '500000'""")
            result = con.fetchall()
            print(result)

            mw.entradaTableWidget.clearContents()
            header = mw.entradaTableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            mw.entradaTableWidget.setRowCount(
                len(result))  # <-- Numeros de linhas conforme quantidade da tabela

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    mw.entradaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        except:
            print('Limpeza falhou')

        mw.entradalineEditPes.clear()
        mw.entradaComboBoxTipo.setCurrentIndex(0)
        mw.entradaComboBoxCampo.setCurrentIndex(0)

        mw.entradalabelCod.setText('----')
        mw.entradalabelMarca.setText('----')
        mw.entradalabelModelo.setText('----')
        mw.entradalabelLocal.setText('----')
        mw.entradalabelPreco.setText('----')

        mw.entradaComboBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.entradaComboBoxCampo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.entradalineEditPes.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.entradalabelDialog.clear()
        mw.entradaFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255); border-radius: 10px;')
        mw.entradaFrameItem.setStyleSheet('background-color:rgb(7, 183, 168);border: 1px;border-radius: 10px;')
        mw.entradaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
            ';background-position:center;background-repeat: no-repeat;')

    def movEstoque():
        cod = mw.entradalabelCod.text()
        motivo = motiEntrada()

        print(cod, motivo)

        if cod == '----' or motivo == None:
            mw.entradaFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 118, 118); border-radius: 10px;')
            mw.entradaFrameItem.setStyleSheet('background-color:rgb(255, 118, 118);border: 1px;border-radius: 10px;')

            texto = 'Campos obrigatórios não preenchidos'
            mw.entradalabelDialog.setText(texto)

        else:
            tipo = mw.entradaComboBoxTipo.currentText()
            marca = mw.entradalabelMarca.text()
            modelo = mw.entradalabelModelo.text()
            local = 'ESTOQUE'
            data = datAT()

            DialogiEstoqueEntrada.show()
            texto = f'DESEJA REALMENTE DA ENTRADA NO ITEM\n {tipo} ID {cod} NO ESTOQUE TI'
            de.LabelDialogMsg.setText(texto)

            def sim():
                if tabCod() is not None:
                    tabela = tabCod()[0]
                    coluna = tabCod()[1]
                    print(tabela, coluna)
                    print(marca, modelo, local, data, motivo, tipo)

                    try:
                        con = db.conMySQL()
                        con.execute(f"""UPDATE {tabela} SET `LOCAL` = 'ESTOQUE' WHERE (`{coluna}` = '{cod}');""")

                        con.execute(f"""INSERT INTO historico VALUES ('{Usuario}','ENT. ESTOQUE TI','{tipo}','{cod}',
                                        '{marca}','{modelo}','{motivo}','{local}','{data}');""")

                        DialogiEstoqueEntrada.close()
                        Positive.show()
                        po.LabelDialog.setText('TRANSAÇÃO REALIZADA COM SUCESSO!')
                        con.close()
                        limpPageEntrada()

                    except: # pymysql.Error as erro:
                        # texto = f'Erro SQL:{str(erro)[1:5]}'
                        # mw.entradalabelDialog.setText(texto)
                        # print(str(erro) + texto)
                        print('deu ruim')

                else:
                    DialogiEstoqueEntrada.close()

            def nao():
                DialogiEstoqueEntrada.close()

            de.pushButtonSim.clicked.connect(sim)
            de.pushButtonNao.clicked.connect(nao)

    def cancelEntrad():
        limpPageEntrada()
        mw.stackedWidget.setCurrentWidget(mw.PageGestao)

    mw.entradaButtonBuscar.clicked.connect(pesEntrada)
    mw.entradaTableWidget.itemSelectionChanged.connect(addItem)
    mw.entradabuttonLimpar.clicked.connect(limpPageEntrada)
    mw.entradabuttonCancel.clicked.connect(cancelEntrad)
    mw.entradabuttonConfirmar.clicked.connect(movEstoque)


#   TRATAMENTO PAGE SAIDA ESTOQUE ----------------------------------------------------------------------------------
    def pesSaida():
        boxTipo = mw.saidaComboBoxTipo.currentText()
        boxCampo = mw.saidaComboBoxCampo.currentText()
        inputUser = mw.saidalineEditPes.text()

        print(boxTipo, boxCampo, inputUser)

        if boxTipo == '' or boxCampo == '' or inputUser == '':
            mw.saidaComboBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193);')
            mw.saidaComboBoxCampo.setStyleSheet('background-color: rgb(255, 192, 193);')
            mw.saidalineEditPes.setStyleSheet('background-color: rgb(255, 192, 193);')

            texto = 'Campos obrigatórios não preenchidos'
            mw.saidalabelDialog.setText(texto)

        else:
            mw.saidaComboBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.saidaComboBoxCampo.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.saidalineEditPes.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.saidalabelDialog.clear()

            tabela = tabCodSaida()[0]
            coluna = tabCodSaida()[1]
            print(tabela, coluna)

            if boxCampo == 'CÓDIGO':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE idOffice LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE idWindows LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {tabela}
                                        WHERE {coluna} LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.saidalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'MARCA':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE VERSAO LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE VERSAO LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE MARCA LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.saidalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'CHAVE':
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT {coluna}, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA
                                    FROM {boxTipo}
                                    WHERE CHAVE LIKE '%{inputUser}%'""")
                    result = con.fetchall()
                    print(result)

                    mw.saidaTableWidget.clearContents()
                    header = mw.saidaTableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    mw.saidaTableWidget.setRowCount(
                        len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                    for row, text in enumerate(result):
                        for column, data in enumerate(text):
                            mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                    con.close()

                except pymysql.Error as erro:
                    texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                    # mw.entradalabelDialog.setText(texto)
                    print(str(erro) + texto)

            if boxCampo == 'LOCAL':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE LOCAL LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE LOCAL LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE LOCAL LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.saidalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'DATA':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM office
                                        WHERE DATA LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        #mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                        FROM windows
                                        WHERE DATA LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        # mw.entradalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE DATA LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.saidaTableWidget.clearContents()
                        header = mw.saidaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.saidaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.saidalabelDialog.setText(texto)
                        print(str(erro) + texto)

            else:
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                    FROM {boxTipo}
                                    WHERE DATA LIKE '%{inputUser}%'""")
                    result = con.fetchall()
                    print(result)

                    mw.saidaTableWidget.clearContents()
                    header = mw.saidaTableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    mw.saidaTableWidget.setRowCount(
                        len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                    for row, text in enumerate(result):
                        for column, data in enumerate(text):
                            mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                    con.close()

                except pymysql.Error as erro:
                    texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                    mw.saidalabelDialog.setText(texto)
                    print(str(erro) + texto)

    def tabCodSaida():
        teste = mw.saidaComboBoxTipo.currentText().lower()

        if teste == 'celular':
            ret = ('celular', 'idCelular')
            return ret

        if teste == 'computer':
            ret = ('computer', 'idComputer')
            return ret

        if teste == 'disco':
            ret = ('disco', 'idDisco')
            return ret

        if teste == 'memoria':
            ret = ('memoria', 'idMemoria')
            return ret

        if teste == 'monitor':
            ret = ('monitor', 'idMonitor')
            return ret

        if teste == 'mouse':
            ret = ('mouse', 'idMouse')
            return ret

        if teste == 'mousepad':
            ret = ('mousepad', 'idMousePad')
            return ret

        if teste == 'office':
            ret = ('office', 'idOffice')
            return ret

        if teste == 'outros':
            ret = ('outros', 'idOutros')
            return ret

        if teste == 'suporte':
            ret = ('suporte', 'idSuporte')
            return ret

        if teste == 'windows':
            ret = ('windows', 'idWindows')
            return ret

        else:
            teste = None
            return teste

    def motiSaida():

        if mw.saidaRadiodefinitivo.isChecked() == True:
            ret = mw.saidaRadiodefinitivo.text()
            return ret

        elif mw.saidaRadioProvisorio.isChecked() == True:
            ret = mw.saidaRadioProvisorio.text()
            return ret

        elif mw.saidaRadioManutencao.isChecked() == True:
            ret = mw.saidaRadioManutencao.text()
            return ret

        elif mw.saidaRadioTreinamento.isChecked() == True:
            ret = mw.saidaRadioTreinamento.text()
            return ret

        elif mw.saidaRadioOutro.isChecked() == True:
            ret = mw.saidaRadioOutro.text()
            return ret

        else:
            return None

    def addItemSaida():
        get = getIDTableSaida()
        pic = getIDCodSaida()[0:2]
        print(get, pic)

        # Teclado 21000
        if pic == '21':
            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 960.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.saidaButtonDestino.setStyleSheet('background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
            'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

        # Suporte 20000
        elif pic == '20':
            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 961.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

        # Memoria 19000
        elif pic == '19':
            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 978.png);\n'
                'background-position:center; background-repeat: no-repeat;')
            mw.saidaUser.setText('COMPUTER')
            mw.label_64.setText('Marca:')
            mw.label_65.setText('Código:')

            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 957.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Disco 18000
        elif pic == '18':
            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 978.png);\n'
                'background-position:center; background-repeat: no-repeat;')
            mw.saidaUser.setText('COMPUTER')
            mw.label_64.setText('Marca:')
            mw.label_65.setText('Código:')

            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 958.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Celular 17000
        elif pic == '17':
            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 950.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

        # Monitor 16000
        elif pic == '16':
            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 952.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

        # Mouse 15000
        elif pic == '15':
            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 956.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

        # MousePad 14000
        elif pic == '14':
            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 959.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

        # Windows 13000
        elif pic == '13':

            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 978.png);\n'
                'background-position:center; background-repeat: no-repeat;')
            mw.saidaUser.setText('COMPUTER')
            mw.label_64.setText('Marca:')
            mw.label_65.setText('Código:')

            mw.saidaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 955.png);\n'
                                                     ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Office 12000
        elif pic == '12':
            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 978.png);\n'
                'background-position:center; background-repeat: no-repeat;')
            mw.saidaUser.setText('COMPUTER')
            mw.label_64.setText('Marca:')
            mw.label_65.setText('Código:')

            mw.saidaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 954.png);\n'
                                                     ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Desktop Notebook 11000
        elif pic == '11':
            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                'background-position:center;background-repeat: no-repeat;')
            mw.saidaUser.setText('USER')
            mw.label_64.setText('Nome:')
            mw.label_65.setText('Código:')

            mw.saidaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 951.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        # Outros 10000
        elif pic == '10':
            mw.saidaButtonDestino.setStyleSheet(
                'background-image: url(:/saida/estoque/entrada e saida/Grupo 979.png);\n'
                'background-position:center; background-repeat: no-repeat;')
            mw.saidaUser.setText('DESTINO')
            mw.label_64.setText('PA:')
            mw.label_65.setText('Código:')

            mw.saidaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                                                     ';background-position:center;background-repeat: no-repeat;')
            cod = mw.saidaTableWidget.item(get, 0).text()
            tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.saidaTableWidget.item(get, 2).text()
            modelo = mw.saidaTableWidget.item(get, 3).text()
            local = mw.saidaTableWidget.item(get, 4).text()
            preco = mw.saidaTableWidget.item(get, 5).text()

            mw.saidalabelCod.setText(cod)
            mw.saidalabelMarca.setText(marca)
            mw.saidalabelModelo.setText(modelo)
            mw.saidalabelLocal.setText(local)
            mw.saidalabelPreco.setText(preco)

            mw.saidaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

        else:
            # Perifericos e Itens do colaborador
            if pic == '21' or '20' or '17' or '16' or '15' or '14' or '11':
                mw.saidaButtonDestino.setStyleSheet(
                    'background-image: url(:/saida/estoque/entrada e saida/Grupo 491.png);\n'
                    'background-position:center;background-repeat: no-repeat;')
                mw.saidaUser.setText('USER')
                mw.label_64.setText('Nome:')
                mw.label_65.setText('Código:')

                mw.saidaFrameItemPicture.setStyleSheet(
                    'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                    ';background-position:center;background-repeat: no-repeat;')
                cod = mw.saidaTableWidget.item(get, 0).text()
                tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
                marca = mw.saidaTableWidget.item(get, 2).text()
                modelo = mw.saidaTableWidget.item(get, 3).text()
                local = mw.saidaTableWidget.item(get, 4).text()
                preco = mw.saidaTableWidget.item(get, 5).text()

                mw.saidalabelCod.setText(cod)
                mw.saidalabelMarca.setText(marca)
                mw.saidalabelModelo.setText(modelo)
                mw.saidalabelLocal.setText(local)
                mw.saidalabelPreco.setText(preco)

                mw.saidaFrameItem.setStyleSheet(
                    'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            # Itens do computador
            if pic == '12' or '13' or '19' or '18':
                mw.saidaButtonDestino.setStyleSheet(
                    'background-image: url(:/saida/estoque/entrada e saida/Grupo 978.png);\n'
                    'background-position:center; background-repeat: no-repeat;')
                mw.saidaUser.setText('COMPUTER')
                mw.label_64.setText('Marca:')
                mw.label_65.setText('Código:')

                mw.saidaFrameItemPicture.setStyleSheet(
                    'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                    ';background-position:center;background-repeat: no-repeat;')
                cod = mw.saidaTableWidget.item(get, 0).text()
                tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
                marca = mw.saidaTableWidget.item(get, 2).text()
                modelo = mw.saidaTableWidget.item(get, 3).text()
                local = mw.saidaTableWidget.item(get, 4).text()
                preco = mw.saidaTableWidget.item(get, 5).text()

                mw.saidalabelCod.setText(cod)
                mw.saidalabelMarca.setText(marca)
                mw.saidalabelModelo.setText(modelo)
                mw.saidalabelLocal.setText(local)
                mw.saidalabelPreco.setText(preco)

                mw.saidaFrameItem.setStyleSheet(
                    'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            # Itens local ou setor
            if pic == '10':
                mw.saidaButtonDestino.setStyleSheet(
                    'background-image: url(:/saida/estoque/entrada e saida/Grupo 979.png);\n'
                    'background-position:center; background-repeat: no-repeat;')
                mw.saidaUser.setText('DESTINO')
                mw.label_64.setText('PA:')
                mw.label_65.setText('Código:')

                mw.saidaFrameItemPicture.setStyleSheet(
                    'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                    ';background-position:center;background-repeat: no-repeat;')
                cod = mw.saidaTableWidget.item(get, 0).text()
                tipo = mw.saidaTableWidget.item(get, 1).text().upper()[0:15]
                marca = mw.saidaTableWidget.item(get, 2).text()
                modelo = mw.saidaTableWidget.item(get, 3).text()
                local = mw.saidaTableWidget.item(get, 4).text()
                preco = mw.saidaTableWidget.item(get, 5).text()

                mw.saidalabelCod.setText(cod)
                mw.saidalabelMarca.setText(marca)
                mw.saidalabelModelo.setText(modelo)
                mw.saidalabelLocal.setText(local)
                mw.saidalabelPreco.setText(preco)

                mw.saidaFrameItem.setStyleSheet(
                    'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

    def getIDTableSaida():
        ret = mw.saidaTableWidget.currentRow()
        return ret

    def getIDCodSaida():
        ret = mw.saidaTableWidget.item(getIDTableSaida(), 0)
        return ret.text() if not ret is None else ret

    def limpPageSaida():
        try:
            con = db.conMySQL()
            con.execute(f"""SELECT idCelular, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                            FROM celular
                            WHERE LOCAL LIKE '500000'""")
            result = con.fetchall()
            print(result)

            mw.saidaTableWidget.clearContents()
            header = mw.saidaTableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            mw.saidaTableWidget.setRowCount(
                len(result))  # <-- Numeros de linhas conforme quantidade da tabela

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    mw.saidaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        except:
            print('Limpeza falhou')

        mw.saidalineEditPes.clear()
        mw.saidaComboBoxTipo.setCurrentIndex(0)
        mw.saidaComboBoxCampo.setCurrentIndex(0)

        mw.saidalabelCod.setText('----')
        mw.saidalabelMarca.setText('----')
        mw.saidalabelModelo.setText('----')
        mw.saidalabelLocal.setText('----')
        mw.saidalabelPreco.setText('----')

        mw.saidaComboBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.saidaComboBoxCampo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.saidalineEditPes.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.saidalabelDialog.clear()
        mw.saidaFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255); border-radius: 10px;')
        mw.saidaFrameItem.setStyleSheet('background-color:rgb(7, 183, 168);border: 1px;border-radius: 10px;')
        mw.saidaFrameItemPicture.setStyleSheet('background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
            ';background-position:center;background-repeat: no-repeat;')
        mw.saidaFrameDestino.setStyleSheet('background-color:rgb(7, 183, 168);border: 1px;border-radius: 10px;')

    def saidaDestino():
        # cod = mw.saidaUser.text()
        # print(type(cod), cod)

        # Perifericos e Itens do colaborador
        if mw.saidaUser.text() == 'USER':
            opSaidaEstoqueTI.close()
            opSaidaEstoqueTI.show()
            ops.stackedWidget.setCurrentWidget(ops.pageOpUser)

            def pUser():
                user = ops.opLineUser.text()
                print(user + '<--- entrada do usuario')

                if user == '':
                    texto = 'Campo de pesquisa em branco \nPor favor preencha o campo de pesquisa de usuario'
                    ops.opLineUser.setStyleSheet('background-color: rgb(255, 192, 193);')
                    ops.opLabelUser.setText(texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT * FROM colaborador WHERE nome like '%{user}%';""")
                        dados = con.fetchall()
                        print(dados)

                        if dados == ():
                            texto = 'Usuário não encontrado\n certifique se de que o mesmo esta cadastrado'
                            ops.opLabelUser.setText(texto)

                        else:
                            nome = dados[0][1]
                            cargo = dados[0][4]
                            idu = dados[0][0]

                            texto = 'COLABORADOR ENCONTRADO'
                            mw.saidaFrameDestino.setStyleSheet(
                                'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mw.saidaCargoUser.setText(nome)
                            mw.saidaCodUser.setText(str(idu))

                            Positive.show()
                            ops.opLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opSaidaEstoqueTI.close()

                            return nome

                    except:
                        texto = 'Colaborador Não Encontrado'
                        dg.LabelDialog.setText(texto)
                        Dialog.show()
                        return None

            ops.opButtonUser.clicked.connect(pUser)

        # Itens do computador
        if mw.saidaUser.text() == 'COMPUTER':
            print('entrou computer')
            opSaidaEstoqueTI.close()
            opSaidaEstoqueTI.show()
            ops.stackedWidget.setCurrentWidget(ops.pageComputer)
            ops.opLineCom.setStyleSheet('background-color: rgb(255, 255, 255);border:1px; border-radius: 10px')

            def maq():
                imputUser = ops.opLineCom.text()

                if imputUser == '':
                    texto = 'Preencha o campo de pesquisa'
                    ops.opLineCom.setStyleSheet('background-color: rgb(255, 184, 185);border:1px; border-radius: 10px')
                    ops.opLabelCom.setText(texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT * FROM computer WHERE idComputer like '%{imputUser}%';""")
                        result = con.fetchall()

                        if result == ():
                            texto = 'MAQUINA NÃO ENCONTRADA!\n Certifique-se de que a maquina esta\n Devidamente cadastrada.'
                            Dialog.show()
                            dg.LabelDialog.setText(texto)
                            ops.opLabelCom.setText('Certifique-se de que a maquina esta\n Devidamente cadastrada.')

                        else:
                            print(result)
                            cod = result[0][0]
                            marca = result[0][2]
                            modelo = result[0][3]
                            print(cod, marca, modelo)

                            texto = f'MAQUINA {marca} {modelo} LOCALIZADA\n CÓDIGO {cod}.'
                            mw.saidaFrameDestino.setStyleSheet(
                                'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mw.saidaCargoUser.setText(marca)
                            mw.saidaCodUser.setText(str(cod))

                            Positive.show()
                            ops.opLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opSaidaEstoqueTI.close()

                    except:
                        print('Algo deu errado ao localizar computer em saida ')

            ops.opButtonCom.clicked.connect(maq)

        # Itens local ou setor
        if mw.saidaUser.text() == 'DESTINO':
            opSaidaEstoqueTI.close()
            opSaidaEstoqueTI.show()
            ops.stackedWidget.setCurrentWidget(ops.pageOpLocal)

            def local():
                local = ops.opBoxLocal.currentText()

                texto = 'Local Selecionado'
                mw.saidaFrameDestino.setStyleSheet(
                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                mw.saidaCargoUser.setText(local)
                mw.saidaCodUser.setText('01')

                Positive.show()
                ops.opLineUser.clear()
                po.LabelDialog.setText(texto)
                opSaidaEstoqueTI.close()

            ops.opButtonLocal.clicked.connect(local)

        else:
            print('?')

    def movEstoqueSaida():
        codItem = mw.saidalabelCod.text()
        motivo = motiSaida()
        codDestino = mw.saidaCodUser.text()

        print(codItem, motivo, codDestino)

        if codItem == '----' or motivo == None or codDestino == '----------':
            mw.saidaFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 118, 118); border-radius: 10px;')
            mw.saidaFrameItem.setStyleSheet('background-color:rgb(255, 118, 118);border: 1px;border-radius: 10px;')
            mw.saidaFrameDestino.setStyleSheet('background-color:rgb(255, 118, 118);border: 1px;border-radius: 10px;')

            texto = 'Campos obrigatórios não preenchidos'
            mw.saidalabelDialog.setText(texto)

        else:
            pic = mw.saidaUser.text()
            print(pic)

            # --------------- Item --------------------
            tipo = mw.saidaComboBoxTipo.currentText()
            marca = mw.saidalabelMarca.text()
            modelo = mw.saidalabelModelo.text()
            local = mw.saidaCargoUser.text()
            data = datAT()

            # --------------- Destino ------------------
            cod = mw.saidaCodUser.text()

            # Itens do colaborador
            if mw.saidaUser.text() == 'USER':

                DialogiEstoqueSaida.show()
                texto = f'DESEJA REALMENTE DA SAIDA NO ITEM\n {tipo} ID {codItem} DO ESTOQUE TI'
                ds.LabelDialogMsg.setText(texto)

                def sim():
                    if tabCodSaida() is not None:
                        tabela = tabCodSaida()[0]
                        coluna = tabCodSaida()[1]
                        print(tabela, coluna)
                        print(marca, modelo, local, data, motivo, tipo)

                        try:
                            con = db.conMySQL()
                            con.execute(
                                f"""UPDATE colaborador SET {coluna} = '{codItem}' WHERE (`idColaborador` = '{cod}');""")

                            con.execute(
                                f"""INSERT INTO historico VALUES ('{Usuario}','SAIDA. ESTOQUE TI','{tipo}','{cod}',
                                                                '{marca}','{modelo}','{motivo}','{local}','{data}');""")

                            DialogiEstoqueSaida.close()
                            Positive.show()
                            po.LabelDialog.setText('TRANSAÇÃO REALIZADA COM SUCESSO!')
                            con.close()
                            limpPageSaida()

                        except pymysql.Error as erro:
                            texto = f'Erro SQL:{str(erro)[1:5]}'
                            mw.saidalabelDialog.setText(texto)
                            print(str(erro) + texto)
                            print('deu ruim')

                    else:
                        DialogiEstoqueSaida.close()
                        print('algo errado no salvamento em colaborador')

                def nao():
                    DialogiEstoqueSaida.close()

                ds.pushButtonSim.clicked.connect(sim)
                ds.pushButtonNao.clicked.connect(nao)

            # Itens do computador
            if mw.saidaUser.text() == 'COMPUTER':

                DialogiEstoqueSaida.show()
                texto = f'DESEJA REALMENTE DA SAIDA NO ITEM\n {tipo} ID {codItem} DO ESTOQUE TI'
                ds.LabelDialogMsg.setText(texto)

                def sim():
                    if tabCodSaida() is not None:
                        tabela = tabCodSaida()[0]
                        coluna = tabCodSaida()[1]
                        print(tabela, coluna)
                        print(marca, modelo, local, data, motivo, tipo)

                        try:
                            con = db.conMySQL()
                            con.execute(f"""UPDATE computer SET {coluna} = '{codItem}' WHERE (`idComputer` = '{cod}');""")

                            con.execute(f"""INSERT INTO historico VALUES ('{Usuario}','SAIDA. ESTOQUE TI','{tipo}','{cod}',
                                                        '{marca}','{modelo}','{motivo}','{local}','{data}');""")

                            DialogiEstoqueSaida.close()
                            Positive.show()
                            po.LabelDialog.setText('TRANSAÇÃO REALIZADA COM SUCESSO!')
                            con.close()
                            limpPageSaida()

                        except:  # pymysql.Error as erro:
                            # texto = f'Erro SQL:{str(erro)[1:5]}'
                            # mw.entradalabelDialog.setText(texto)
                            # print(str(erro) + texto)
                            print('deu ruim')

                    else:
                        DialogiEstoqueSaida.close()

                def nao():
                    DialogiEstoqueSaida.close()

                ds.pushButtonSim.clicked.connect(sim)
                ds.pushButtonNao.clicked.connect(nao)

            # Itens local ou setor
            if mw.saidaUser.text() == 'DESTINO':
                item = mw.saidalabelMarca.text()

                DialogiEstoqueSaida.show()
                texto = f'DESEJA REALMENTE DA SAIDA NO ITEM\n {item} ID {codItem} DO ESTOQUE TI'
                ds.LabelDialogMsg.setText(texto)

                def sim():
                    if tabCodSaida() is not None:
                        tabela = tabCodSaida()[0]
                        coluna = tabCodSaida()[1]
                        print(tabela, coluna)
                        print(marca, modelo, local, data, motivo, tipo)

                        try:
                            con = db.conMySQL()
                            con.execute(f"""UPDATE {tabela} SET `LOCAL` = '{local}' WHERE (`{coluna}` = '{codItem}');""")

                            con.execute(f"""INSERT INTO historico VALUES ('{Usuario}','SAIDA. ESTOQUE TI','{item}','{cod}',
                                                        '{marca}','{modelo}','{motivo}','{local}','{data}');""")

                            DialogiEstoqueSaida.close()
                            Positive.show()
                            po.LabelDialog.setText('TRANSAÇÃO REALIZADA COM SUCESSO!')
                            con.close()
                            limpPageSaida()

                        except pymysql.Error as erro:
                            texto = f'Erro SQL:{str(erro)[1:5]}'
                            mw.saidalabelDialog.setText(texto)
                            print(str(erro) + texto)
                            print('deu ruim')

                    else:
                        DialogiEstoqueSaida.close()

                def nao():
                    DialogiEstoqueSaida.close()

                ds.pushButtonSim.clicked.connect(sim)
                ds.pushButtonNao.clicked.connect(nao)

    def cancelSaida():
        limpPageSaida()
        mw.stackedWidget.setCurrentWidget(mw.PageGestao)

    mw.saidaButtonDestino.clicked.connect(saidaDestino)
    mw.saidaButtonBuscar.clicked.connect(pesSaida)
    mw.saidaTableWidget.itemSelectionChanged.connect(addItemSaida)
    mw.saidabuttonLimpar.clicked.connect(limpPageSaida)
    mw.saidabuttonCancel.clicked.connect(cancelSaida)
    mw.saidabuttonConfirmar.clicked.connect(movEstoqueSaida)

    #   TRATAMENTO PAGE SAIDA ESTOQUE ----------------------------------------------------------------------------------
    def pesBaixa():
        boxTipo = mw.baixaComboBoxTipo.currentText()
        boxCampo = mw.baixaComboBoxCampo.currentText()
        inputUser = mw.baixalineEditPes.text()

        print(boxTipo, boxCampo, inputUser)

        if boxTipo == '' or boxCampo == '' or inputUser == '':
            mw.baixaComboBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193);')
            mw.baixaComboBoxCampo.setStyleSheet('background-color: rgb(255, 192, 193);')
            mw.baixalineEditPes.setStyleSheet('background-color: rgb(255, 192, 193);')

            texto = 'Campos obrigatórios não preenchidos'
            mw.baixalabelDialog.setText(texto)

        else:
            mw.baixaComboBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.baixaComboBoxCampo.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.baixalineEditPes.setStyleSheet('background-color: rgb(255, 255, 255);')
            mw.baixalabelDialog.clear()

            tabela = tabCodBaixa()[0]
            coluna = tabCodBaixa()[1]
            print(tabela, coluna)

            if boxCampo == 'CÓDIGO':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM office
                                            WHERE idOffice LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM windows
                                            WHERE idWindows LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                            FROM {tabela}
                                            WHERE {coluna} LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'MARCA':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM office
                                            WHERE VERSAO LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM windows
                                            WHERE VERSAO LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                            FROM {boxTipo}
                                            WHERE MARCA LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'CHAVE':
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT {coluna}, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE CHAVE LIKE '%{inputUser}%'""")
                    result = con.fetchall()
                    print(result)

                    mw.baixaTableWidget.clearContents()
                    header = mw.baixaTableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    mw.baixaTableWidget.setRowCount(
                        len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                    for row, text in enumerate(result):
                        for column, data in enumerate(text):
                            mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                    con.close()

                except pymysql.Error as erro:
                    texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                    mw.baixalabelDialog.setText(texto)
                    print(str(erro) + texto)

            if boxCampo == 'LOCAL':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM office
                                            WHERE LOCAL LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM windows
                                            WHERE LOCAL LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                            FROM {boxTipo}
                                            WHERE LOCAL LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

            if boxCampo == 'DATA':

                if tabela == 'office':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idOffice, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM office
                                            WHERE DATA LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                if tabela == 'windows':
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT idWindows, CHAVE, VERSAO, VERSAOPRO, LOCAL, VALOR, DATA 
                                            FROM windows
                                            WHERE DATA LIKE '%{inputUser}%'""")

                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()


                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

                else:
                    try:
                        con = db.conMySQL()
                        con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                            FROM {boxTipo}
                                            WHERE DATA LIKE '%{inputUser}%'""")
                        result = con.fetchall()
                        print(result)

                        mw.baixaTableWidget.clearContents()
                        header = mw.baixaTableWidget.horizontalHeader()
                        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                        mw.baixaTableWidget.setRowCount(
                            len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                        for row, text in enumerate(result):
                            for column, data in enumerate(text):
                                mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                        con.close()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)

            else:
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT {coluna}, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                        FROM {boxTipo}
                                        WHERE DATA LIKE '%{inputUser}%'""")
                    result = con.fetchall()
                    print(result)

                    mw.baixaTableWidget.clearContents()
                    header = mw.baixaTableWidget.horizontalHeader()
                    header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
                    mw.baixaTableWidget.setRowCount(
                        len(result))  # <-- Numeros de linhas conforme quantidade da tabela

                    for row, text in enumerate(result):
                        for column, data in enumerate(text):
                            mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

                    con.close()

                except pymysql.Error as erro:
                    texto = f'Erro SQL:{str(erro)[1:5]} Nada Encontrado'
                    mw.baixalabelDialog.setText(texto)
                    print(str(erro) + texto)

    def tabCodBaixa():
        teste = mw.baixaComboBoxTipo.currentText().lower()

        if teste == 'celular':
            ret = ('celular', 'idCelular')
            return ret

        if teste == 'computer':
            ret = ('computer', 'idComputer')
            return ret

        if teste == 'disco':
            ret = ('disco', 'idDisco')
            return ret

        if teste == 'memoria':
            ret = ('memoria', 'idMemoria')
            return ret

        if teste == 'monitor':
            ret = ('monitor', 'idMonitor')
            return ret

        if teste == 'mouse':
            ret = ('mouse', 'idMouse')
            return ret

        if teste == 'mousepad':
            ret = ('mousepad', 'idMousePad')
            return ret

        if teste == 'office':
            ret = ('office', 'idOffice')
            return ret

        if teste == 'outros':
            ret = ('outros', 'idOutros')
            return ret

        if teste == 'suporte':
            ret = ('suporte', 'idSuporte')
            return ret

        if teste == 'windows':
            ret = ('windows', 'idWindows')
            return ret

        else:
            teste = None
            return teste

    def motiBaixa():

        if mw.baixaRadioObsoleto.isChecked() == True:
            ret = mw.baixaRadioObsoleto.text()
            return ret

        elif mw.baixaRadioDefeito.isChecked() == True:
            ret = mw.baixaRadioDefeito.text()
            return ret

        elif mw.baixaRadioSucata.isChecked() == True:
            ret = mw.baixaRadioSucata.text()
            return ret

        elif mw.baixaRadioVenda.isChecked() == True:
            ret = mw.baixaRadioVenda.text()
            return ret

        elif mw.baixaRadioOutro.isChecked() == True:
            ret = mw.baixaRadioOutro.text()
            return ret

        else:
            return None

    def addItemBaixa():
        get = getIDTableBaixa()
        pic = getIDCodBaixa()[0:2]
        print(get, pic)

        # Teclado 21000
        if pic == '21':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 960.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')
            mw.baixaFrameDestino.setStyleSheet('background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Suporte 20000
        elif pic == '20':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 961.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')
            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Memoria 19000
        elif pic == '19':

            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 957.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')
            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Disco 18000
        elif pic == '18':

            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 958.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Celular 17000
        elif pic == '17':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 950.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Monitor 16000
        elif pic == '16':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 952.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Mouse 15000
        elif pic == '15':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 956.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # MousePad 14000
        elif pic == '14':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 959.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet('background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Windows 13000
        elif pic == '13':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 955.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet('background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Office 12000
        elif pic == '12':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 954.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Desktop Notebook 11000
        elif pic == '11':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 951.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        # Outros 10000
        elif pic == '10':
            mw.baixaFrameItemPicture.setStyleSheet(
                'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
                ';background-position:center;background-repeat: no-repeat;')
            cod = mw.baixaTableWidget.item(get, 0).text()
            tipo = mw.baixaTableWidget.item(get, 1).text().upper()[0:15]
            marca = mw.baixaTableWidget.item(get, 2).text()
            modelo = mw.baixaTableWidget.item(get, 3).text()
            local = mw.baixaTableWidget.item(get, 4).text()
            preco = mw.baixaTableWidget.item(get, 5).text()

            mw.baixalabelCod.setText(cod)
            mw.baixalabelMarca.setText(marca)
            mw.baixalabelModelo.setText(modelo)
            mw.baixalabelLocal.setText(local)
            mw.baixalabelPreco.setText(preco)

            mw.baixaFrameItem.setStyleSheet(
                'background-color: rgb(199, 211, 0);border: 1px; border-radius: 10px;')

            mw.baixaFrameDestino.setStyleSheet(
                'background-color: rgb(255, 118, 118); border: 1px; border-radius: 10px;')

        else:
            texto = 'Família não encontrada'
            print('Nenhuma familia encontrada')
            mw.baixalabelDialog.setText(texto)

    def getIDTableBaixa():
        ret = mw.baixaTableWidget.currentRow()
        return ret

    def getIDCodBaixa():
        ret = mw.baixaTableWidget.item(getIDTableBaixa(), 0)
        return ret.text() if not ret is None else ret

    def limpPageBaixa():
        try:
            con = db.conMySQL()
            con.execute(f"""SELECT idCelular, TIPO, MARCA, MODELO, LOCAL, VALOR, DATA
                                FROM celular
                                WHERE LOCAL LIKE '500000'""")
            result = con.fetchall()
            print(result)

            mw.baixaTableWidget.clearContents()
            header = mw.baixaTableWidget.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            mw.baixaTableWidget.setRowCount(
                len(result))  # <-- Numeros de linhas conforme quantidade da tabela

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    mw.baixaTableWidget.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        except:
            print('Limpeza falhou')

        mw.baixalineEditPes.clear()
        mw.baixaComboBoxTipo.setCurrentIndex(0)
        mw.baixaComboBoxCampo.setCurrentIndex(0)

        mw.baixalabelCod.setText('----')
        mw.baixalabelMarca.setText('----')
        mw.baixalabelModelo.setText('----')
        mw.baixalabelLocal.setText('----')
        mw.baixalabelPreco.setText('----')

        mw.baixaComboBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.baixaComboBoxCampo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.baixalineEditPes.setStyleSheet('background-color: rgb(255, 255, 255);')
        mw.baixalabelDialog.clear()
        mw.baixaFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255); border-radius: 10px;')
        mw.baixaFrameItem.setStyleSheet('background-color:rgb(7, 183, 168);border: 1px;border-radius: 10px;')
        mw.baixaFrameItemPicture.setStyleSheet(
            'background-image: url(:/picture/estoque/entrada e saida/pictures/Grupo 974.png);\n'
            ';background-position:center;background-repeat: no-repeat;')

        mw.baixaFrameDestino.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')

    def movEstoqueBaixa():
        codItem = mw.baixalabelCod.text()
        motivo = motiBaixa()
        tipo = mw.baixaTableWidget.item(getIDTableBaixa(), 1)

        print(codItem, motivo)

        if codItem == '----' or motivo == None:
            mw.baixaFrameMotivo.setStyleSheet(
                'border: 2px solid; border-color: rgb(255, 118, 118); border-radius: 10px;')
            mw.baixaFrameItem.setStyleSheet('background-color:rgb(255, 118, 118);border: 1px;border-radius: 10px;')

            texto = 'Campos obrigatórios não preenchidos'
            mw.baixalabelDialog.setText(texto)

        else:
            # --------------- Item --------------------
            tipo = mw.baixaComboBoxTipo.currentText()
            marca = mw.baixalabelMarca.text()
            modelo = mw.baixalabelModelo.text()
            local = 'BAIXA'
            data = datAT()

            DialogiEstoqueBaixa.show()
            texto = f'DESEJA REALMENTE BAIXAR O ITEM\n {marca} ID {codItem} DO ESTOQUE TI'
            dx.LabelDialogMsg.setText(texto)

            def sim():
                if tabCodBaixa() is not None:
                    tabela = tabCodBaixa()[0]
                    coluna = tabCodBaixa()[1]
                    print(tabela, coluna)
                    print(marca, modelo, local, data, motivo, tipo)

                    try:
                        con = db.conMySQL()
                        con.execute(
                            f"""DELETE FROM {tabela} WHERE (`{coluna}` = '{codItem}');""")

                        con.execute(
                            f"""INSERT INTO historico VALUES ('{Usuario}','BAIXA ESTOQUE TI','{tipo}','{codItem}',
                                                        '{marca}','{modelo}','{motivo}','{local}','{data}');""")

                        DialogiEstoqueBaixa.close()
                        Positive.show()
                        po.LabelDialog.setText('TRANSAÇÃO REALIZADA COM SUCESSO!')
                        con.close()
                        limpPageBaixa()

                    except pymysql.Error as erro:
                        texto = f'Erro SQL:{str(erro)[1:5]}'
                        mw.baixalabelDialog.setText(texto)
                        print(str(erro) + texto)
                        print('deu ruim')

                else:
                    DialogiEstoqueBaixa.close()

            def nao():
                DialogiEstoqueBaixa.close()

            dx.pushButtonSim.clicked.connect(sim)
            dx.pushButtonNao.clicked.connect(nao)

    def cancelBaixa():
        limpPageBaixa()
        mw.stackedWidget.setCurrentWidget(mw.PageGestao)

    mw.baixaButtonBuscar.clicked.connect(pesBaixa)
    mw.baixaTableWidget.itemSelectionChanged.connect(addItemBaixa)
    mw.baixabuttonLimpar.clicked.connect(limpPageBaixa)
    mw.baixabuttonCancel.clicked.connect(cancelBaixa)
    mw.baixabuttonConfirmar.clicked.connect(movEstoqueBaixa)


#   GRAFICO HOME #######################################################################################################

    def graphicPizza():
        # Entrada e tratamento de dados -------------------------------------
        con = db.conMySQL()
        con.execute(""" SELECT * FROM disco 
                        WHERE LOCAL = 'ESTOQUE'
                        AND TIPO like '%SSD%';""")

        ssd = len(con.fetchall())

        con.execute(""" SELECT * FROM memoria 
                        WHERE LOCAL = 'ESTOQUE';""")
        memoria = len(con.fetchall())

        con.execute(""" SELECT * FROM mouse 
                        WHERE LOCAL = 'ESTOQUE';""")
        mouse = len(con.fetchall())

        con.execute(""" SELECT * FROM mousepad 
                        WHERE LOCAL = 'ESTOQUE';""")
        mousePad = len(con.fetchall())

        con.execute(""" SELECT * FROM office 
                        WHERE LOCAL = 'ESTOQUE';""")
        office = len(con.fetchall())

        con.execute(""" SELECT * FROM windows 
                        WHERE LOCAL = 'ESTOQUE';""")
        windows = len(con.fetchall())

        con.execute(""" SELECT * FROM suporte 
                        WHERE LOCAL = 'ESTOQUE';""")
        suporte = len(con.fetchall())

        con.execute(""" SELECT * FROM teclado 
                        WHERE LOCAL = 'ESTOQUE';""")
        teclado = len(con.fetchall())

        print(ssd, memoria, suporte, teclado, mousePad, mouse, office, windows)
        con.close()

        valores = [ssd, memoria, suporte, teclado, mouse, mousePad, office, windows]

        figure, ax = plt.subplots(figsize=(8, 3), subplot_kw=dict(aspect="equal"))

        recipe = [f"SSD {valores[0]}", f"MEMORIA {valores[1]}", f"SUPORTE {valores[2]}", f"TECLADO {valores[3]}",
                  f"MOUSE {valores[4]}", f"MOUSE PAD {valores[5]}", f"OFFICE {valores[6]}", f"WINDOWS {valores[6]}"]

        wedges, texts = ax.pie(valores, wedgeprops=dict(width=0.5), startangle=-40)
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        kw = dict(arrowprops=dict(arrowstyle="-"), bbox=bbox_props, zorder=0, va="center")

        for i, p in enumerate(wedges):
            ang = (p.theta2 - p.theta1) / 2. + p.theta1
            y = np.sin(np.deg2rad(ang))
            x = np.cos(np.deg2rad(ang))
            horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
            connectionstyle = "angle,angleA=0,angleB={}".format(ang)
            kw["arrowprops"].update({"connectionstyle": connectionstyle})
            ax.annotate(recipe[i], xy=(x, y), xytext=(1.35 * np.sign(x), 1.4 * y),
                        horizontalalignment=horizontalalignment, **kw)

        ax.set_title("RATEIO DE PERIFÉRICOS")

        canvas = FigureCanvas(figure)
        canvas.draw()

        mw.horizontalLayoutGPC.addWidget(canvas)

    def graphicBar():
        # Entrada e tratamento de dados -------------------------------------
        con = db.conMySQL()
        con.execute(""" SELECT tipo FROM historico 
                            WHERE status = 'SAIDA. ESTOQUE TI'
                            AND tipo like '%DISCO%';""")
        ssd = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                WHERE status = 'SAIDA. ESTOQUE TI'
                                AND tipo like '%MEMORIA%';""")
        memoria = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                    WHERE status = 'SAIDA. ESTOQUE TI'
                                    AND tipo like '%MOUSE%';""")
        mouse = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                    WHERE status = 'SAIDA. ESTOQUE TI'
                                    AND tipo like '%MOUSE PAD%';""")
        mousePad = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                    WHERE status = 'SAIDA. ESTOQUE TI'
                                    AND tipo like '%OFFICE%';""")
        office = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                    WHERE status = 'SAIDA. ESTOQUE TI'
                                    AND tipo like '%WINDOWS%';""")
        windows = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                    WHERE status = 'SAIDA. ESTOQUE TI'
                                    AND tipo like '%SUPORTE%';""")
        suporte = len(con.fetchall())

        con.execute(""" SELECT tipo FROM historico 
                                    WHERE status = 'SAIDA. ESTOQUE TI'
                                    AND tipo like '%TECLADO%';""")
        teclado = len(con.fetchall())

        print(ssd, memoria, suporte, teclado, mousePad, mouse, office, windows)
        con.close()

        nomes = ['SSD', 'MEM', 'SUP', 'TEC', 'MOU', 'PAD', 'OFF', 'WIN']
        valores = [ssd, memoria, suporte, teclado, mouse, mousePad, office, windows]

        print(nomes, valores)

        # Stylo do grafico --------------------------------------------------
        plt.style.use('seaborn')

        # Ajustando o layout na janela --------------------------------------
        plt.rcParams.update({'figure.autolayout': True})

        # Construção do gráfico ---------------------------------------------
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.bar(nomes, valores, color='#00A194')

        # Rotacionando a label ----------------------------------------------
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=45, horizontalalignment='right')

        # Rotulando o gráfico -----------------------------------------------
        ax.set(xlabel='', ylabel='', title='SAIDAS DO ESTOQUE')

        canvas = FigureCanvas(fig)
        canvas.draw()
        mw.horizontalLayoutGPC1.addWidget(canvas)

    def graphicBarUser():
        # Entrada e tratamento de dados -------------------------------------
        con = db.conMySQL()
        con.execute(""" SELECT * FROM historico
                        WHERE user = 'gabrieln4155_00';""")
        gabriel = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                        WHERE user = 'sideh4155_00';""")
        side = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                            WHERE user = 'emanuels4155_00';""")
        emanuel = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                                WHERE user = 'alexandres4155_00';""")
        alexandre = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                                    WHERE user = 'admin';""")
        admin = len(con.fetchall())

        print(gabriel, side, emanuel, alexandre, admin)
        con.close()

        nomes = ['GABRIEL', 'HENRIQUE', 'EMANUEL', 'ADMIN']
        valores = [gabriel, side, emanuel,  admin]

        print(nomes, valores)

        # Stylo do grafico --------------------------------------------------
        plt.style.use('seaborn')

        # Ajustando o layout na janela --------------------------------------
        plt.rcParams.update({'figure.autolayout': True})

        # Construção do gráfico ---------------------------------------------
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.bar(nomes, valores, color='#00353E')

        # Rotacionando a label ----------------------------------------------
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=0, horizontalalignment='right')

        # Rotulando o gráfico -----------------------------------------------
        ax.set(xlabel='', ylabel='', title='ATIVIDADE DE USUÁRIOS')

        canvas = FigureCanvas(fig)
        canvas.draw()
        mw.verticalLayoutGPC.addWidget(canvas)

    def graphicBarUser1():
        # Entrada e tratamento de dados -------------------------------------
        con = db.conMySQL()
        con.execute(""" SELECT * FROM historico
                        WHERE user = 'gabrieln4155_00';""")
        gabriel = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                        WHERE user = 'sideh4155_00';""")
        side = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                            WHERE user = 'emanuels4155_00';""")
        emanuel = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                                WHERE user = 'alexandres4155_00';""")
        alexandre = len(con.fetchall())

        con.execute(""" SELECT * FROM historico
                                    WHERE user = 'admin';""")
        admin = len(con.fetchall())

        print(gabriel, side, emanuel, alexandre, admin)
        con.close()

        nomes = ['GABRIEL', 'HENRIQUE', 'EMANUEL', 'ALEXANDRE', 'ADMIN']
        valores = [gabriel, side, emanuel, alexandre, admin]

        print(nomes, valores)

        # Stylo do grafico --------------------------------------------------
        plt.style.use('seaborn')

        # Ajustando o layout na janela --------------------------------------
        plt.rcParams.update({'figure.autolayout': True})

        # Construção do gráfico ---------------------------------------------
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.bar(nomes, valores, color='#00353E')

        # Rotacionando a label ----------------------------------------------
        labels = ax.get_xticklabels()
        plt.setp(labels, rotation=0, horizontalalignment='right')

        # Rotulando o gráfico -----------------------------------------------
        ax.set(xlabel='', ylabel='', title='FLUXO DE SAIDAS DO ESTOQUE')

        canvas = FigureCanvas(fig)
        canvas.draw()
        mw.verticalLayoutGPC.addWidget(canvas)

    graphicBarUser1()
    graphicBarUser()
    graphicPizza()
    graphicBar()

    # CADASTRO DE ITENS NO BANCO #######################################################################################
    ####################################################################################################################
    ####################################################################################################################
    ####################################################################################################################

    # TRATAMENTO NOTEBOOK # <<< ------------------------------------------
    def cadNote():
        imb = mw.notIMB.text()
        marca = mw.notMarca.text()
        modelo = mw.notModelo.text()
        condicao = mw.notCondicao.currentText()
        ano = mw.notAno.text()
        preco = mw.notPreco.text()
        service = mw.notService.text()
        rede = mw.notRede.text()
        team = mw.notTeam.text()
        ant = mw.notBoxAntevirus.currentText()
        tela = mw.notBoxTela.currentText()
        car = mw.notBoxCarregador.currentText()
        pro = mw.notPro.text()
        marPro = mw.notMarcaPro.text()
        frePro = mw.notFrePro.text()
        gePro = mw.notBoxGeracao.currentText()
        disco = mw.notBoxSSD.currentText()
        exp = mw.notBoxExp.currentText()
        ram = mw.notRam.text()
        verRam = mw.notVerRam.text()
        freRam = mw.notFreRam.text()
        expRam = mw.notBoxExpRam.currentText()

        motivo = motiNote()
        tipo = 'Notebook'
        local = mw.notSetorLocal.text()
        data = datAT()
        user = mw.notCodUser.text()
        win = mw.notCodWin.text()
        off = mw.notCodOff.text()

        def trataWin():
            if mw.notCodWin.text() == '------------':
                return 'null'
            else:
                return mw.notCodWin.text()

        def trataOff():
            if mw.notCodOff.text() == '------------':
                return 'null'
            else:
                return mw.notCodOff.text()

        idWindows = trataWin()
        idOffice = trataOff()

        # print(imb, marca, modelo, condicao, ano, preco, service, rede, team, ant, tela, car, pro, marPro, frePro,
        #       gePro, disco, exp, ram, verRam, freRam, expRam, user, win, off, motivo, tipo, local, data)

        if motivo == '' or marca == '' or modelo == '' or service == '' or rede == '' or \
                car == '' or pro == '' or gePro == '' or ram == '' or verRam == '':
            mw.frameMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.notMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notService.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notRede.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notBoxCarregador.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notPro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notBoxGeracao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.notVerRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
            mw.notLabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, VALOR,
                            SERVICETAG, TEAMVIEWER, REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO,
                            FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, ANTEVIRUS,
                            TIPO, LOCAL, DATA, idWindows, idOffice)

                            VALUES ('{imb}','{marca}','{modelo}','{condicao}','{ano}','{tela}','{preco}',
                            '{service}','{team}','{rede}','{disco}','{exp}','{car}','{pro}','{marPro}',
                            '{frePro}','{gePro}','{ram}','{verRam}','{freRam}','{expRam}','{ant}',
                            '{tipo}','{local}','{data}',{idWindows},{idOffice});""")

                cur.execute(f"""SELECT MAX(idComputer) FROM computer;""")
                banc = cur.fetchall()
                idCon = banc[0][0]

                if user != '------------':
                    cur.execute(f"""SELECT * FROM colaborador WHERE idComputer = {idCon};""")
                    result = cur.fetchall()

                    if result == ():
                        cur.execute(
                            f"""UPDATE colaborador SET idComputer = '{idCon}' WHERE idColaborador = '{user}';""")

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{idCon}','{marca}',
                    '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {idCon} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                cleanNote()
                mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def motiNote():

        if mw.notRadioCompra.isChecked() == True:
            compra = mw.notRadioCompra.text()
            return compra

        elif mw.notRadioCadastro.isChecked() == True:
            cadastro = mw.notRadioCadastro.text()
            return cadastro

        elif mw.notRadioProvisorio.isChecked() == True:
            provisorio = mw.notRadioProvisorio.text()
            return provisorio

        elif mw.notRadioOutro.isChecked() == True:
            outros = mw.notRadioOutro.text()
            return outros

        else:
            return 'Motivo Não Selecionado'

    def winNote():
        opNote.close()
        opNote.show()
        op.stackedWidget.setCurrentWidget(op.pageOpWin)

        def checkWin():

            windows = op.notLineWin.text()

            if len(windows) < 25:
                texto = 'Chave Windows Invalida'
                op.notlabelWin.setText(texto)

            else:
                try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
                    cur = db.conMySQL()
                    cur.execute(f"""SELECT * FROM windows WHERE CHAVE = '{windows}';""")  # ------ Que Contenha
                    idw = cur.fetchall()
                    print(windows + '<--- Isto é oque o usuario digitou')

                    if idw == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
                        texto = 'Chave Windows Não Cadastrada'
                        op.notlabelWin.setText(texto)

                    if idw != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
                        chave = idw[0][1]  # <-------------------- pega o campo da chave
                        id = idw[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID WINDOWS) int
                        versao = idw[0][2]  # <-------------------- pega o campo da versão do windows

                        try:  # <---------- vai pesquisar na tabela computer se essa (ID WINDOWS) esta vinculada com alguma maquina
                            cur.execute(f"""SELECT * FROM computer WHERE idWindows = {id};""")
                            idN = cur.fetchall()
                            cur.close()

                            if idN == ():  # <--------- se retornar tupla vazia não achou (ID WINDOWS) vinculado a alguma maquina
                                texto = 'Esta chave Windows \nEstá disponivel!'
                                mw.notFrameWindows.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                mw.notVerWin.setText(versao)
                                mw.notCodWin.setText(str(id))

                                Positive.show()
                                op.notLineWin.clear()
                                po.LabelDialog.setText(texto)
                                opNote.close()

                            else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                                texto = 'Esta chave Windows \nNão está disponivel!'
                                op.notlabelWin.setText(texto)

                        except pymysql.Error as erro:
                            texto = str(erro)
                            dg.LabelDialog.setText(texto)
                            Dialog.show()

                except:
                    texto = 'ALGO DEU ERRADO!'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        op.notButtonWin.clicked.connect(checkWin)

    def offNote():
        opNote.close()
        opNote.show()
        op.stackedWidget.setCurrentWidget(op.pageOpOff)

        def checkOff():

            office = op.notLineOff.text()

            if len(office) < 25:
                texto = 'Chave Office Invalida'
                op.notlabelOff.setText(texto)

            else:
                try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
                    cur = db.conMySQL()
                    cur.execute(f"""SELECT * FROM office WHERE CHAVE = '{office}';""")  # ------ Que Contenha
                    ido = cur.fetchall()
                    print(office + '<--- Isto é oque o usuario digitou')

                    if ido == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
                        texto = 'Chave Office Não Cadastrada'
                        op.notlabelOff.setText(texto)

                    if ido != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
                        chave = ido[0][1]  # <-------------------- pega o campo da chave
                        id = ido[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID OFFICE) int
                        versao = ido[0][2]  # <-------------------- pega o campo da versão do windows

                        try:  # <---------- vai pesquisar na tabela computer se essa (ID OFFICE) esta vinculada com alguma maquina
                            cur.execute(f"""SELECT * FROM computer WHERE idOffice = {id};""")
                            idN = cur.fetchall()
                            cur.close()

                            if idN == ():  # <--------- se retornar tupla vazia não achou (ID OFFICE) vinculado a alguma maquina
                                texto = 'Esta chave Office \nEstá disponivel!'
                                mw.notFrameOffice.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                mw.notVerOff.setText(versao)
                                mw.notCodOff.setText(str(id))

                                Positive.show()
                                op.notLineOff.clear()
                                po.LabelDialog.setText(texto)
                                opNote.close()

                            else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                                texto = 'Esta chave Office \nNão está disponivel!'
                                op.notlabelOff.setText(texto)

                        except pymysql.Error as erro:
                            texto = str(erro)
                            dg.LabelDialog.setText(texto)
                            Dialog.show()

                except:
                    texto = 'ALGO DEU ERRADO!'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        op.notButtonOff.clicked.connect(checkOff)

    def cleanNote():
        mw.notIMB.clear()
        mw.notMarca.clear()
        mw.notModelo.clear()
        mw.notCondicao.clear()
        mw.notAno.clear()
        mw.notPreco.clear()
        mw.notService.clear()
        mw.notRede.clear()
        mw.notTeam.clear()
        mw.notBoxAntevirus.setCurrentIndex(0)
        mw.notBoxTela.setCurrentIndex(0)
        mw.notBoxCarregador.setCurrentIndex(0)
        mw.notPro.clear()
        mw.notMarcaPro.clear()
        mw.notFrePro.clear()
        mw.notBoxGeracao.setCurrentIndex(0)
        mw.notBoxSSD.setCurrentIndex(0)
        mw.notBoxExp.setCurrentIndex(0)
        mw.notRam.clear()
        mw.notVerRam.clear()
        mw.notFreRam.clear()
        mw.notBoxExpRam.setCurrentIndex(0)
        mw.frameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.notMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notService.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notRede.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notBoxCarregador.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notPro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notBoxGeracao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.notVerRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

        mw.notFrameWindows.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.notCodWin.setText('------------')
        mw.notVerWin.setText('------------')

        mw.notFrameOffice.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.notCodOff.setText('------------')
        mw.notVerOff.setText('------------')

        mw.notFrameLocal.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.notCodLocal.setText('------------')
        mw.notSetorLocal.setText('------------')

        mw.notFrameUser.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.notCodUser.setText('------------')
        mw.notCarUser.setText('------------')
        mw.notLabelUser.setText('USER')

        mw.notLabelDialog.clear()

    def userNote():
        opNote.close()
        opNote.show()
        op.stackedWidget.setCurrentWidget(op.pageOpUser)

        def pUser():
            user = op.notLineUser.text()
            print(user + '<--- entrada do usuario')

            if user == '':
                texto = 'Campo de pesquisa em branco \nPor favor preencha o campo de pesquisa de usuario'
                op.notLineUser.setStyleSheet('background-color: rgb(255, 192, 193);')
                op.notlabelUser.setText(texto)

            else:
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT * FROM colaborador WHERE nome like '%{user}%';""")
                    dados = con.fetchall()

                    if dados == ():
                        texto = 'Usuário não encontrado\n certifique se de que o mesmo esta cadastrado'
                        op.notlabelUser.setText(texto)

                    else:
                        nome = dados[0][1]
                        cargo = dados[0][4]
                        idu = dados[0][0]

                        con.execute(f"""SELECT idComputer FROM colaborador WHERE idColaborador = {idu};""")
                        result = con.fetchall()
                        print(result)

                        if result == ((None,),):
                            texto = 'Colaborador Encontrado'
                            mw.notFrameUser.setStyleSheet(
                                'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mw.notLabelUser.setText(nome)
                            mw.notCarUser.setText(cargo)
                            mw.notCodUser.setText(str(idu))

                            Positive.show()
                            op.notLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opNote.close()

                        else:
                            texto = 'Colaborador Já Possue Notebook\nDeseja Subistituir?'
                            DialogiConditional.show()
                            di.LabelDialogMsg.setText(texto)

                            def sim():
                                mw.notFrameUser.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')
                                mw.notLabelUser.setText(nome)
                                mw.notCarUser.setText(cargo)
                                mw.notCodUser.setText(str(idu))
                                DialogiConditional.close()
                                op.notLineUser.clear()
                                opNote.close()

                            def nao():
                                DialogiConditional.close()
                                op.notLineUser.clear()
                                opNote.close()

                            di.pushButtonSim.clicked.connect(sim)
                            di.pushButtonNao.clicked.connect(nao)



                except:
                    texto = 'Colaborador Não Encontrado'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        op.notButtonUser.clicked.connect(pUser)

    def placeNote():
        opNote.close()
        opNote.show()
        op.stackedWidget.setCurrentWidget(op.pageOpLocal)

        def local():
            local = op.notBoxLocal.currentText()

            texto = 'Local Selecionado'
            mw.notFrameLocal.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mw.notSetorLocal.setText(local)
            mw.notCodLocal.setText('01')

            Positive.show()
            op.notLineUser.clear()
            po.LabelDialog.setText(texto)
            opNote.close()

        op.notButtonLocal.clicked.connect(local)

    def cancelNote():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
        cleanNote()

    mw.notButtonCancelar.clicked.connect(cancelNote)
    mw.notButtonLocal.clicked.connect(placeNote)
    mw.notButtonUser.clicked.connect(userNote)
    mw.notButtonWin.clicked.connect(winNote)
    mw.notButtonOff.clicked.connect(offNote)
    mw.notButtonLimpar.clicked.connect(cleanNote)
    mw.notButtonConfirmar.clicked.connect(cadNote)

    # TRATAMENTO DESKTOP # <<< ------------------------------------------
    def cadDesk():
        imb = mw.topIMB.text()
        marca = mw.topMarca.text()
        modelo = mw.topModelo.text()
        condicao = mw.topCondicao.currentText()
        ano = mw.topAno.text()
        preco = mw.topPreco.text()
        service = mw.topService.text()
        rede = mw.topRede.text()
        team = mw.topTeam.text()
        ant = mw.topBoxAntevirus.currentText()
        monitor = mw.topBoxMonitor.currentText()
        pro = mw.topPro.text()
        marPro = mw.topMarcaPro.text()
        frePro = mw.topFrePro.text()
        gePro = mw.topBoxGeracao.currentText()
        disco = mw.topBoxSSD.currentText()
        exp = mw.topBoxExp.currentText()
        ram = mw.topRam.text()
        verRam = mw.topVerRam.text()
        freRam = mw.topFreRam.text()
        expRam = mw.topBoxExpRam.currentText()

        motivo = motiDesk()
        tipo = 'Desktop'
        local = mw.topSetorLocal.text()
        data = datAT()
        user = mw.topCodUser.text()
        win = mw.topCodWin.text()
        off = mw.topCodOff.text()

        def trataWinTop():
            if mw.topCodWin.text() == '------------':
                return 'null'
            else:
                return mw.notCodWin.text()

        def trataOffTop():
            if mw.topCodOff.text() == '------------':
                return 'null'
            else:
                return mw.notCodOff.text()

        idWindows = trataWinTop()
        idOffice = trataOffTop()

        print(imb, marca, modelo, condicao, ano, preco, service, rede, team, ant, monitor, pro, marPro, frePro,
              gePro, disco, exp, ram, verRam, freRam, expRam, user, win, off, motivo, tipo, local, data)

        if motivo == '' or marca == '' or modelo == '' or service == '' or rede == '' or \
                pro == '' or gePro == '' or ram == '' or verRam == '':

            mw.frameMotivo_2.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.topMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topService.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topRede.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topPro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topBoxGeracao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.topVerRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
            mw.topLabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, VALOR,
                            SERVICETAG, TEAMVIEWER, REDE, SSD, EXPANCIVEL, PROCESSADOR, MARCAPRO,
                            FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, ANTEVIRUS,
                            TIPO, LOCAL, DATA, idWindows, idOffice)

                            VALUES ('{imb}','{marca}','{modelo}','{condicao}','{ano}','{monitor}','{preco}',
                            '{service}','{team}','{rede}','{disco}','{exp}','{pro}','{marPro}',
                            '{frePro}','{gePro}','{ram}','{verRam}','{freRam}','{expRam}','{ant}',
                            '{tipo}','{local}','{data}',{idWindows},{idOffice});""")

                cur.execute(f"""SELECT MAX(idComputer) FROM computer;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                if user != '------------':
                    cur.execute(f"""UPDATE colaborador SET idComputer = '{result}' WHERE idColaborador = '{user}';""")

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                    '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                cleanDesk()
                mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def motiDesk():

        if mw.topRadioCompra.isChecked() == True:
            compra = mw.topRadioCompra.text()
            return compra

        elif mw.topRadioCadastro.isChecked() == True:
            cadastro = mw.topRadioCadastro.text()
            return cadastro

        elif mw.topRadioProvisorio.isChecked() == True:
            provisorio = mw.topRadioProvisorio.text()
            return provisorio

        elif mw.topRadioOutro.isChecked() == True:
            outros = mw.topRadioOutro.text()
            return outros

        else:
            return 'Motivo Não Selecionado'

    def winDesk():
        opDesk.close()
        opDesk.show()
        opd.stackedWidget.setCurrentWidget(opd.pageOpWin)

        def checkWin():

            windows = opd.topLineWin.text()

            if len(windows) < 25:
                texto = 'Chave Windows Invalida'
                opd.toplabelWin.setText(texto)

            else:
                try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
                    cur = db.conMySQL()
                    cur.execute(f"""SELECT * FROM windows WHERE CHAVE = '{windows}';""")  # ------ Que Contenha
                    idw = cur.fetchall()
                    print(windows + '<--- Isto é oque o usuario digitou')

                    if idw == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
                        texto = 'Chave Windows Não Cadastrada'
                        opd.toplabelWin.setText(texto)

                    if idw != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
                        chave = idw[0][1]  # <-------------------- pega o campo da chave
                        id = idw[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID WINDOWS) int
                        versao = idw[0][2]  # <-------------------- pega o campo da versão do windows

                        try:  # <---------- vai pesquisar na tabela computer se essa (ID WINDOWS) esta vinculada com alguma maquina
                            cur.execute(f"""SELECT * FROM computer WHERE idWindows = {id};""")
                            idN = cur.fetchall()
                            cur.close()

                            if idN == ():  # <--------- se retornar tupla vazia não achou (ID WINDOWS) vinculado a alguma maquina
                                texto = 'Esta chave Windows \nEstá disponivel!'
                                mw.topFrameWindows.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                mw.topVerWin.setText(versao)
                                mw.topCodWin.setText(str(id))

                                Positive.show()
                                opd.topLineWin.clear()
                                po.LabelDialog.setText(texto)
                                opDesk.close()

                            else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                                texto = 'Esta chave Windows não está \nDisponivel!'
                                opd.toplabelWin.setText(texto)

                        except pymysql.Error as erro:
                            texto = str(erro)
                            dg.LabelDialog.setText(texto)
                            Dialog.show()

                except:
                    texto = 'ALGO DEU ERRADO!'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        opd.topButtonWin.clicked.connect(checkWin)

    def offDesk():
        opDesk.close()
        opDesk.show()
        opd.stackedWidget.setCurrentWidget(opd.pageOpOff)

        def checkOff():

            office = opd.topLineOff.text()

            if len(office) < 25:
                texto = 'Chave Office Invalida'
                opd.toplabelOff.setText(texto)

            else:
                try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
                    cur = db.conMySQL()
                    cur.execute(f"""SELECT * FROM office WHERE CHAVE = '{office}';""")  # ------ Que Contenha
                    ido = cur.fetchall()
                    print(office + '<--- Isto é oque o usuario digitou')

                    if ido == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
                        texto = 'Chave Office Não Cadastrada'
                        opd.toplabelOff.setText(texto)

                    if ido != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
                        chave = ido[0][1]  # <-------------------- pega o campo da chave
                        id = ido[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID OFFICE) int
                        versao = ido[0][2]  # <-------------------- pega o campo da versão do windows

                        try:  # <---------- vai pesquisar na tabela computer se essa (ID OFFICE) esta vinculada com alguma maquina
                            cur.execute(f"""SELECT * FROM computer WHERE idOffice = {id};""")
                            idN = cur.fetchall()
                            cur.close()

                            if idN == ():  # <--------- se retornar tupla vazia não achou (ID OFFICE) vinculado a alguma maquina
                                texto = 'Esta chave Office \nEstá disponivel!'
                                mw.topFrameOffice.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                mw.topVerOff.setText(versao)
                                mw.topCodOff.setText(str(id))

                                Positive.show()
                                opd.topLineOff.clear()
                                po.LabelDialog.setText(texto)
                                opDesk.close()

                            else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                                texto = 'Esta chave Office não está \nDisponivel!'
                                opd.toplabelOff.setText(texto)

                        except pymysql.Error as erro:
                            texto = str(erro)
                            dg.LabelDialog.setText(texto)
                            Dialog.show()

                except:
                    texto = 'ALGO DEU ERRADO!'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        opd.topButtonOff.clicked.connect(checkOff)

    def cleanDesk():
        mw.topIMB.clear()
        mw.topMarca.clear()
        mw.topModelo.clear()
        mw.topCondicao.clear()
        mw.topAno.clear()
        mw.topPreco.clear()
        mw.topService.clear()
        mw.topRede.clear()
        mw.topTeam.clear()
        mw.topBoxAntevirus.setCurrentIndex(0)
        mw.topBoxMonitor.setCurrentIndex(0)
        mw.topPro.clear()
        mw.topMarcaPro.clear()
        mw.topFrePro.clear()
        mw.topBoxGeracao.setCurrentIndex(0)
        mw.topBoxSSD.setCurrentIndex(0)
        mw.topBoxExp.setCurrentIndex(0)
        mw.topRam.clear()
        mw.topVerRam.clear()
        mw.topFreRam.clear()
        mw.topBoxExpRam.setCurrentIndex(0)
        mw.frameMotivo_2.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.topMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topService.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topRede.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topPro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topBoxGeracao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.topVerRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

        mw.topFrameWindows.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.topCodWin.setText('------------')
        mw.topVerWin.setText('------------')

        mw.topFrameOffice.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.topCodOff.setText('------------')
        mw.topVerOff.setText('------------')

        mw.topFrameLocal.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.topCodLocal.setText('------------')
        mw.topSetorLocal.setText('------------')

        mw.topFrameUser.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.topCodUser.setText('------------')
        mw.topCarUser.setText('------------')
        mw.topLabelUser.setText('USER')

        mw.topLabelDialog.clear()

    def userDesk():
        opDesk.close()
        opDesk.show()
        opd.stackedWidget.setCurrentWidget(opd.pageOpUser)

        def pUser():
            user = opd.topLineUser.text()
            print(user + '<--- entrada do usuario')

            if user == '':
                texto = 'Campo de pesquisa em branco \nPor favor preencha o campo de pesquisa de usuario'
                opd.topLineUser.setStyleSheet('background-color: rgb(255, 192, 193);')
                opd.toplabelUser.setText(texto)

            else:
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT * FROM colaborador WHERE nome like '%{user}%';""")
                    dados = con.fetchall()

                    if dados == ():
                        texto = 'Usuário não encontrado\n certifique se de que o mesmo esta cadastrado'
                        opd.toplabelUser.setText(texto)

                    else:
                        nome = dados[0][1]
                        cargo = dados[0][4]
                        idu = dados[0][0]

                        con.execute(f"""SELECT idComputer FROM colaborador WHERE idColaborador = {idu};""")
                        result = con.fetchall()
                        print(result)

                        if result == ((None,),):
                            texto = 'Colaborador Encontrado'
                            mw.topFrameUser.setStyleSheet(
                                'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mw.topLabelUser.setText(nome)
                            mw.topCarUser.setText(cargo)
                            mw.topCodUser.setText(str(idu))

                            Positive.show()
                            opd.topLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opDesk.close()

                        else:
                            texto = 'Colaborador Já Possue Notebook\nDeseja Subistituir?'
                            DialogiConditional.show()
                            di.LabelDialogMsg.setText(texto)

                            def simDesk():
                                mw.topFrameUser.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')
                                mw.topLabelUser.setText(nome)
                                mw.topCarUser.setText(cargo)
                                mw.topCodUser.setText(str(idu))
                                DialogiConditional.close()
                                opd.topLineUser.clear()
                                opDesk.close()

                            def naoDesk():
                                DialogiConditional.close()
                                opd.topLineUser.clear()
                                opDesk.close()

                            di.pushButtonSim.clicked.connect(simDesk)
                            di.pushButtonNao.clicked.connect(naoDesk)



                except:
                    texto = 'Colaborador Não Encontrado'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        opd.topButtonUser.clicked.connect(pUser)

    def placeDesk():
        opDesk.close()
        opDesk.show()
        opd.stackedWidget.setCurrentWidget(opd.pageOpLocal)

        def local():
            local = opd.topBoxLocal.currentText()

            texto = 'Local Selecionado'
            mw.topFrameLocal.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mw.topSetorLocal.setText(local)
            mw.topCodLocal.setText('01')

            Positive.show()
            opd.topLineUser.clear()
            po.LabelDialog.setText(texto)
            opDesk.close()

        opd.topButtonLocal.clicked.connect(local)

    def cancelDesk():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
        cleanNote()

    mw.topButtonCancelar.clicked.connect(cancelDesk)
    mw.topButtonLocal.clicked.connect(placeDesk)
    mw.topButtonUser.clicked.connect(userDesk)
    mw.topButtonWin.clicked.connect(winDesk)
    mw.topButtonOff.clicked.connect(offDesk)
    mw.topButtonLimpar.clicked.connect(cleanDesk)
    mw.topButtonConfirmar.clicked.connect(cadDesk)

    # TRATAMENTO CELULAR # <<< ------------------------------------------
    def cadCell():
        marca = mw.celMarca.text()
        modelo = mw.celModelo.text()
        condicao = mw.celEstado.text()
        ano = mw.celAnoFab.text()
        cor = mw.celCor.text()
        preco = mw.celPreco.text()
        pro = mw.celPro.text()
        modPro = mw.celModPro.text()
        frePro = mw.celFrePro.text()
        ram = mw.celRam.text()
        bateria = mw.celbat.text()
        sistema = mw.celBoxSistema.currentText()
        micro = mw.celBoxMicro.currentText()
        memo = mw.celMemo.text()
        dual = mw.celBoxDual.currentText()
        chipOne = mw.celBoxChipOne.currentText()
        numOne = mw.celNumeroOne.text()
        chipTwe = mw.celBoxChipTwo.currentText()
        numTwe = mw.celNumeroTwo.text()

        motivo = motiCell()
        email = mw.celEndEmail.text()
        tipo = 'Celular'
        local = mw.celSetorLocal.text()

        data = datAT()

        user = mw.celCodUser.text()
        imeiOne = mw.celImeiOne.text()
        imeiTwo = mw.celImeiTwe.text()

        # print(marca, modelo, condicao, ano, preco, ano, cor, pro, modPro, frePro, ram, bateria, sistema, micro, memo,
        #         dual, chipOne, numOne, chipTwe, numTwe,  user, imeiOne, imeiTwo, motivo, tipo, local, data)

        if marca == '' or modelo == '' or cor == '' or pro == '' or frePro == '' or ram == '' or memo == '':

            mw.frameMotivo_3.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.celMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.celModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.celCor.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.celPro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.celFrePro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.celRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.celMemo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
            mw.celLabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO celular (IMEI, IMEI2, MARCA, MODELO, CONDICAO, ANOFAB, COR, VALOR,
                                PROCESSADOR, MODPRO, FREPRO, RAM, BATERIA, SISTEMA, MICRO, MEMOINT, DUO,
                                CHIP, CHIP2, NUMERO, NUMERO2, EMAIL, TIPO, LOCAL, DATA)

                                VALUES ('{imeiOne}','{imeiTwo}','{marca}','{modelo}','{condicao}','{ano}','{cor}','{preco}',
                                '{pro}','{modPro}','{frePro}','{ram}','{bateria}','{sistema}','{micro}','{memo}','{dual}',
                                '{chipOne}','{chipTwe}','{numOne}','{numTwe}','{email}','{tipo}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idCelular) FROM celular;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                if user != '------------':
                    cur.execute(f"""UPDATE colaborador SET idCelular = '{result}' WHERE idColaborador = '{user}';""")

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                        '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                cleanCell()
                mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def motiCell():

        if mw.celRadioCompra.isChecked() == True:
            compra = mw.celRadioCompra.text()
            return compra

        elif mw.celRadioCadastro.isChecked() == True:
            cadastro = mw.celRadioCadastro.text()
            return cadastro

        elif mw.celRadioProvisorio.isChecked() == True:
            provisorio = mw.celRadioProvisorio.text()
            return provisorio

        elif mw.celRadioOutro.isChecked() == True:
            outros = mw.celRadioOutro.text()
            return outros

        else:
            return 'Motivo Não Selecionado'

    def cleanCell():
        mw.celMarca.clear()
        mw.celModelo.clear()
        mw.celEstado.clear()
        mw.celAnoFab.clear()
        mw.celCor.clear()
        mw.celPreco.clear()
        mw.celPro.clear()
        mw.celModPro.clear()
        mw.celFrePro.clear()
        mw.celRam.clear()
        mw.celbat.clear()
        mw.celBoxSistema.setCurrentIndex(0)
        mw.celBoxMicro.setCurrentIndex(0)
        mw.celMemo.clear()
        mw.celBoxDual.setCurrentIndex(0)
        mw.celNumeroOne.clear()
        mw.celNumeroTwo.clear()
        mw.celBoxChipOne.setCurrentIndex(0)
        mw.celBoxChipTwo.setCurrentIndex(0)

        mw.frameMotivo_3.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')

        mw.celMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.celModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.celCor.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.celPro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.celFrePro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.celRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.celMemo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

        mw.celFrameImei.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.celImeiOne.setText('------------')
        mw.celImeiTwe.setText('------------')

        mw.celFrameEmail.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.celEndEmail.setText('------------')
        mw.celCodEmail.setText('------------')

        mw.celFrameLocal.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.celCodLocal.setText('------------')
        mw.celSetorLocal.setText('------------')

        mw.celFrameUser.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mw.celCodUser.setText('------------')
        mw.celCarUser.setText('------------')
        mw.celLabelUser.setText('USER')

        mw.celLabelDialog.clear()

    def userCell():
        opCell.close()
        opCell.show()
        opc.stackedWidget.setCurrentWidget(opc.pageOpUser)

        def pUser():
            user = opc.opLineUser.text()
            print(user + '<--- entrada do usuario')

            if user == '':
                texto = 'Campo de pesquisa em branco \nPor favor preencha o campo de pesquisa de usuario'
                opc.opLineUser.setStyleSheet('background-color: rgb(255, 192, 193);')
                opc.opLabelUser.setText(texto)

            else:
                try:
                    con = db.conMySQL()
                    con.execute(f"""SELECT * FROM colaborador WHERE nome like '%{user}%';""")
                    dados = con.fetchall()

                    if dados == ():
                        texto = 'Usuário não encontrado\n certifique se de que o mesmo esta cadastrado'
                        opc.opLabelUser.setText(texto)

                    else:
                        nome = dados[0][1]
                        cargo = dados[0][4]
                        idu = dados[0][0]

                        con.execute(f"""SELECT idCelular FROM colaborador WHERE idColaborador = {idu};""")
                        result = con.fetchall()
                        print(result)

                        if result == ((None,),):
                            texto = 'Colaborador Encontrado'
                            mw.celFrameUser.setStyleSheet(
                                'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mw.celLabelUser.setText(nome)
                            mw.celCarUser.setText(cargo)
                            mw.celCodUser.setText(str(idu))

                            Positive.show()
                            opc.opLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opCell.close()

                        else:
                            texto = 'Colaborador Já Possue Notebook\nDeseja Subistituir?'
                            DialogiConditional.show()
                            di.LabelDialogMsg.setText(texto)

                            def simCell():
                                mw.celFrameUser.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')
                                mw.celLabelUser.setText(nome)
                                mw.celCarUser.setText(cargo)
                                mw.celCodUser.setText(str(idu))
                                DialogiConditional.close()
                                opc.opLineUser.clear()
                                opCell.close()

                            def naoCell():
                                DialogiConditional.close()
                                opc.opLineUser.clear()
                                opCell.close()

                            di.pushButtonSim.clicked.connect(simCell)
                            di.pushButtonNao.clicked.connect(naoCell)

                except:
                    texto = 'Algo deu Errado'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        opc.opButtonUser.clicked.connect(pUser)

    def placeCell():
        opCell.close()
        opCell.show()
        opc.stackedWidget.setCurrentWidget(opc.pageOpLocal)

        def local():
            local = opc.opBoxLocal.currentText()

            texto = 'Local Selecionado'
            mw.celFrameLocal.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mw.celSetorLocal.setText(local)
            mw.celCodLocal.setText('01')

            Positive.show()
            opc.opLineUser.clear()
            po.LabelDialog.setText(texto)
            opCell.close()

        opc.opButtonLocal.clicked.connect(local)

    def imei():
        opCell.close()
        opCell.show()
        opc.stackedWidget.setCurrentWidget(opc.pageOpImei)

        def pesImei():
            imeiOne = opc.opLineImei_2.text()
            imeiTwe = opc.opLineImei.text()
            print(imeiOne, imeiTwe)

            con = db.conMySQL()
            con.execute(f"""SELECT * FROM celular WHERE IMEI = '{imeiOne}';""")
            result = con.fetchall()

            if result == ():
                texto = 'Codigo Imei Valido'
                mw.celFrameImei.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                mw.celImeiOne.setText(imeiOne)
                mw.celImeiTwe.setText(imeiTwe)

                Positive.show()
                po.LabelDialog.setText(texto)
                opCell.close()

            else:
                texto = 'Código IMEI já cadastrado'
                opc.opLabelImei.setText(texto)

        opc.opButtonImei.clicked.connect(pesImei)

    def email():
        opCell.close()
        opCell.show()
        opc.stackedWidget.setCurrentWidget(opc.pageOpEmail)

        def regEmail():
            email = opc.opLineEmail.text()

            texto = 'Email vinculado com Sucesso'
            mw.celFrameEmail.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mw.celEndEmail.setText(email)
            mw.celCodEmail.setText('01')

            Positive.show()
            po.LabelDialog.setText(texto)
            opCell.close()

        opc.opButtonEmail.clicked.connect(regEmail)

    def cancelCell():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
        cleanCell()

    mw.celButtonCancelar.clicked.connect(cancelCell)
    mw.celButtonLocal.clicked.connect(placeCell)
    mw.celButtonUser.clicked.connect(userCell)
    mw.celButtonImei.clicked.connect(imei)
    mw.celButtonEmail.clicked.connect(email)
    mw.celButtonLimpar.clicked.connect(cleanCell)
    mw.celButtonConfirmar.clicked.connect(cadCell)

    # TRATAMENTO MONITOR # <<< ------------------------------------------

    def cadMonitor():
        modelo = mw.moModelo.text()
        marca = mw.moMarca.text()
        condicao = mw.moCondicao.text()
        valor = mw.moValor.text()
        tamanho = mw.moBoxTamanho.currentText()

        motivo = motivoMonitor()
        tipo = 'Monitor'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tamanho == '' or motivo == None:

            mw.moFrameMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.moModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.moMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.moBoxTamanho.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO monitor (marca, modelo, condicao, tamanho, valor, local, data)
                            VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idMonitor) FROM monitor;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                        '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMonitor()
                mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearMonitor():
        mw.moMarca.clear()
        mw.moModelo.clear()
        mw.moCondicao.clear()
        mw.moValor.clear()
        mw.moBoxTamanho.setCurrentIndex(0)

        mw.moFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.moModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.moMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.moBoxTamanho.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoMonitor():
        if mw.moRadioCompra.isChecked() == True:
            compra = mw.moRadioCompra.text()
            return compra

        elif mw.moRadioCadastro.isChecked() == True:
            cadastro = mw.moRadioCadastro.text()
            return cadastro

        elif mw.moRadioProvisorio.isChecked() == True:
            provisorio = mw.moRadioProvisorio.text()
            return provisorio

        elif mw.moRadioOutros.isChecked() == True:
            outros = mw.moRadioOutros.text()
            return outros

    def cancelMonitor():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
        clearMonitor()

    mw.moButtonConfirmar.clicked.connect(cadMonitor)
    mw.moButtonCancelar.clicked.connect(cancelMonitor)
    mw.moButtonLimpar.clicked.connect(clearMonitor)

    # TRATAMENTO WINDOWS # <<< ------------------------------------------

    def cadWindows():
        chave = mw.winCod.text().upper()
        verPro = mw.winVersao.text()
        valor = mw.winValor.text()
        versao = mw.winBoxVersao.currentText()

        motivo = motivoWin()
        tipo = 'windows'
        local = 'ESTOQUE'
        data = datAT()

        if chave == '' or verPro == '' or versao == '' or motivo == None:

            mw.winMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.winVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.winBoxVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.winCod.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO windows (CHAVE, VERSAOPRO, VERSAO, VALOR, local, data)
                                VALUES ('{chave}','{verPro}','{versao}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idWindows) FROM windows;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{verPro}',
                            '{versao}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearWin()
                mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)

            except pymysql.Error as erro:
                trat = str(erro)
                print(trat)
                codigo = trat[1:5]

                if trat.count('1062'):
                    texto = f'CHAVE INFORMADA JÁ CADASTRADA\n CODIGO MYSQL{codigo}'
                    Dialog.show()
                    dg.LabelDialog.setText(texto)

    def clearWin():
        mw.winCod.clear()
        mw.winVersao.clear()
        mw.winValor.clear()
        mw.winBoxVersao.setCurrentIndex(0)

        mw.winMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.winVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.winBoxVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.winCod.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoWin():
        if mw.winRadioCompra.isChecked() == True:
            compra = mw.winRadioCompra.text()
            return compra

        elif mw.winRadioCadastro.isChecked() == True:
            cadastro = mw.winRadioCadastro.text()
            return cadastro

        elif mw.winRadioProvisorio.isChecked() == True:
            provisorio = mw.winRadioProvisorio.text()
            return provisorio

        elif mw.winRadioOutro.isChecked() == True:
            outros = mw.winRadioOutro.text()
            return outros

    def cancelWin():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
        clearWin()

    mw.winButtonConfirmar.clicked.connect(cadWindows)
    mw.winButtonCancelar.clicked.connect(cancelWin)
    mw.winButtonLimpar.clicked.connect(clearWin)

    # TRATAMENTO OFFICE # <<< ------------------------------------------

    def cadOffice():
        chave = mw.offCod.text().upper()
        verPro = mw.offVersao.text()
        valor = mw.offValor.text()
        versao = mw.offBoxVersao.currentText()

        motivo = motivoOff()
        tipo = 'Office'
        local = 'ESTOQUE'
        data = datAT()

        if chave == '' or verPro == '' or versao == '' or motivo == None:

            mw.offMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.offVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.offBoxVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.offCod.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO office (CHAVE, VERSAOPRO, VERSAO, VALOR, local, data)
                                    VALUES ('{chave}','{verPro}','{versao}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idOffice) FROM office;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{verPro}',
                                '{versao}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearOff()
                mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)

            except pymysql.Error as erro:
                trat = str(erro)
                print(trat)
                codigo = trat[1:5]

                if trat.count('1062'):
                    texto = f'CHAVE INFORMADA JÁ CADASTRADA\n CODIGO MYSQL{codigo}'
                    Dialog.show()
                    dg.LabelDialog.setText(texto)

    def clearOff():
        mw.offCod.clear()
        mw.offVersao.clear()
        mw.offValor.clear()
        mw.offBoxVersao.setCurrentIndex(0)

        mw.offMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.offVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.offBoxVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.offCod.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoOff():
        if mw.offRadioCompra.isChecked() == True:
            compra = mw.offRadioCompra.text()
            return compra

        elif mw.offRadioCadastro.isChecked() == True:
            cadastro = mw.offRadioCadastro.text()
            return cadastro

        elif mw.offRadioProvisorio.isChecked() == True:
            provisorio = mw.offRadioProvisorio.text()
            return provisorio

        elif mw.offRadioOutro.isChecked() == True:
            outros = mw.offRadioOutro.text()
            return outros

    def cancelOff():
        mw.stackedWidgetCad.setCurrentWidget(mw.pageNovoCad)
        clearOff()

    mw.offButtonConfirmar.clicked.connect(cadOffice)
    mw.offButtonCancelar.clicked.connect(cancelOff)
    mw.offButtonLimpar.clicked.connect(clearOff)

    # TRATAMENTO MEMORIA # <<< ------------------------------------------

    def cadMemoria():
        modelo = mw.meBarramento.text()
        marca = mw.meMarca.text()
        condicao = mw.meCondicao.text()
        valor = mw.meValor.text()
        tamanho = mw.meBoxTamanho.currentText()
        plataforma = mw.meBoxPlataforma.currentText()

        motivo = motivoMemo()
        tipo = 'Memoria'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tamanho == '' or motivo == None or plataforma == '':

            mw.meMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.meBarramento.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.meMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.meBoxTamanho.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.meBoxPlataforma.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO memoria (MARCA, MODELO, CONDICAO, TAMANHO, PLATAFORMA, VALOR, TIPO, LOCAL, DATA)
                                VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{plataforma}','{valor}','{tipo}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idMemoria) FROM memoria;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                    '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMonitor()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearMemo():
        mw.meMarca.clear()
        mw.meBarramento.clear()
        mw.meCondicao.clear()
        mw.meBoxTamanho.setCurrentIndex(0)
        mw.meBoxPlataforma.setCurrentIndex(0)
        mw.meValor.clear()

        mw.meMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.meBarramento.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.meMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.meBoxTamanho.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.meBoxPlataforma.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoMemo():
        if mw.meRadioCompra.isChecked() == True:
            compra = mw.meRadioCompra.text()
            return compra

        elif mw.meRadioCadastro.isChecked() == True:
            cadastro = mw.meRadioCadastro.text()
            return cadastro

        elif mw.meRadioProvisorio.isChecked() == True:
            provisorio = mw.meRadioProvisorio.text()
            return provisorio

        elif mw.meRadioOutro.isChecked() == True:
            outros = mw.meRadioOutro.text()
            return outros

    def cancelMemo():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearMemo()

    mw.meButtonConfirmar.clicked.connect(cadMemoria)
    mw.meButtonCancelar.clicked.connect(cancelMemo)
    mw.meButtonLimpar.clicked.connect(clearMemo)

    # TRATAMENTO DISCO # <<< ------------------------------------------

    def cadDisco():
        modelo = mw.disModelo.text()
        marca = mw.disMarca.text()
        condicao = mw.disCondicao.text()
        valor = mw.disValor.text()
        tamanho = mw.disBoxTamanho.currentText()
        tipo = mw.disBoxTipo.currentText()

        motivo = motivoDis()

        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tamanho == '' or motivo == None or tipo == '':

            mw.disMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.disModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.disMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.disBoxTamanho.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.disBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO disco (MARCA, MODELO, CONDICAO, TAMANHO, TIPO, VALOR, LOCAL, DATA)
                                VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{tipo}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idDisco) FROM disco;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                    '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearDis()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearDis():
        mw.disMarca.clear()
        mw.disModelo.clear()
        mw.disCondicao.clear()
        mw.disBoxTamanho.setCurrentIndex(0)
        mw.disBoxTipo.setCurrentIndex(0)
        mw.disValor.clear()

        mw.disMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.disModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.disMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.disBoxTamanho.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.disBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoDis():
        if mw.disRadioCompra.isChecked() == True:
            compra = mw.disRadioCompra.text()
            return compra

        elif mw.disRadioCadastro.isChecked() == True:
            cadastro = mw.disRadioCadastro.text()
            return cadastro

        elif mw.disRadioProvisorio.isChecked() == True:
            provisorio = mw.disRadioProvisorio.text()
            return provisorio

        elif mw.disRadioOutro.isChecked() == True:
            outros = mw.disRadioOutro.text()
            return outros

    def cancelDis():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearDis()

    mw.disButtonConfirmar.clicked.connect(cadDisco)
    mw.disButtonCancelar.clicked.connect(cancelDis)
    mw.disButtonLimpar.clicked.connect(clearDis)

    # TRATAMENTO MOUSE # <<< ------------------------------------------

    def cadMouse():
        modelo = mw.mouModelo.text()
        marca = mw.mouMarca.text()
        condicao = mw.mouCondicao.text()
        valor = mw.mouValor.text()
        tipo = mw.mouBoxTipo.currentText()

        motivo = motivoMou()
        tipo = 'MOUSE: ' + tipo
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or motivo == None or tipo == '':

            mw.mouMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.mouModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.mouMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.mouBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO mouse (MARCA, MODELO, CONDICAO, TIPO, VALOR, LOCAL, DATA)
                                    VALUES ('{marca}','{modelo}','{condicao}','{tipo}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idMouse) FROM mouse;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                        '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMou()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearMou():
        mw.mouMarca.clear()
        mw.mouModelo.clear()
        mw.mouCondicao.clear()
        mw.mouBoxTipo.setCurrentIndex(0)
        mw.mouValor.clear()

        mw.mouMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.mouModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.mouMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.mouBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoMou():
        if mw.mouRadioCompra.isChecked() == True:
            compra = mw.mouRadioCompra.text()
            return compra

        elif mw.mouRadioCadastro.isChecked() == True:
            cadastro = mw.mouRadioCadastro.text()
            return cadastro

        elif mw.mouRadioProvisorio.isChecked() == True:
            provisorio = mw.mouRadioProvisorio.text()
            return provisorio

        elif mw.mouRadioOutro.isChecked() == True:
            outros = mw.mouRadioOutro.text()
            return outros

    def cancelMou():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearMou()

    mw.mouButtonConfirmar.clicked.connect(cadMouse)
    mw.mouButtonCancelar.clicked.connect(cancelMou)
    mw.mouButtonLimpar.clicked.connect(clearMou)

    # TRATAMENTO OUTROS # <<< ------------------------------------------

    def cadOutros():
        nome = mw.ouNome.text()
        modelo = mw.ouModelo.text()
        marca = mw.ouMarca.text()
        condicao = mw.ouCondicao.text()
        valor = mw.ouValor.text()

        motivo = motivoOutros()
        tipo = 'Outros'
        local = 'ESTOQUE'
        data = datAT()

        if nome == '' or motivo == None:

            mw.ouMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.ouNome.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO outros (NOME, MARCA, MODELO, CONDICAO, VALOR, LOCAL, DATA)
                                    VALUES ('{nome}','{marca}','{modelo}','{condicao}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idOutros) FROM outros;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{nome}',
                        '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMou()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearOutros():
        mw.ouNome.clear()
        mw.ouMarca.clear()
        mw.ouModelo.clear()
        mw.ouCondicao.clear()
        mw.ouValor.clear()

        mw.ouMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.ouNome.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoOutros():
        if mw.ouRadioCompra.isChecked() == True:
            compra = mw.ouRadioCompra.text()
            return compra

        elif mw.ouRadioCadastro.isChecked() == True:
            cadastro = mw.ouRadioCadastro.text()
            return cadastro

        elif mw.ouRadioProvisorio.isChecked() == True:
            provisorio = mw.ouRadioProvisorio.text()
            return provisorio

        elif mw.ouRadioOutro.isChecked() == True:
            outros = mw.ouRadioOutro.text()
            return outros

    def cancelOutros():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearOutros()

    mw.ouButtonConfirmar.clicked.connect(cadOutros)
    mw.ouButtonCancelar.clicked.connect(cancelOutros)
    mw.ouButtonLimpar.clicked.connect(clearOutros)

    # TRATAMENTO PAD # <<< ------------------------------------------

    def cadPad():
        modelo = mw.padModelo.text()
        marca = mw.padMarca.text()
        condicao = mw.padCondicao.text()
        valor = mw.padPreco.text()

        motivo = motivoPad()
        tipo = 'Mouse Pad'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or motivo == None:

            mw.padMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.padMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.padModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO mousepad (MARCA, MODELO, CONDICAO, VALOR, LOCAL, DATA)
                                    VALUES ('{marca}','{modelo}','{condicao}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idMousePad) FROM mousepad;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                        '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMou()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearPad():
        mw.padMarca.clear()
        mw.padModelo.clear()
        mw.padCondicao.clear()
        mw.padPreco.clear()

        mw.padMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.padMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.padModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoPad():
        if mw.padRadioCompra.isChecked() == True:
            compra = mw.padRadioCompra.text()
            return compra

        elif mw.padRadioCadastro.isChecked() == True:
            cadastro = mw.padRadioCadastro.text()
            return cadastro

        elif mw.padRadioProvisorio.isChecked() == True:
            provisorio = mw.padRadioProvisorio.text()
            return provisorio

        elif mw.padRadioOutro.isChecked() == True:
            outros = mw.padRadioOutro.text()
            return outros

    def cancelPad():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearPad()

    mw.padButtonConfirmar.clicked.connect(cadPad)
    mw.padButtonCancelar.clicked.connect(cancelPad)
    mw.padButtonLimpar.clicked.connect(clearPad)

    # TRATAMENTO PAD # <<< ------------------------------------------

    def cadTeclado():
        modelo = mw.telModelo.text()
        marca = mw.telMarca.text()
        condicao = mw.telCondicao.text()
        valor = mw.telValor.text()
        tipo = mw.telBoxTipo.currentText()

        motivo = motivoTec()
        tipo = 'Teclado: ' + tipo
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tipo == '' or motivo == None:

            mw.telMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.telMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.telModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.telBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO teclado (MARCA, MODELO, CONDICAO, TIPO, VALOR, LOCAL, DATA)
                                        VALUES ('{marca}','{modelo}','{condicao}','{tipo}','{valor}','{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idTeclado) FROM teclado;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                            '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMou()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearTec():
        mw.telMarca.clear()
        mw.telModelo.clear()
        mw.telCondicao.clear()
        mw.telValor.clear()

        mw.telMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.telMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.telModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.telBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoTec():
        if mw.telRadioCompra.isChecked() == True:
            compra = mw.telRadioCompra.text()
            return compra

        elif mw.telRadioCadastro.isChecked() == True:
            cadastro = mw.telRadioCadastro.text()
            return cadastro

        elif mw.telRadioProvisorio.isChecked() == True:
            provisorio = mw.telRadioProvisorio.text()
            return provisorio

        elif mw.telRadioOutro.isChecked() == True:
            outros = mw.telRadioOutro.text()
            return outros

    def cancelTec():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearTec()

    mw.telButtonConfirmar.clicked.connect(cadTeclado)
    mw.telButtonCancelar.clicked.connect(cancelTec)
    mw.telButtonLimpar.clicked.connect(clearTec)

    # TRATAMENTO SUPORTE # <<< ------------------------------------------

    def cadSuport():
        modelo = mw.supModelo.text()
        marca = mw.supMarca.text()
        condicao = mw.supCondicao.text()
        valor = mw.supValor.text()

        motivo = motivoSup()
        tipo = 'Suporte'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or motivo == None:

            mw.supMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mw.supMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mw.supModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO suporte (MARCA, MODELO, CONDICAO, VALOR, TIPO, LOCAL, DATA)
                                           VALUES ('{marca}','{modelo}','{condicao}','{valor}', '{tipo}', '{local}','{data}');""")

                cur.execute(f"""SELECT MAX(idSuporte) FROM suporte;""")
                result = cur.fetchall()
                result = result[0][0]
                print(result)

                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{result}','{marca}',
                               '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {result} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                clearMou()
                mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearSup():
        mw.supMarca.clear()
        mw.supModelo.clear()
        mw.supCondicao.clear()
        mw.supValor.clear()

        mw.supMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mw.supMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mw.supModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoSup():
        if mw.supRadioCompra.isChecked() == True:
            compra = mw.supRadioCompra.text()
            return compra

        elif mw.supRadioCadastro.isChecked() == True:
            cadastro = mw.supRadioCadastro.text()
            return cadastro

        elif mw.supRadioProvisorio.isChecked() == True:
            provisorio = mw.supRadioProvisorio.text()
            return provisorio

        elif mw.supRadioOutro.isChecked() == True:
            outros = mw.supRadioOutro.text()
            return outros

    def cancelSup():
        mw.stackedWidgetCad.setCurrentWidget(mw.pagePerifericosCad)
        clearSup()

    mw.supButtonConfirmar.clicked.connect(cadSuport)
    mw.supButtonCancelar.clicked.connect(cancelSup)
    mw.supButtonLimpar.clicked.connect(clearSup)



































if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    opNote = QtWidgets.QMainWindow()
    op = Ui_opNote()
    op.setupUi(opNote)

    opDesk = QtWidgets.QMainWindow()
    opd = Ui_opDesk()
    opd.setupUi(opDesk)

    opCell = QtWidgets.QMainWindow()
    opc = Ui_opCell()
    opc.setupUi(opCell)

    opSaidaEstoqueTI = QtWidgets.QMainWindow()
    ops = Ui_opSaidaEstoqueTI()
    ops.setupUi(opSaidaEstoqueTI)

    MainControle = QtWidgets.QMainWindow()
    mc = Ui_MainControle()
    mc.setupUi(MainControle)

    DialogiEstoqueEntrada = QtWidgets.QMainWindow()
    de = Ui_DialogiEstoqueEntrada()
    de.setupUi(DialogiEstoqueEntrada)

    DialogiEstoqueSaida = QtWidgets.QMainWindow()
    ds = Ui_DialogiEstoqueSaida()
    ds.setupUi(DialogiEstoqueSaida)

    DialogiEstoqueBaixa = QtWidgets.QMainWindow()
    dx = Ui_DialogiEstoqueBaixa()
    dx.setupUi(DialogiEstoqueBaixa)

    DialogiConditional = QtWidgets.QMainWindow()
    di = Ui_DialogiConditional()
    di.setupUi(DialogiConditional)

    Positive = QtWidgets.QDialog()
    po = Ui_Positive()
    po.setupUi(Positive)

    MainLogin = QtWidgets.QMainWindow()
    ui = Ui_MainLogin()
    ui.setupUi(MainLogin)

    MainEstoque = QtWidgets.QMainWindow()
    mw = Ui_MainEstoque()
    mw.setupUi(MainEstoque)

    MainEEstoque = QtWidgets.QMainWindow()
    ee = Ui_MainEEstoque()
    ee.setupUi(MainEEstoque)

    Dialog = QtWidgets.QDialog()
    dg = Ui_Dialog()
    dg.setupUi(Dialog)

    login(ui)
    controle()
    estoqueTi()

    MainLogin.showMaximized()
    # MainEstoque.showMaximized()
    sys.exit(app.exec_())
