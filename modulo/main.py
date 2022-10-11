from login import *
from ControleTI import *
from EstoqueTI import *
from entradaEstoque import *
from Dialog import *
from DialogCondicional import *
from Positive import *
from opNote import *
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

    # BUTÕES DE NAVEGAÇÃO DO MENU ######################################################################################
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
                    f"""INSERT INTO bdsister.computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
                        SERVICETAG, TEAMVIEWER, REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO,
                        FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, ANTEVIRUS,
                        DESCRICAO, TIPO, LOCAL, DATA)
                    
                        VALUES ('{imb}','{marca}','{modelo}','{condicao}','{ano}','{tela}','{preco}',
                        '{service}','{team}','{rede}','{disco}','{exp}','{car}','{pro}','{marPro}',
                        '{frePro}','{gePro}','{ram}','{verRam}','{freRam}','{expRam}','{ant}',
                        '{'descricao'}','{tipo}','{local}','{data}');""")

            except:
                print('algo deu errado')

    def win():
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
                                    mc.notFrameWindows.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                    mc.notVerWin.setText(versao)
                                    mc.notCodWin.setText(str(id))

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

    def off():
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
                                    mc.notFrameOffice.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                    mc.notVerOff.setText(versao)
                                    mc.notCodOff.setText(str(id))

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

        mc.notFrameWindows.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.notCodWin.setText('------------')
        mc.notVerWin.setText('------------')

        mc.notFrameOffice.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.notCodOff.setText('------------')
        mc.notVerOff.setText('------------')

    def user():
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
                    con.close()

                    nome = dados[0][1]
                    cargo = dados[0][4]
                    idu = dados[0][0]

                    if dados == ():
                        texto = 'Usuário não encontrado\n certifique se de que o mesmo esta cadastrado'
                        op.notlabelUser.setText(texto)

                    else:
                        texto = 'Colaborador Encontrado'
                        mc.notFrameUser.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                        mc.notLabelUser.setText(nome)
                        mc.notCarUser.setText(cargo)
                        mc.notCodUser.setText(str(idu))

                        Positive.show()
                        op.notLineUser.clear()
                        po.LabelDialog.setText(texto)
                        opNote.close()


                except:
                    texto = 'ALGO DEU ERRADO!'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

        op.notButtonUser.clicked.connect(pUser)

    mc.notButtonUser.clicked.connect(user)
    mc.notButtonWin.clicked.connect(win)
    mc.notButtonOff.clicked.connect(off)
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

    opNote = QtWidgets.QMainWindow()
    op = Ui_opNote()
    op.setupUi(opNote)

    MainControle = QtWidgets.QMainWindow()
    mc = Ui_MainControle()
    mc.setupUi(MainControle)

    DialogiConditional = QtWidgets.QMainWindow()
    di = Ui_DialogiConditional()
    di.setupUi(DialogiConditional)

    Positive = QtWidgets.QDialog()
    po = Ui_Positive()
    po.setupUi(Positive)

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
