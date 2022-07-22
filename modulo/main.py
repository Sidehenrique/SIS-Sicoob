from login import *
from estoqueTI import *
from entradaEstoque import *
import db
from datetime import date
import pymysql


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
        print(usuario, password + '<--- entrada do Usuário')

        if usuario == '' or password == '':
            text = 'CAMPOS NÃO PREENCHIDOS'
            mensage(text)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(f"""SELECT password FROM usuarios WHERE user = '{usuario}';""")
                senha_bd = cursor.fetchall()
                print(senha_bd[0][0] + '<--- banco de dados')
                cursor.close()

                if password == senha_bd[0][0]:
                    texto = 'BEM VINDO ' + usuario.upper()
                    mensage(texto)
                    MainLogin.close()
                    MainEstoque.showMaximized()

                else:
                    texto = 'SENHA INCORRETA'
                    mensage(texto)

            except:
                texto = 'NOME DE USUÁRIO INCORRETO'
                mensage(texto)
                return




        # try:
        #     cursor = db.conMySQL()
        #     cursor.execute(f"""SELECT password FROM usuarios WHERE user = '{usuario}';""")
        #     senha_bd = cursor.fetchall()
        #     print(senha_bd[0][0] + '<--- banco de dados')
        #     cursor.close()
        #
        #     if usuario == '' or password == '':
        #         text = 'Campos Não Preenchidos'
        #         mensage(text)
        #
        #     elif password == senha_bd[0][0]:
        #         texto2 = 'Login efetuado com sucesso'
        #         mensage(texto2)
        #         print('Sucesso!!!')
        #         MainLogin.close()
        #         MainEstoque.showMaximized()
        #
        #     else:
        #         texto3 = 'A senha esta incorreta'
        #         mensage(texto3)
        #
        # except pymysql.Error as erro:
        #     texto1 = 'Erro de Servidor' + str(erro)
        #     print(str(erro))
        #     mensage(texto1)
        #     return

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
        imb = ee.notIMB.text()
        marca = ee.notMarca.text().upper()
        modelo = ee.notModelo.text().upper()
        condicao = ee.notCondicao.text().upper()
        anoFab = ee.notAno.text()
        cfg = ee.notBoxCFG.currentText()
        tela = ee.notBoxTela.currentText()
        ssd = ee.notBoxSSD.currentText()
        HDexp = ee.notBoxExp.currentText()
        preco = ee.notPreco.text()
        carregador = ee.notBoxCarregador.currentText()
        processador = ee.notPro.text().upper()
        marcaPro = ee.notMarcaPro.text().upper()
        frequenciaPro = ee.notFrePro.text().upper()
        geracaoPro = ee.notBoxGeracao.currentText()
        ram = ee.notRam.text().upper()
        ddr = ee.notVerRam.text().upper()
        frequenciaMemo = ee.notFreRam.text()
        memoExp = ee.notBoxExpRam.currentText()
        chaveW = ee.notWindows.text().upper()
        chaveO = ee.notOffice.text().upper()
        windows = ee.notBoxWindows.currentText()
        office = ee.notBoxOffice.currentText()
        descricao = ee.notDecricao.text().upper()
        data = date.today()
        serviceTag = ee.notService.text().upper()
        teamViewer = ee.notTeam.text().upper()
        anteVirus = ee.notBoxAntevirus.currentText()
        nomeRede = ee.notRede.text().upper()

        if marca =='' or modelo =='' or serviceTag =='' or nomeRede =='' or carregador =='' or processador =='' or geracaoPro =='' or ram =='' or ddr =='':

            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.notMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notService.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notRede.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notBoxCarregador.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notBoxGeracao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.notVerRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.labelNotebook.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO sisdb.notebook (IMB, MARCA, MODELO, CONDICAO, ANOFAB, CFG, TELA, PRECO, SERVICETAG, TEAMVIEWER,
                    REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO, FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM,
                    LICENCAWINDOWS, LICENCAOFFICE, WINDOWS, OFFICE, ANTEVIRUS, DESCRICAO, DATA) 
                    
                    VALUES ({imb},'{marca}','{modelo}','{condicao}',{anoFab},'{cfg}',{tela},
                    {preco},'{serviceTag}','{teamViewer}','{nomeRede}','{ssd}','{HDexp}','{carregador}',
                    '{processador}','{marcaPro}','{frequenciaPro}','{geracaoPro}',{ram},'{ddr}',{frequenciaMemo},
                    '{anteVirus}','{memoExp}','{chaveW}','{chaveO}','{windows}','{office}','{descricao}','{data}');""")
                cursor.close()

                mensage = 'CADASTRADO COM SUCESSO!'
                limparCampsNote()
                ee.labelNotebook.setStyleSheet("color: rgb(37, 163, 8);")
                ee.labelNotebook.setText(mensage)

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.labelNotebook.setStyleSheet("rgb(255, 0, 0);")
                ee.labelNotebook.setText(mensageErro)

    def limparCampsNote():
        ee.notIMB.clear()
        ee.notMarca.clear()
        ee.notModelo.clear()
        ee.notCondicao.clear()
        ee.notAno.clear()
        ee.notPreco.clear()
        ee.notService.clear()
        ee.notTeam.clear()
        ee.notRede.clear()
        ee.notPro.clear()
        ee.notMarcaPro.clear()
        ee.notFrePro.clear()
        ee.notRam.clear()
        ee.notVerRam.clear()
        ee.notFreRam.clear()
        ee.notWindows.clear()
        ee.notOffice.clear()
        ee.notDecricao.clear()
        ee.labelNotebook.clear()

    def cancelarCadNote():
        limparCampsNote()
        MainEEstoque.close()
    ee.pushButtonCancelarNote.clicked.connect(cancelarCadNote)
    ee.pushButtonSalvarNote.clicked.connect(cadastrarNotebook)

    # Cadastro de celular no banco =====================================================================================
    def cadastrarCelu():
        imei = ee.celMeiOne.text()
        imei2 = ee.celMeiTwo.text()
        marca = ee.celMarca.text()
        modelo = ee.celModelo.text()
        condicao = ee.celEstado.text()
        anofab = ee.celAnoFab.text()
        cor = ee.celCor.text()
        preco = ee.celPreco.text()
        processador = ee.celPro.text()
        modeloPro = ee.celModPro.text()
        frequencia = ee.celFrePro.text()
        ram = ee.celRam.text()
        bateria = ee.celbat.text()
        sistema = ee.notBoxSitema.currentText()
        microSD = ee.celBoxMicro.currentText()
        memoria = ee.celMemo.text()
        dual = ee.celBoxDual.currentText()
        chip1 = ee.celBoxChipOne.currentText()
        chip2 = ee.celBoxChipTwo.currentText()
        numero1 = ee.celNumeroOne.text()
        numero2 = ee.celNumeroTwo.text()
        descricao = ee.celDescricao.text()
        data = date.today()

        if imei =='' or marca =='' or modelo =='' or condicao =='' or cor =='' or ram =='' or memoria =='':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.celMeiOne.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.celMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.celModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.celEstado.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.celCor.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.celRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.celMemo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Celular.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Celular VALUES ({imei},{imei2},'{marca}','{modelo}','{condicao}',{anofab},'{cor}',
                    {preco},'{processador}','{modeloPro}','{frequencia}',{ram},{bateria},'{sistema}',
                    '{microSD}',{memoria},'{dual}','{chip1}','{chip2}',{numero1},{numero2},'{descricao}','{data}');""")
                cursor.close()
                limparCampsCelu()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Celular.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Celular.setText(mensage)

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Celular.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Celular.setText(mensageErro)

    def limparCampsCelu():
        ee.celMeiOne.clear()
        ee.celMeiTwo.clear()
        ee.celMarca.clear()
        ee.celModelo.clear()
        ee.celEstado.clear()
        ee.celAnoFab.clear()
        ee.celCor.clear()
        ee.celPreco.clear()
        ee.celMemo.clear()
        ee.celPro.clear()
        ee.celDescricao.clear()
        ee.celFrePro.clear()
        ee.celRam.clear()
        ee.celbat.clear()
        ee.celNumeroOne.clear()
        ee.celNumeroTwo.clear()
        ee.label_Celular.clear()

    def cancelarCadCelu():
        limparCampsCelu()
        MainEEstoque.close()
    ee.pushButtonCadastraCelular.clicked.connect(cadastrarCelu)
    ee.pushButtonCancelarCelular.clicked.connect(cancelarCadCelu)

    # Cadastro de Memorias no banco ====================================================================================
    def cadastrarMemo():
        marca = ee.meMarca.text()
        modelo = ee.meModelo.text()
        condicao = ee.meCondicao.text()
        tamanho = ee.meBoxTamanho.currentText()
        plataforma = ee.mePlataforma.text()
        valor = ee.meValor.text()
        descricao = ee.meDescricao.text()
        data = date.today()

        if marca == '' or modelo == '' or tamanho == '' or plataforma == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.meMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.meModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.meBoxTamanho.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.mePlataforma.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Memoria.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Memoria VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{plataforma}',{valor}
                    ,'{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Memoria.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Memoria.setText(mensage)

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

    def cancelarCadMemo():
        limparCampsMemo()
        MainEEstoque.close()
    ee.pushButtonCadastraMemo.clicked.connect(cadastrarMemo)
    ee.pushButtonCancelarMemo.clicked.connect(cancelarCadMemo)

    # Cadastro de Disco no banco =======================================================================================
    def cadastrarDisco():
        marca = ee.disMarca.text()
        modelo = ee.disModelo.text()
        condicao = ee.disCondicao.text()
        tamanho = ee.disBoxTamanho.currentText()
        plataforma = ee.disPlataforma.text()
        valor = ee.disValor.text()
        descricao = ee.disDescricao.text()
        data = date.today()

        if marca == '' or tamanho == '' or plataforma == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.disMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.disModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.disBoxTamanho.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.disPlataforma.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Disco.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Disco VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{plataforma}','{valor}'
                    ,'{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Disco.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Disco.setText(mensage)

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Disco.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Disco.setText(mensageErro)

    def limparCampsDisco():
        ee.disMarca.clear()
        ee.disModelo.clear()
        ee.disCondicao.clear()
        ee.disPlataforma.clear()
        ee.disValor.clear()
        ee.disDescricao.clear()
        ee.label_Disco.clear()

    def cancelarCadDisco():
        limparCampsDisco()
        MainEEstoque.close()
    ee.pushButtonCadastraDisco.clicked.connect(cadastrarDisco)
    ee.pushButtonCancelarDisco.clicked.connect(cancelarCadDisco)

    # Cadastro de Mouse no banco =======================================================================================
    def cadastrarMouse():
        marca = ee.moMarca.text()
        modelo = ee.moModelo.text()
        condicao = ee.moCondicao.text()
        tipo = ee.moBoxTipo.currentText()
        valor = ee.moValor.text()
        descricao = ee.moDescricao.text()
        data = date.today()

        if marca == '' or modelo == '' or tipo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.moMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.moModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.moCondicao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.moBoxTipo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Mouse.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Mouse VALUES ('{marca}','{modelo}','{condicao}','{tipo}',{valor},
                    ,'{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Mouse.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Mouse.setText(mensage)

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Mouse.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Mouse.setText(mensageErro)

    def limparCampsMouse():
        ee.moMarca.clear()
        ee.moModelo.clear()
        ee.moCondicao.clear()
        ee.moValor.clear()
        ee.moDescricao.clear()
        ee.label_Mouse.clear()

    def cancelarCadMouse():
        limparCampsMouse()
        MainEEstoque.close()
    ee.pushButtonCadastraMouse.clicked.connect(cadastrarMouse)
    ee.pushButtonCancelarMouse.clicked.connect(cancelarCadMouse)

    # Cadastro de Mouse Pad no banco ===================================================================================
    def cadastrarPad():
        marca = ee.padMarca.text()
        modelo = ee.padModelo.text()
        condicao = ee.padCondicao.text()
        valor = ee.padValor.text()
        descricao = ee.padDescricao.text()
        data = date.today()

        if marca == '' or modelo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.padMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.padModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Pad.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO MousePad VALUES ('{marca}','{modelo}','{condicao}',{valor},
                    ,'{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Pad.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Pad.setText(mensage)

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Pad.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Pad.setText(mensageErro)

    def limparCampsPad():
        ee.padMarca.clear()
        ee.padModelo.clear()
        ee.padCondicao.clear()
        ee.padValor.clear()
        ee.padDescricao.clear()
        ee.label_Pad.clear()

    def cancelarCadPad():
        limparCampsPad()
        MainEEstoque.close()
    ee.pushButtonCadastraPad.clicked.connect(cadastrarPad)
    ee.pushButtonCancelarPad.clicked.connect(cancelarCadPad)

    # Cadastro de Teclado no banco =====================================================================================
    def cadastrarTeclado():
        marca = ee.tecMarca.text()
        modelo = ee.tecModelo.text()
        condicao = ee.tecCondicao.text()
        tipo = ee.tecBoxTipo.currentText()
        valor = ee.tecValor.text()
        descricao = ee.tecDescricao.text()
        data = date.today()

        if marca == '' or modelo == '' or tipo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.tecMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.tecModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.tecBoxTipo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Teclado.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Teclado VALUES ('{marca}','{modelo}','{condicao}','{tipo}', {valor},
                           '{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Teclado.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Teclado.setText(mensage)

            except pymysql.Error as erro:
                print(erro)
                mensageErro = 'O ITEM NÃO FOI CADASTRADO!\n' + str(erro)
                ee.label_Pad.setStyleSheet("rgb(255, 0, 0);")
                ee.label_Pad.setText(mensageErro)

    def limparCampsTeclado():
        ee.tecMarca.clear()
        ee.tecModelo.clear()
        ee.tecCondicao.clear()
        ee.tecValor.clear()
        ee.tecDescricao.clear()
        ee.label_Teclado.clear()

    def cancelarCadTeclado():
        limparCampsTeclado()
        MainEEstoque.close()
    ee.pushButtonCadastraTeclado.clicked.connect(cadastrarTeclado)
    ee.pushButtonCancelarTeclado.clicked.connect(cancelarCadTeclado)

    # Cadastro de Suporte no banco =====================================================================================
    def cadastrarSuporte():
        marca = ee.supMarca.text()
        modelo = ee.supModelo.text()
        condicao = ee.supCondicao.text()
        valor = ee.supValor.text()
        descricao = ee.supDescricao.text()
        data = date.today()

        if marca == '' or modelo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.supMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.supModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Suporte.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Suporte VALUES ('{marca}','{modelo}','{condicao}','{valor}',
                           ,'{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Suporte.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Suporte.setText(mensage)

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

    def cancelarCadSuporte():
        limparCampsSuporte()
        MainEEstoque.close()
    ee.pushButtonCadastraSuporte.clicked.connect(cadastrarSuporte)
    ee.pushButtonCancelarSuporte.clicked.connect(cancelarCadSuporte)

    # Cadastro de Email no banco =======================================================================================
    def cadastrarEmail():
        empresa = ee.emailEmpresa.text()
        quantidade = ee.emailBoxQuantidade.currentText()
        valor = ee.emailValor.text()
        descricao = ee.emailDescricao.text()
        data = date.today()

        if empresa == '' or quantidade == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.emailEmpresa.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.emailBoxQuantidade.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Email.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Email VALUES ('{empresa}',{quantidade},{valor},'{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Email.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Email.setText(mensage)

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

    def cancelarCadEmail():
        limparCampsEmail()
        MainEEstoque.close()
    ee.pushButtonCadastraEmail.clicked.connect(cadastrarEmail)
    ee.pushButtonCancelarEmail.clicked.connect(cancelarCadEmail)

    # Cadastro de Office no banco ======================================================================================
    def cadastrarOffice():
        chave = ee.offChave.text()
        versaoPro = ee.offVersaoPro.text()
        versao = ee.offBoxVersao.currentText()
        valor = ee.offValor.text()
        descricao = ee.offDescricao.text()
        data = date.today()

        if chave == '' or versaoPro == '' or versao == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.offChave.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.offVersaoPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.offBoxVersao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Office.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Office VALUES ('{chave}','{versaoPro}','{versao}', {valor}, '{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Office.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Office.setText(mensage)

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

    def cancelarCadOffice():
        limparCampsOffice()
        MainEEstoque.close()

    ee.pushButtonCadastraOffice.clicked.connect(cadastrarOffice)
    ee.pushButtonCancelarOffice.clicked.connect(cancelarCadOffice)

    # Cadastro de Windows no banco =====================================================================================
    def cadastrarWindows():
        chave = ee.wiChave.text()
        versaoPro = ee.wiVersaoPro.text()
        versao = ee.wiBoxVersao.currentText()
        valor = ee.wiValor.text()
        descricao = ee.wiDescricao.text()
        data = date.today()

        if chave == '' or versaoPro == '' or versao == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            ee.wiChave.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.wiVersaoPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.wiBoxVersao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            ee.label_Windows.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO Windows VALUES ('{chave}','{versaoPro}','{versao}', {valor}, '{descricao}','{data}');""")
                cursor.close()
                limparCampsMemo()

                mensage = 'CADASTRADO COM SUCESSO!'
                ee.label_Windows.setStyleSheet("color: rgb(37, 163, 8);")
                ee.label_Windows.setText(mensage)

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

    def cancelarCadWindows():
        limparCampsWindows()
        MainEEstoque.close()

    ee.pushButtonCadastraWindows.clicked.connect(cadastrarWindows)
    ee.pushButtonCancelarWindows.clicked.connect(cancelarCadWindows)

    # Cadastro de Outros no banco ======================================================================================
    def cadastrarOutros():
        nome = ee.ouNome.text()
        marca = ee.ouMarca.text()
        modelo = ee.ouModelo.text()
        condicao = ee.ouCondicao.text()
        valor = ee.ouValor.text()
        descricao = ee.ouDescricao.text()
        data = date.today()

        try:
            cursor = db.conMySQL()
            cursor.execute(
                f"""INSERT INTO Outros VALUES ('{nome}','{marca}','{modelo}','{condicao}',{valor},'{descricao}','{data}');""")
            cursor.close()
            limparCampsMemo()

            mensage = 'CADASTRADO COM SUCESSO!'
            ee.label_Outro.setStyleSheet("color: rgb(37, 163, 8);")
            ee.label_Outro.setText(mensage)

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
