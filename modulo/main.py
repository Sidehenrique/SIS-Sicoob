from login import *
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


'''TRATAMENTO ESTOQUE TI ============================================================================================'''


def estoqueTi(mw, ee):
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
        pass

    mw.pushButtonControle.clicked.connect(ButtonControle)

    def ButtonEstoque():
        quantiTable()
        mw.lineEdit_pesquisar.clear()
        pass

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

        con.execute("""SELECT * FROM historico""")
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

    ''' Cadastro de Items do estoque no banco ======================================================================='''
    # mudar o comboBox seletor dos items de cadastro
    ee.stackedWidgetCadastro.setCurrentIndex(0)
    ee.comboBoxSeletorGeral.activated['int'].connect(ee.stackedWidgetCadastro.setCurrentIndex)
    QtCore.QMetaObject.connectSlotsByName(MainEEstoque)

    ################################################--NOTEBOOK--########################################################
    def cadastrarNote():
        tipo = mw.BoxNoteItem.currentText()
        motivo = mw.BoxNoteMotivo.currentText()
        imb = mw.notIMB.text()
        marca = mw.notMarca.text().upper()
        modelo = mw.notModelo.text().upper()
        condicao = mw.notCondicao.text().upper()
        anoFab = mw.notAno.text()
        tela = mw.notBoxTela.currentText()
        disco = mw.notBoxSSD.currentText()
        DiscoExp = mw.notBoxExp.currentText()
        preco = mw.notPreco.text()
        carregador = mw.notBoxCarregador.currentText()
        processador = mw.notPro.text().upper()
        marcaPro = mw.notMarcaPro.text().upper()
        frePro = mw.notFrePro.text().upper()
        geracaoPro = mw.notBoxGeracao.currentText()
        ram = mw.notRam.text().upper()
        ramMod = mw.notVerRam.text().upper()
        freRam = mw.notFreRam.text()
        ramExp = mw.notBoxExpRam.currentText()

        descricao = mw.notDecricao.text()
        data = date.today()
        serviceTag = mw.notService.text().upper()
        teamViewer = mw.notTeam.text().upper()
        anteVirus = mw.notBoxAntevirus.currentText()
        nomeRede = mw.notRede.text().upper()
        local = 'ESTOQUE'
        windows = mw.notWindows.text().upper()
        office = mw.notOffice.text().upper()

        idWindows = mw.labelViewerWin.text().upper()
        idOffice = mw.labelViwerOff.text().upper()

        '''Essa condicional é responsavel por verificar e tratar se tiver campos obrigatoris vazios'''
        if tipo == '' or motivo == '' or marca == '' or modelo == '' or serviceTag == '' or nomeRede == '' or \
                carregador == '' or processador == '' or geracaoPro == '' or ram == '' or ramMod == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            mw.BoxNoteMotivo.setStyleSheet("border: 1px solid rgb(255, 0, 0);")
            mw.BoxNoteItem.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notService.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notRede.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notBoxCarregador.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notBoxGeracao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.notVerRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.labelNoteMensage.setText(mensagem)

        ## TRATAMENTO DE SAVE NO BANCO:

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
                   SERVICETAG, TEAMVIEWER,REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO,
                   FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, LICENCAWINDOWS, LICENCAOFFICE,
                   ANTEVIRUS, DESCRICAO, LOCAL, DATA, idWindows, idOffice)

                   VALUES ('{imb}','{marca}','{modelo}','{condicao}','{anoFab}','{tela}','{preco}',
                   '{serviceTag}','{teamViewer}','{nomeRede}','{disco}','{DiscoExp}','{carregador}',
                   '{processador}','{marcaPro}','{frePro}','{geracaoPro}','{ram}','{ramMod}','{freRam}',
                   '{ramExp}','{windows}','{office}','{anteVirus}','{descricao}','{local}','{data}','{idWindows}','{idOffice}');""")

                cursor.execute(f"""SELECT MAX(idComputer) FROM computer;""")
                cur = cursor.fetchall()
                id_computer = cur[0][0]
                print(id_computer)

                cursor.execute(
                    f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id_computer}','{marca}','{modelo}',
                    '{motivo}','{local}','{data}');""")

                cursor.close()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                limparCampsNote()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                dg.LabelDialog.setText('ITEM NÃO CADASTRADO\n'+str(erro))
                Dialog.show()
                print(erro)

    def limWin():
        mw.labelViewerWin.clear()
        mw.labelNoteMensage.clear()
        mw.notWindows.clear()

    def limOff():
        mw.labelViwerOff.clear()
        mw.labelNoteMensage.clear()
        mw.notOffice.clear()

    def verWin():
        windows = mw.notWindows.text().upper()
        if len(windows) != 25:
            texto = 'O TAMANHO DA CHAVE NÃO CONFERE\nENTRE COM 25 DIGITOS SEM PONTOS'
            dg.LabelDialog.setText(texto)
            Dialog.show()

        else:
            try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
                cur = db.conMySQL()
                cur.execute(f"""SELECT * FROM windows WHERE CHAVE = '{windows}';""")  # ------ Que Contenha
                idw = cur.fetchall()
                print(windows + '<--- Este é oque o usuario digitou')
                print(idw)

                if idw == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
                    texto = 'ESTA CHAVE NÃO EXISTE\nCADASTRE A CHAVE PRIMEIRO'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

                if idw != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
                    chave = idw[0][1]
                    id = idw[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID OFFICE) int
                    print(chave)
                    print(id)

                    try:  # <---------- vai pesquisar na tabela computer se essa (ID OFFICE) esta vinculada com alguma maquina
                        cur.execute(f"""SELECT * FROM computer WHERE idWindows = {id};""")
                        idNote = cur.fetchall()
                        print(idNote)
                        cur.close()

                        if idNote == ():  # <--------- se retornar tupla vazia não achou (ID WINDOWS) vinculado a alguma maquina
                            texto = 'CHAVE WINDOWS DISPONIVEL!'
                            mw.labelViewerWin.setText(str(id))
                            mw.labelViewerWin.setStyleSheet("color: rgb(37, 163, 8);")
                            mw.labelNoteMensage.setText('CHAVE DISPONIVEL')
                            mw.labelNoteMensage.setStyleSheet("color: rgb(37, 163, 8);")
                            dg.LabelDialog.setText(texto)
                            Dialog.show()
                            return id

                        else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                            print(f'ID COMPUTER {idNote[0][0]} ID WINDOWS {idNote[0][28]}')
                            texto = f'ESTA ID WINDOWS {idNote[0][28]}\nJA ESTA EM USO NO COMPUTER {idNote[0][0]}'
                            dg.LabelDialog.setText(texto)
                            mw.labelNoteMensage.setText('CHAVE INDISPONIVEL!')
                            Dialog.show()

                    except:
                        texto = 'ALGO DEU ERRADO!'
                        dg.LabelDialog.setText(texto)
                        Dialog.show()

            except:
                texto = 'ALGO DEU ERRADO!!'
                dg.LabelDialog.setText(texto)
                Dialog.show()

    def verOff():
        office = mw.notOffice.text().upper()
        if len(office) != 25:
            texto = 'O TAMANHO DA CHAVE NÃO CONFERE\nENTRE COM 25 DIGITOS SEM PONTOS'
            dg.LabelDialog.setText(texto)
            Dialog.show()

        else:
            try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
                cur = db.conMySQL()
                cur.execute(f"""SELECT * FROM office WHERE CHAVE = '{office}';""")  # ------ Que Contenha
                ido = cur.fetchall()
                print(office + '<--- Este é oque o usuario digitou')
                print(ido)

                if ido == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
                    texto = 'ESTA CHAVE NÃO EXISTE\nCADASTRE A CHAVE PRIMEIRO'
                    dg.LabelDialog.setText(texto)
                    Dialog.show()

                if ido != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
                    chave = ido[0][1]
                    id = ido[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID OFFICE) int
                    print(chave)
                    print(id)

                    try:  # <---------- vai pesquisar na tabela computer se essa (ID OFFICE) esta vinculada com alguma maquina
                        cur.execute(f"""SELECT * FROM computer WHERE idOffice = {id};""")
                        idNote = cur.fetchall()
                        print(idNote)
                        cur.close()

                        if idNote == ():  # <--------- se retornar tupla vazia não achou (ID WINDOWS) vinculado a alguma maquina
                            texto = 'CHAVE OFFICE DISPONIVEL!'
                            mw.labelViwerOff.setText(str(id))
                            mw.labelViwerOff.setStyleSheet("color: rgb(37, 163, 8);")
                            mw.labelNoteMensage.setText('CHAVE DISPONIVEL')
                            mw.labelNoteMensage.setStyleSheet("color: rgb(37, 163, 8);")
                            dg.LabelDialog.setText(texto)
                            Dialog.show()
                            return id

                        else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                            print(f'ID COMPUTER {idNote[0][0]} ID OFFICE {idNote[0][29]}')
                            texto = f'ESTA ID OFFICE {idNote[0][29]}\nJÁ ESTA EM USO NO COMPUTER {idNote[0][0]}'
                            dg.LabelDialog.setText(texto)
                            mw.labelNoteMensage.setText('CHAVE INDISPONIVEL!')
                            Dialog.show()

                    except:
                        texto = 'ALGO DEU ERRADO'
                        dg.LabelDialog.setText(texto)
                        Dialog.show()

            except:
                texto = 'ALGO DEU ERRADO'
                dg.LabelDialog.setText(texto)
                Dialog.show()

    def limparCampsNote():
        mw.notIMB.clear()
        mw.notMarca.clear()
        mw.notModelo.clear()
        mw.notCondicao.clear()
        mw.notAno.clear()
        mw.notPreco.clear()
        mw.notService.clear()
        mw.notTeam.clear()
        mw.notRede.clear()
        mw.notPro.clear()
        mw.notMarcaPro.clear()
        mw.notFrePro.clear()
        mw.notRam.clear()
        mw.notVerRam.clear()
        mw.notFreRam.clear()
        mw.notWindows.clear()
        mw.notOffice.clear()
        mw.notDecricao.clear()
        mw.labelNotebook.clear()
        mw.labelViwerOff.clear()
        mw.labelNoteMensage.clear()
        mw.notOffice.clear()
        mw.labelViewerWin.clear()
        mw.labelNoteMensage.clear()
        mw.notWindows.clear()

    def cancelarCadNote():
        limparCampsNote()
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)

    mw.limWindows.clicked.connect(limWin)
    mw.limOffice.clicked.connect(limOff)
    mw.PesWindows.clicked.connect(verWin)
    mw.PesOffice.clicked.connect(verOff)
    mw.pushButtonCancelarNote.clicked.connect(cancelarCadNote)
    mw.pushButtonSalvarNote.clicked.connect(cadastrarNote)

    #################################################--CELULAR--########################################################
    def cadastrarCelu():
        imei = mw.celMeiOne.text()
        imei2 = mw.celMeiTwo.text()
        marca = mw.celMarca.text()
        modelo = mw.celModelo.text()
        condicao = mw.celEstado.text()
        anofab = mw.celAnoFab.text()
        cor = mw.celCor.text()
        preco = mw.celPreco.text()
        processador = mw.celPro.text()
        modeloPro = mw.celModPro.text()
        frequencia = mw.celFrePro.text()
        ram = mw.celRam.text()
        bateria = mw.celbat.text()
        sistema = mw.notBoxSitema.currentText()
        microSD = mw.celBoxMicro.currentText()
        memoria = mw.celMemo.text()
        dual = mw.celBoxDual.currentText()
        chip1 = mw.celBoxChipOne.currentText()
        chip2 = mw.celBoxChipTwo.currentText()
        numero1 = mw.celNumeroOne.text()
        numero2 = mw.celNumeroTwo.text()
        descricao = mw.celDescricao.text()
        motivo = mw.BoxCelMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()


        if imei == '' or marca == '' or modelo == '' or condicao == '' or cor == '' or ram == '' or memoria == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            mw.celMeiOne.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celEstado.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celCor.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celMemo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.BoxCelMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.label_Celular.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO celular (imei, imei2, marca, modelo, condicao, anofab, cor, 
                    preco, processador, modpro, frepro, ram, bateria, sistema, 
                    micro, memoint, DUALCHIP, chip, chip2, numero, numero2, descricao, local, data)

                    VALUES ('{imei}','{imei2}','{marca}','{modelo}','{condicao}','{anofab}','{cor}',
                            '{preco}','{processador}','{modeloPro}','{frequencia}','{ram}','{bateria}','{sistema}',
                            '{microSD}','{memoria}','{dual}','{chip1}','{chip2}','{numero1}','{numero2}','{descricao}',
                            '{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idCelular) FROM celular;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(
                    f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','CELULAR','{id}','{marca}','{modelo}',
                            '{motivo}','{local}','{data}');""")
                cursor.close()

                limparCampsCelu()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                mw.label_Celular.setStyleSheet("rgb(255, 0, 0);")
                mw.label_Celular.setText(mensageErro)

    def limparCampsCelu():
        mw.celMeiOne.clear()
        mw.celMeiTwo.clear()
        mw.celMarca.clear()
        mw.celModelo.clear()
        mw.celEstado.clear()
        mw.celAnoFab.clear()
        mw.celCor.clear()
        mw.celPreco.clear()
        mw.celModPro.clear()
        mw.celMemo.clear()
        mw.celPro.clear()
        mw.celDescricao.clear()
        mw.celFrePro.clear()
        mw.celRam.clear()
        mw.celbat.clear()
        mw.celNumeroOne.clear()
        mw.celNumeroTwo.clear()
        mw.label_Celular.clear()

    def cancelarCadCelu():
        limparCampsCelu()
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)

    mw.pushButtonCadastraCelular.clicked.connect(cadastrarCelu)
    mw.pushButtonCancelarCelular.clicked.connect(cancelarCadCelu)

    #################################################--MEMORIA--########################################################
    def cadastrarMemo():
        tipo = ee.comboBoxSeletorGeral.currentText()
        marca = ee.meMarca.text()
        modelo = ee.meModelo.text()
        condicao = ee.meCondicao.text()
        tamanho = ee.meBoxTamanho.currentText()
        plataforma = ee.mePlataforma.text()
        valor = ee.meValor.text()
        descricao = ee.meDescricao.text()
        motivo = ee.BoxMemoMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if marca == '' or modelo == '' or tamanho == '' or plataforma == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.meMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.meModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.meBoxTamanho.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.mePlataforma.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxMemoMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Memoria.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Memoria (marca,modelo,condicao,tamanho,plataforma,valor,descricao,data)
                    VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{plataforma}','{valor}'
                    ,'{descricao}','{data}');""")

                cursor.execute(f"""SELECT MAX(idMemoria) FROM memoria;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(
                    f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                            '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsMemo()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Memoria.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Memoria.setText(mensageErro)

    def limparCampsMemo():
        ee.meMarca.clear()
        ee.meModelo.clear()
        ee.meCondicao.clear()
        ee.mePlataforma.clear()
        ee.meValor.clear()
        ee.meDescricao.clear()
        ee.label_Memoria.clear()
        ee.BoxMemoMotivo.setCurrentIndex(0)
        ee.meBoxTamanho.setCurrentIndex(0)

    def cancelarCadMemo():
        limparCampsMemo()
        MainEEstoque.close()

    ee.pushButtonCadastraMemo.clicked.connect(cadastrarMemo)
    ee.pushButtonCancelarMemo.clicked.connect(cancelarCadMemo)

    #################################################-- DISCO --########################################################
    def cadastrarDisco():
        marca = ee.disMarca.text()
        modelo = ee.disModelo.text()
        condicao = ee.disCondicao.text()
        tamanho = ee.disBoxTamanho.currentText()
        valor = ee.disValor.text()
        descricao = ee.disDescricao.text()
        data = date.today()

        tipo = ee.disBoxTipo.currentText()
        local = 'ESTOQUE'
        motivo = ee.BoxDiscoMotivo.currentText()

        if marca == '' or tamanho == '' or tipo == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.disMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.disModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.disBoxTamanho.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxDiscoMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.comboBoxTipo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Disco.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Disco (marca, modelo, condicao, tamanho, tipo, valor, descricao, local, data)
                    VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{tipo}','{valor}','{descricao}',
                    '{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idDisco) FROM disco;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsDisco()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Disco.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Disco.setText(mensageErro)

    def limparCampsDisco():
        ee.disMarca.clear()
        ee.disModelo.clear()
        ee.disCondicao.clear()
        ee.disValor.clear()
        ee.disDescricao.clear()
        ee.label_Disco.clear()
        ee.BoxDiscoMotivo.setCurrentIndex(0)
        ee.disBoxTamanho.setCurrentIndex(0)
        ee.disBoxTipo.setCurrentIndex(0)

    def cancelarCadDisco():
        limparCampsDisco()
        MainEEstoque.close()

    ee.pushButtonCadastraDisco.clicked.connect(cadastrarDisco)
    ee.pushButtonCancelarDisco.clicked.connect(cancelarCadDisco)

    #################################################-- MOUSE --########################################################
    def cadastrarMouse():
        marca = ee.moMarca.text()
        modelo = ee.moModelo.text()
        condicao = ee.moCondicao.text()
        tipo = ee.moBoxTipo.currentText()
        valor = ee.moValor.text()
        descricao = ee.moDescricao.text()
        data = date.today()
        motivo = ee.BoxMouseMotivo.currentText()
        local = 'ESTOQUE'

        if marca == '' or modelo == '' or tipo == '' or motivo =='':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão devidamente preenchidos'
            ee.moMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.moModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.moCondicao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.moBoxTipo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxMouseMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Mouse.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Mouse (marca,modelo,condicao,tipo,valor,descricao,local,data)
                    VALUES ('{marca}','{modelo}','{condicao}','{tipo}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idMouse) FROM mouse;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsMouse()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Disco.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Disco.setText(mensageErro)

    def limparCampsMouse():
        ee.moMarca.clear()
        ee.moModelo.clear()
        ee.moCondicao.clear()
        ee.moValor.clear()
        ee.moDescricao.clear()
        ee.label_Mouse.clear()
        ee.BoxMouseMotivo.setCurrentIndex(0)
        ee.moBoxTipo.setCurrentIndex(0)

    def cancelarCadMouse():
        limparCampsMouse()
        MainEEstoque.close()

    ee.pushButtonCadastraMouse.clicked.connect(cadastrarMouse)
    ee.pushButtonCancelarMouse.clicked.connect(cancelarCadMouse)

    ###############################################-- MOUSE PAD --######################################################
    def cadastrarPad():
        marca = ee.padMarca.text()
        modelo = ee.padModelo.text()
        condicao = ee.padCondicao.text()
        valor = ee.padValor.text()
        descricao = ee.padDescricao.text()
        motivo = ee.BoxPadMotivo.currentText()
        tipo = ee.comboBoxSeletorGeral.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if marca == '' or modelo == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.padMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.padModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxPadMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Pad.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(f"""INSERT INTO MousePad (marca,modelo,condicao,valor,descricao,local,data)
                VALUES ('{marca}','{modelo}','{condicao}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idMousePad) FROM mousepad;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsPad()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Pad.setStyleSheet("rgb(255, 0, 0);")
                ee.label_pad.setText(mensageErro)

    def limparCampsPad():
        ee.padMarca.clear()
        ee.padModelo.clear()
        ee.padCondicao.clear()
        ee.padValor.clear()
        ee.padDescricao.clear()
        ee.label_Pad.clear()
        ee.BoxPadMotivo.setCurrentIndex(0)

    def cancelarCadPad():
        limparCampsPad()
        MainEEstoque.close()

    ee.pushButtonCadastraPad.clicked.connect(cadastrarPad)
    ee.pushButtonCancelarPad.clicked.connect(cancelarCadPad)

    ################################################-- TECLADO --#######################################################
    def cadastrarTeclado():
        marca = ee.TecMarca.text()
        modelo = ee.tecModelo.text()
        condicao = ee.tecCondicao.text()
        tipo = ee.tecBoxTipo.currentText()
        valor = ee.tecValor.text()
        descricao = ee.tecDescricao.text()
        tipo = ee.comboBoxSeletorGeral.currentText()
        motivo = ee.BoxTecMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if marca == '' or modelo == '' or tipo == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.TecMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.tecModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.tecBoxTipo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxTecMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Teclado.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO teclado (marca,modelo,condicao,tipo,valor,descricao,local,data)
                    VALUES ('{marca}','{modelo}','{condicao}','{tipo}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idTeclado) FROM teclado;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsTeclado()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Teclado.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Teclado.setText(mensageErro)

    def limparCampsTeclado():
        ee.TecMarca.clear()
        ee.tecModelo.clear()
        ee.tecCondicao.clear()
        ee.tecValor.clear()
        ee.tecDescricao.clear()
        ee.label_Teclado.clear()
        ee.BoxTecMotivo.setCurrentIndex(0)
        ee.tecBoxTipo.setCurrentIndex(0)

    def cancelarCadTeclado():
        limparCampsTeclado()
        MainEEstoque.close()

    ee.pushButtonCadastraTeclado.clicked.connect(cadastrarTeclado)
    ee.pushButtonCancelarTeclado.clicked.connect(cancelarCadTeclado)

    ################################################-- SUPORTE --#######################################################
    def cadastrarSuporte():
        marca = ee.supMarca.text()
        modelo = ee.supModelo.text()
        condicao = ee.supCondicao.text()
        valor = ee.supValor.text()
        descricao = ee.supDescricao.text()
        motivo = ee.BoxSupMotivo.currentText()
        tipo = ee.comboBoxSeletorGeral.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if marca == '' or modelo == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.supMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.supModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxSupMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Suporte.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Suporte (marca,modelo,condicao,valor,descricao,local, data)
                    VALUES ('{marca}','{modelo}','{condicao}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idSuporte) FROM suporte;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsSuporte()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Suporte.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Suporte.setText(mensageErro)

    def limparCampsSuporte():
        ee.supMarca.clear()
        ee.supModelo.clear()
        ee.supCondicao.clear()
        ee.supDescricao.clear()
        ee.supValor.clear()
        ee.label_Suporte.clear()
        ee.BoxSupMotivo.setCurrentIndex(0)

    def cancelarCadSuporte():
        limparCampsSuporte()
        MainEEstoque.close()

    ee.pushButtonCadastraSuporte.clicked.connect(cadastrarSuporte)
    ee.pushButtonCancelarSuporte.clicked.connect(cancelarCadSuporte)

    #################################################-- EMAIL --########################################################
    def cadastrarEmail():
        empresa = ee.emailEmpresa.text()
        quantidade = ee.emailBoxQuantidade.currentText()
        valor = ee.emailValor.text()
        descricao = ee.emailDescricao.text()
        tipo = ee.comboBoxSeletorGeral.currentText()
        motivo = ee.BoxEmailMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if empresa == '' or quantidade == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.emailEmpresa.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.emailBoxQuantidade.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxEmailMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Email.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Email (empresa,quantidade,valor,descricao,local, data)
                    VALUES ('{empresa}',{quantidade},'{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idEmail) FROM Email;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{empresa}','{empresa}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsEmail()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Email.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Email.setText(mensageErro)

    def limparCampsEmail():
        ee.emailEmpresa.clear()
        ee.emailValor.clear()
        ee.emailDescricao.clear()
        ee.label_Email.clear()
        ee.emailBoxQuantidade.setCurrentIndex(0)
        ee.BoxEmailMotivo.setCurrentIndex(0)

    def cancelarCadEmail():
        limparCampsEmail()
        MainEEstoque.close()

    ee.pushButtonCadastraEmail.clicked.connect(cadastrarEmail)
    ee.pushButtonCancelarEmail.clicked.connect(cancelarCadEmail)

    ################################################-- OFFICE --########################################################
    def cadastrarOffice():
        chave = ee.offChave.text()
        versaoPro = ee.offVersaoPro.text()
        versao = ee.offBoxVersao.currentText()
        valor = ee.offValor.text()
        descricao = ee.offDescricao.text()
        tipo = ee.comboBoxSeletorGeral.currentText()
        motivo = ee.BoxOffMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if chave == '' or versaoPro == '' or versao == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.offChave.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.offVersaoPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.offBoxVersao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxOffMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Office.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Office (chave,versaopro,versao,valor,descricao,local,data)
                    VALUES ('{chave}','{versaoPro}','{versao}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idOffice) FROM office;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(
                f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{versao}','{versaoPro}',
                '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsOffice()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Office.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Office.setText(mensageErro)

    def limparCampsOffice():
        ee.offChave.clear()
        ee.offVersaoPro.clear()
        ee.offValor.clear()
        ee.offDescricao.clear()
        ee.label_Office.clear()
        ee.BoxOffMotivo.setCurrentIndex(0)
        ee.offBoxVersao.setCurrentIndex(0)

    def cancelarCadOffice():
        limparCampsOffice()
        MainEEstoque.close()

    ee.pushButtonCadastraOffice.clicked.connect(cadastrarOffice)
    ee.pushButtonCancelarOffice.clicked.connect(cancelarCadOffice)

    ################################################-- WINDOWS --#######################################################
    def cadastrarWindows():
        chave = ee.wiChave.text()
        versaoPro = ee.wiVersaoPro.text()
        versao = ee.wiBoxVersao.currentText()
        valor = ee.wiValor.text()
        descricao = ee.wiDescricao.text()
        tipo = ee.comboBoxSeletorGeral.currentText()
        motivo = ee.BoxWinMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if chave == '' or versaoPro == '' or versao == '' or motivo =='':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.wiChave.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.wiVersaoPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.wiBoxVersao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxWinMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Windows.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Windows (chave,versaopro,versao,valor,descricao,local,data)
                    VALUES ('{chave}','{versaoPro}','{versao}', '{valor}', '{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idWindows) FROM windows;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(
                    f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{versao}','{versaoPro}',
                    '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsWindows()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Windows.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Windows.setText(mensageErro)

    def limparCampsWindows():
        ee.wiChave.clear()
        ee.wiVersaoPro.clear()
        ee.wiValor.clear()
        ee.wiDescricao.clear()
        ee.label_Windows.clear()
        ee.BoxWinMotivo.setCurrentIndex(0)
        ee.wiBoxVersao.setCurrentIndex(0)

    def cancelarCadWindows():
        limparCampsWindows()
        MainEEstoque.close()

    ee.pushButtonCadastraWindows.clicked.connect(cadastrarWindows)
    ee.pushButtonCancelarWindows.clicked.connect(cancelarCadWindows)

    ################################################-- OUTROS --########################################################
    def cadastrarOutros():
        nome = ee.ouNome.text()
        marca = ee.ouMarca.text()
        modelo = ee.ouModelo.text()
        condicao = ee.ouCondicao.text()
        valor = ee.ouValor.text()
        descricao = ee.ouDescricao.text()
        tipo = ee.comboBoxSeletorGeral.currentText()
        motivo = ee.BoxOutrosMotivo.currentText()
        local = 'ESTOQUE'
        data = date.today()

        if nome == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.ouNome.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.BoxOutrosMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Outro.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(f"""INSERT INTO Outros (nome,marca,modelo,condicao,valor,descricao,local,data)
                    VALUES ('{nome}','{marca}','{modelo}','{condicao}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idOutros) FROM outro;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{nome}','{marca}',
                    '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsOutros()

                mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
                dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
                Dialog.show()
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Outro.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Outro.setText(mensageErro)

    def limparCampsOutros():
        ee.ouMarca.clear()
        ee.ouModelo.clear()
        ee.ouNome.clear()
        ee.ouCondicao.clear()
        ee.ouValor.clear()
        ee.ouDescricao.clear()
        ee.label_Outro.clear()

    def cancelarCadOutros():
        limparCampsOutros()
        MainEEstoque.close()

    ee.pushButtonCadastraOutro.clicked.connect(cadastrarOutros)
    ee.pushButtonCancelarOutro.clicked.connect(cancelarCadOutros)

    # Cadastro de Monitor no banco ======================================================================================
    def cadastrarMonitor():
        marca = mw.MonMarca.text()
        modelo = mw.MonModelo.text()
        condicao = mw.MonCondicao.text()
        tamanho = mw.MonBoxTela.currentText()
        valor = mw.MonValor.text()
        descricao = mw.MonDescricao.text()
        data = date.today()

        if marca == '' or modelo == '' or tamanho == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            mw.MonMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.MonModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.MonBoxTela.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.label_Outro.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO monitor (nome,marca,modelo,condicao,tamanho,valor,descricao,data)
                        VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{valor}','{descricao}','{data}');""")
                cursor.close()
                limparCampsMonitor()

                mensage = 'CADASTRADO COM SUCESSO!'
                mw.label_Mon.setStyleSheet("color: rgb(37, 163, 8);")
                mw.label_Mon.setText(mensage)
                quantiTable()
                carregarDados()

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                mw.label_Mon.setStyleSheet("rgb(255, 0, 0);")
                mw.label_Mon.setText(mensageErro)

    def limparCampsMonitor():
        mw.MonMarca.clear()
        mw.MonModelo.clear()
        mw.MonCondicao.clear()
        mw.MonValor.clear()
        mw.MonDescricao.clear()
        mw.label_Mon.clear()

    def cancelarCadMonitor():
        limparCampsMonitor()

    ee.pushButtonCadastraOutro.clicked.connect(cadastrarMonitor)
    ee.pushButtonCancelarOutro.clicked.connect(cancelarCadMonitor)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    MainEstoque = QtWidgets.QMainWindow()
    MainEEstoque = QtWidgets.QMainWindow()
    Dialog = QtWidgets.QDialog()

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
    estoqueTi(mw, ee)

    sys.exit(app.exec_())
