from login import *
from ControleTI import *
from EstoqueTI import *
from entradaEstoque import *
from Dialog import *
from DialogCondicional import *
from DialogCondicionalOne import *
from DialogCondicionalTwe import *
import db
from datetime import date
import pymysql


'''TRATAMENTO LOGIN ================================================================================================='''


def login(ui):
    # Tratamento do POPUP -----------------------------------------------------------------
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
                    texto = 'BEM VINDO ' + Usuario.upper()
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


'''TRATAMENTO HOME =================================================================================================='''
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

'''TRATAMENTO CONTROLE TI ==========================================================================================='''


def controle():
    MainControle.setWindowTitle('PAINEL DE CONTROLE TI')

    # BUTÕES DE NAVEGAÇÃO ##############################################################################################
    def ButtonEstoqueTI():
        MainEstoque.showMaximized()
        MainControle.close()
    mc.pushButtonEstoque.clicked.connect(ButtonEstoqueTI)

    def buttonVoltar():
        MainLogin.showMaximized()
        MainEstoque.close()
    mc.pushButtonVoltar.clicked.connect(buttonVoltar)

    # CADASTRO DE ITENS NO BANCO #######################################################################################
    def cadNote():
        imb = mc.notIMB.text()
        marca = mc.notMarca.text()
        modelo = mc.notModelo.text()
        condicao = mc.notCondicao.text()
        ano = mc.notAno.text()
        preco = mc.notPreco.text()
        service = mc.notService.text()
        rede = mc.notRede.text()
        team = mc.notTeam.text()
        ant = mc.notBoxAntevirus.currentText()
        tela = mc.notBoxTela.currentText()
        car = mc.notBoxCarregador.currentText()
        pro = mc.notPro.text()
        marPro = mc.notMarcaPro.text()
        frePro = mc.notFrePro.text()
        gePro = mc.notBoxGeracao.currentText()
        disco = mc.notBoxSSD.currentText()
        exp = mc.notBoxExp.currentText()
        ram = mc.notRam.text()
        verRam = mc.notVerRam.text()
        freRam = mc.notFreRam.text()
        expRam = mc.notBoxExpRam.currentText()

        motivo = ''

        tipo = ''
        local = ''
        data = ''

        print(imb, marca, modelo, condicao, ano, preco, service, rede, team, ant, tela, car, pro, marPro, frePro,
              gePro, disco, exp, ram, verRam, freRam, expRam)

        def checkcamps():
            if motivo == '' or marca == '' or modelo == '' or service == '' or rede == '' or \
                    car == '' or pro == '' or gePro == '' or ram == '' or verRam == '':
                mc.frameMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
                mc.notMarca.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notModelo.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notService.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notRede.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notBoxCarregador.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notPro.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notBoxGeracao.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notRam.setStyleSheet('background-color: rgb(255, 192, 193);')
                mc.notVerRam.setStyleSheet('background-color: rgb(255, 192, 193);')
                mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
                mc.notLabelDialog.setText(mensage)

        def salveNote():
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
                    SERVICETAG, TEAMVIEWER, REDE, SSD, EXPANCIVEL, CARREGADOR, RPOCESSADOR, MARCAPRO,
                    FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, ANTEVIRUS, LOCAL, DATA)
                    
                    VALUES ('{imb}','{marca}','{modelo}','{condicao}','{ano}','{tela}','{preco}','{service}','{team}',
                    '{rede}','{disco}','{exp}','{car}','{pro}','{marPro}','{frePro}','{gePro}','{ram}','{verRam}',
                    '{freRam}','{expRam}','{ant}','{tipo}','{local}','{data}');""")

            except:
                print('algo deu errado')

    def lpNote():
        mc.notIMB.clear()
        mc.notMarca.clear()
        mc.notModelo.clear()
        mc.notCondicao.clear()
        mc.notAno.clear()
        mc.notPreco.clear()
        mc.notService.clear()
        mc.notRede.clear()
        mc.notTeam.clear()
        mc.notBoxAntevirus.setCurrentIndex(0)
        mc.notBoxTela.setCurrentIndex(0)
        mc.notBoxCarregador.setCurrentIndex(0)
        mc.notPro.clear()
        mc.notMarcaPro.clear()
        mc.notFrePro.clear()
        mc.notBoxGeracao.setCurrentIndex(0)
        mc.notBoxSSD.setCurrentIndex(0)
        mc.notBoxExp.setCurrentIndex(0)
        mc.notRam.clear()
        mc.notVerRam.clear()
        mc.notFreRam.clear()
        mc.notBoxExpRam.setCurrentIndex(0)
        mc.frameMotivo.setStyleSheet('border: 2px solid;border-color: rgb(255, 255, 255);border-radius: 10px;')
        mc.notMarca.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notModelo.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notService.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notRede.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notBoxCarregador.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notPro.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notBoxGeracao.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notRam.setStyleSheet('background-color: rgb(255, 255, 255);')
        mc.notVerRam.setStyleSheet('background-color: rgb(255, 255, 255);')

    mc.notButtonLimpar.clicked.connect(lpNote)
    mc.notButtonConfirmar.clicked.connect(cadNote)









'''TRATAMENTO ESTOQUE TI ============================================================================================'''


def estoqueTi():
    MainEstoque.setWindowTitle('ESTOQUE')

    #  Acionamento Botões menu -----------------------------------------------------------------------------------------
    def ButtonVoltar():
        mw.lineEdit_pesquisar.clear()
        MainEstoque.close()
        ui.frame_erro.hide()
        MainLogin.showMaximized()

    mw.pushButtonVoltar.clicked.connect(ButtonVoltar)

    def ButtonChamados():
        mw.lineEdit_pesquisar.clear()
        pass

    mw.pushButtonChamados.clicked.connect(ButtonChamados)

    def ButtonControle():
        mw.lineEdit_pesquisar.clear()
        MainControle.showMaximized()
        MainEstoque.close()

    mw.pushButtonControle.clicked.connect(ButtonControle)

    def ButtonEstoque():
        quantiTable()
        mw.lineEdit_pesquisar.clear()
        pass

    mw.pushButtonEstoque.clicked.connect(ButtonEstoque)

    #  Acionamento Botões Submenu --------------------------------------------------------------------------------------
    def ButtonInicio():
        quantiTable()
        carregarDados()
        mw.stackedWidget.setCurrentWidget(mw.pageHome)

    mw.pushButton_Inicio.clicked.connect(ButtonInicio)

    def ButtonGestao():
        mw.stackedWidget.setCurrentWidget(mw.PageGestao)

    mw.pushButtonGestao.clicked.connect(ButtonGestao)

    def ButtonHistorico():
        mw.stackedWidget.setCurrentWidget(mw.pageHistorico)
        carregarDados()
    mw.pushButtonHistorico.clicked.connect(ButtonHistorico)

    #  Acionamento Botões PAGE GESTÃO-----------------------------------------------------------------------------------

    def ButtonNovo():
        mw.stackedWidget.setCurrentWidget(mw.pageModulos)
        mw.stackedWidgetMenu.setCurrentWidget(mw.pageNovo)
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
        print('click')

    mw.pushButtonNovo.clicked.connect(ButtonNovo)

    def ButtonEntrada():
        mw.stackedWidget.setCurrentWidget(mw.pageModulos)
        mw.stackedWidgetMenu.setCurrentWidget(mw.pageEntrada)
        print('click')

    mw.pushButtonEntrada.clicked.connect(ButtonEntrada)

    def ButtonSaida():
        mw.stackedWidget.setCurrentWidget(mw.pageModulos)
        mw.stackedWidgetMenu.setCurrentWidget(mw.pageSaida)
        mw.stackedWidgetSaida.setCurrentWidget(mw.pagSaida)
        print('click')

    mw.pushButtonSaida.clicked.connect(ButtonSaida)

    #  Acionamento Botões PAGE NOVO-----------------------------------------------------------------------------------
    def ButtonNote():
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageNovoNote)

    mw.pushNote.clicked.connect(ButtonNote)

    def ButtonCelu():
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageNovoCelu)

    mw.pushCelular.clicked.connect(ButtonCelu)

    def ButtonPeri():
        MainEEstoque.show()

    mw.pushPerifericos.clicked.connect(ButtonPeri)

    def ButtonMon():
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageNovoMonitor)

    mw.pushMonitor.clicked.connect(ButtonMon)

    #  pré visualização de quantidade ----------------------------------------------------------------------------------
    def quantiTable():
        cursor = db.conMySQL()
        cursor.execute(f"""SELECT * FROM computer;""")
        notebook = len(cursor.fetchall())
        mw.labelNotebook.setText(str(notebook))
        mw.labelTotalnotebook.setText(str(notebook))

        cursor.execute(f"""SELECT * FROM celular;""")
        celular = len(cursor.fetchall())
        mw.labelCelular.setText(str(celular))
        mw.labelTotalcelular.setText(str(celular))

        cursor.execute(f"""SELECT * FROM memoria;""")
        memoria = len(cursor.fetchall())
        mw.labelMemoria.setText(str(memoria))
        mw.labelTotalmemoria.setText(str(memoria))

        cursor.execute(f"""SELECT * FROM disco;""")
        disco = len(cursor.fetchall())
        mw.labelSSD.setText(str(disco))
        mw.labelTotaldisco.setText(str(disco))

        cursor.execute(f"""SELECT * FROM mouse;""")
        mouse = len(cursor.fetchall())
        mw.labelMouse.setText(str(mouse))
        mw.labelTotalMouse.setText(str(mouse))

        cursor.execute(f"""SELECT * FROM mousePad;""")
        pad = len(cursor.fetchall())
        mw.labelMousepad.setText(str(pad))
        mw.labelTotalPad.setText(str(pad))

        cursor.execute(f"""SELECT * FROM teclado;""")
        teclado = len(cursor.fetchall())
        mw.labelTeclado.setText(str(teclado))
        mw.labelTotalTeclado.setText(str(teclado))

        cursor.execute(f"""SELECT * FROM suporte;""")
        suporte = len(cursor.fetchall())
        mw.labelSuporte.setText(str(suporte))
        mw.labelTotalSuporte.setText(str(suporte))

        cursor.execute(f"""SELECT * FROM email;""")
        email = len(cursor.fetchall())
        mw.labelEmail.setText(str(email))
        mw.labelTotalEmail.setText(str(email))

        cursor.execute(f"""SELECT * FROM office;""")
        office = len(cursor.fetchall())
        mw.labelOffice.setText(str(office))
        mw.labelTotalOffice.setText(str(office))

        cursor.execute(f"""SELECT * FROM windows;""")
        windows = len(cursor.fetchall())
        mw.labelWindows.setText(str(windows))
        mw.labelTotalWindows.setText(str(windows))

        cursor.execute(f"""SELECT * FROM outros;""")
        outros = len(cursor.fetchall())
        mw.labelOutros.setText(str(outros))
        mw.labelTotalOutros.setText(str(outros))

        cursor.close()
        return notebook, celular, memoria, disco, mouse, pad, teclado, suporte, email, office, windows

    quantiTable()

    #  Acionamento Botões de icones de TABELA --------------------------------------------------------------------------

    mw.ButtonNotebook.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageNotebook))
    mw.ButtonCelular.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageCelular))
    mw.ButtonMemoria.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMemoria))
    mw.ButtonSSD.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageDisco))
    mw.ButtonMouse.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMouse))
    mw.ButtonMousePad.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pagePad))
    mw.ButtonTeclado.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageTeclado))
    mw.ButtonSuporte.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageSuporte))
    mw.ButtonEmail.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageEmail))
    mw.ButtonOffice.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageOffice))
    mw.ButtonWindows.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageWindows))
    mw.ButtonOutros.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageOutros))

    ''' Visualização de items da tabela ============================================================================='''

    def carregarDados():
        con = db.conMySQL()
        con.execute("""SELECT * FROM computer""")
        result = con.fetchall()

        mw.tableWidgetNotebook.clearContents()
        mw.tableWidgetNotebook.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetNotebook.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM celular""")
        result = con.fetchall()

        mw.tableWidgetCelular.clearContents()
        mw.tableWidgetCelular.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetCelular.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM memoria""")
        result = con.fetchall()

        mw.tableWidgetMemo.clearContents()
        header = mw.tableWidgetMemo.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        mw.tableWidgetMemo.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetMemo.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM disco""")
        result = con.fetchall()

        mw.tableWidgetDis.clearContents()
        header = mw.tableWidgetDis.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetDis.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetDis.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM mouse""")
        result = con.fetchall()

        mw.tableWidgetMouse.clearContents()
        header = mw.tableWidgetMouse.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetMouse.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetMouse.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM mousepad""")
        result = con.fetchall()

        mw.tableWidgetPad.clearContents()
        header = mw.tableWidgetPad.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetPad.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetPad.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM teclado""")
        result = con.fetchall()

        mw.tableWidgetTec.clearContents()
        header = mw.tableWidgetTec.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetTec.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetTec.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM suporte""")
        result = con.fetchall()

        mw.tableWidgetSuporte.clearContents()
        header = mw.tableWidgetSuporte.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetSuporte.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetSuporte.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM email""")
        result = con.fetchall()

        mw.tableWidgetEmail.clearContents()
        header = mw.tableWidgetEmail.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetEmail.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetEmail.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM office""")
        result = con.fetchall()

        mw.tableWidgetOffice.clearContents()
        header = mw.tableWidgetOffice.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetOffice.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetOffice.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM windows""")
        result = con.fetchall()

        mw.tableWidgetWindows.clearContents()
        header = mw.tableWidgetWindows.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetWindows.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetWindows.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""SELECT * FROM outros""")
        result = con.fetchall()

        mw.tableWidgetOutros.clearContents()
        header = mw.tableWidgetOutros.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetOutros.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetOutros.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

        con.execute("""select * from historico order by data desc LIMIT 18;""")
        result = con.fetchall()

        mw.tableWidgetHistorico.clearContents()
        header = mw.tableWidgetHistorico.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # -------------------------------------------------------
        mw.tableWidgetHistorico.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetHistorico.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))
        con.close()

    carregarDados()
    mw.ButtonNoteView.clicked.connect(carregarDados)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    MainEstoque = QtWidgets.QMainWindow()
    MainEEstoque = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()

    MainControle = QtWidgets.QMainWindow()
    mc = Ui_MainControle()
    mc.setupUi(MainControle)

    DialogiConditional = QtWidgets.QMainWindow()
    di = Ui_DialogiConditional()
    di.setupUi(DialogiConditional)

    DialogiConditionalOne = QtWidgets.QMainWindow()
    di1 = Ui_DialogiConditionalOne()
    di1.setupUi(DialogiConditionalOne)

    DialogiConditionalTwe = QtWidgets.QMainWindow()
    di2 = Ui_DialogiConditionalTwe()
    di2.setupUi(DialogiConditionalTwe)

    ui = Ui_MainLogin()
    mw = Ui_MainEstoque()
    ee = Ui_MainEEstoque()
    dg = Ui_Dialog()

    ui.setupUi(MainLogin)
    mw.setupUi(MainEstoque)
    ee.setupUi(MainEEstoque)
    dg.setupUi(Dialog)

    MainLogin.showMaximized()
    login(ui)
    estoqueTi()
    controle()

    sys.exit(app.exec_())
