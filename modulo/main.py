from login import *
from ControleTI import *
from EstoqueTI import *
from entradaEstoque import *
from Dialog import *
from DialogCondicional import *
from Positive import *
from opNote import *
from opDesk import *
from opCell import *
import db
import datetime
import pymysql


########################################################################################################################
        ################################################ LOGIN ################################################

def login(ui):
    MainLogin.setWindowTitle('LOGIN')

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

########################################################################################################################
      ################################################ CONTROLE TI ################################################


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
    def buttonCad():
        mc.stackedWidget.setCurrentWidget(mc.pageCad)

    mc.pushButtonCadastro.clicked.connect(buttonCad)

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

    # TRATAMENTO PAGE NOVO # <<< ------------------------------------------
    def note():
        mc.stackedWidget.setCurrentWidget(mc.pageNotebook)
    mc.buttonNote.clicked.connect(note)

    def desk():
        mc.stackedWidget.setCurrentWidget(mc.pageDesktop)
    mc.buttonDesk.clicked.connect(desk)

    def cell():
        mc.stackedWidget.setCurrentWidget(mc.pageCelular)
    mc.buttonCel.clicked.connect(cell)

    def Monitor():
        mc.stackedWidget.setCurrentWidget(mc.pageMonitor)
    mc.buttonMon.clicked.connect(Monitor)

    def perifericos():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
    mc.buttonPeri.clicked.connect(perifericos)

    def Windows():
        mc.stackedWidget.setCurrentWidget(mc.pageWindows)
    mc.buttonWin.clicked.connect(Windows)

    def Office():
        mc.stackedWidget.setCurrentWidget(mc.pageOffice)
    mc.buttonOff.clicked.connect(Office)

    def Memoria():
        mc.stackedWidget.setCurrentWidget(mc.pageMemoria)
    mc.buttonMemo.clicked.connect(Memoria)

    def disco():
        mc.stackedWidget.setCurrentWidget(mc.pageDisco)
    mc.buttonDisco.clicked.connect(disco)

    def mouse():
        mc.stackedWidget.setCurrentWidget(mc.pageMouse)
    mc.buttonMouse.clicked.connect(mouse)

    def pad():
        mc.stackedWidget.setCurrentWidget(mc.pagePad)
    mc.buttonPad.clicked.connect(pad)

    def teclado():
        mc.stackedWidget.setCurrentWidget(mc.pageTeclado)
    mc.buttonTeclado.clicked.connect(teclado)

    def suport():
        mc.stackedWidget.setCurrentWidget(mc.pageSuporte)
    mc.buttonUporte.clicked.connect(suport)

    def outros():
        mc.stackedWidget.setCurrentWidget(mc.pageOutros)
    mc.buttonOutros.clicked.connect(outros)

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

    # CADASTRO DE ITENS NO BANCO #######################################################################################

    # TRATAMENTO NOTEBOOK # <<< ------------------------------------------
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

        motivo = motiNote()
        tipo = 'Notebook'
        local = mc.notSetorLocal.text()
        data = datAT()
        user = mc.notCodUser.text()
        win = mc.notCodWin.text()
        off = mc.notCodOff.text()

        def trataWin():
            if mc.notCodWin.text() == '------------':
                return 'null'
            else:
                return mc.notCodWin.text()

        def trataOff():
            if mc.notCodOff.text() == '------------':
                return 'null'
            else:
                return mc.notCodOff.text()

        idWindows = trataWin()
        idOffice = trataOff()

        # print(imb, marca, modelo, condicao, ano, preco, service, rede, team, ant, tela, car, pro, marPro, frePro,
        #       gePro, disco, exp, ram, verRam, freRam, expRam, user, win, off, motivo, tipo, local, data)

        if motivo == '' or marca == '' or modelo == '' or service == '' or rede == '' or \
                car == '' or pro == '' or gePro == '' or ram == '' or verRam == '':
            mc.frameMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.notMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notService.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notRede.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notBoxCarregador.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notPro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notBoxGeracao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.notVerRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
            mc.notLabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
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
                        cur.execute(f"""UPDATE colaborador SET idComputer = '{idCon}' WHERE idColaborador = '{user}';""")



                cur.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{idCon}','{marca}',
                '{modelo}','{motivo}','{local}','{data}');""")
                cur.close()

                Positive.show()
                texto = f'{tipo} {idCon} \nCadastrado com Sucesso!'
                po.LabelDialog.setText(texto)

                cleanNote()
                mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def motiNote():

        if mc.notRadioCompra.isChecked() == True:
            compra = mc.notRadioCompra.text()
            return compra

        elif mc.notRadioCadastro.isChecked() == True:
            cadastro = mc.notRadioCadastro.text()
            return cadastro

        elif mc.notRadioProvisorio.isChecked() == True:
            provisorio = mc.notRadioProvisorio.text()
            return provisorio

        elif mc.notRadioOutro.isChecked() == True:
            outros = mc.notRadioOutro.text()
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

    def cleanNote():
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
        mc.frameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.notMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notService.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notRede.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notBoxCarregador.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notPro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notBoxGeracao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.notVerRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

        mc.notFrameWindows.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.notCodWin.setText('------------')
        mc.notVerWin.setText('------------')

        mc.notFrameOffice.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.notCodOff.setText('------------')
        mc.notVerOff.setText('------------')

        mc.notFrameLocal.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.notCodLocal.setText('------------')
        mc.notSetorLocal.setText('------------')

        mc.notFrameUser.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.notCodUser.setText('------------')
        mc.notCarUser.setText('------------')
        mc.notLabelUser.setText('USER')

        mc.notLabelDialog.clear()

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
                            mc.notFrameUser.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mc.notLabelUser.setText(nome)
                            mc.notCarUser.setText(cargo)
                            mc.notCodUser.setText(str(idu))

                            Positive.show()
                            op.notLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opNote.close()

                        else:
                            texto = 'Colaborador Já Possue Notebook\nDeseja Subistituir?'
                            DialogiConditional.show()
                            di.LabelDialogMsg.setText(texto)

                            def sim():
                                mc.notFrameUser.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')
                                mc.notLabelUser.setText(nome)
                                mc.notCarUser.setText(cargo)
                                mc.notCodUser.setText(str(idu))
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
            mc.notFrameLocal.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mc.notSetorLocal.setText(local)
            mc.notCodLocal.setText('01')

            Positive.show()
            op.notLineUser.clear()
            po.LabelDialog.setText(texto)
            opNote.close()

        op.notButtonLocal.clicked.connect(local)

    def cancelNote():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
        cleanNote()

    mc.notButtonCancelar.clicked.connect(cancelNote)
    mc.notButtonLocal.clicked.connect(placeNote)
    mc.notButtonUser.clicked.connect(userNote)
    mc.notButtonWin.clicked.connect(winNote)
    mc.notButtonOff.clicked.connect(offNote)
    mc.notButtonLimpar.clicked.connect(cleanNote)
    mc.notButtonConfirmar.clicked.connect(cadNote)

    # TRATAMENTO DESKTOP # <<< ------------------------------------------
    def cadDesk():
        imb = mc.topIMB.text()
        marca = mc.topMarca.text()
        modelo = mc.topModelo.text()
        condicao = mc.topCondicao.text()
        ano = mc.topAno.text()
        preco = mc.topPreco.text()
        service = mc.topService.text()
        rede = mc.topRede.text()
        team = mc.topTeam.text()
        ant = mc.topBoxAntevirus.currentText()
        monitor = mc.topBoxMonitor.currentText()
        pro = mc.topPro.text()
        marPro = mc.topMarcaPro.text()
        frePro = mc.topFrePro.text()
        gePro = mc.topBoxGeracao.currentText()
        disco = mc.topBoxSSD.currentText()
        exp = mc.topBoxExp.currentText()
        ram = mc.topRam.text()
        verRam = mc.topVerRam.text()
        freRam = mc.topFreRam.text()
        expRam = mc.topBoxExpRam.currentText()

        motivo = motiDesk()
        tipo = 'Desktop'
        local = mc.topSetorLocal.text()
        data = datAT()
        user = mc.topCodUser.text()
        win = mc.topCodWin.text()
        off = mc.topCodOff.text()

        def trataWinTop():
            if mc.topCodWin.text() == '------------':
                return 'null'
            else:
                return mc.notCodWin.text()

        def trataOffTop():
            if mc.topCodOff.text() == '------------':
                return 'null'
            else:
                return mc.notCodOff.text()

        idWindows = trataWinTop()
        idOffice = trataOffTop()

        print(imb, marca, modelo, condicao, ano, preco, service, rede, team, ant, monitor, pro, marPro, frePro,
              gePro, disco, exp, ram, verRam, freRam, expRam, user, win, off, motivo, tipo, local, data)

        if motivo == '' or marca == '' or modelo == '' or service == '' or rede == '' or \
                pro == '' or gePro == '' or ram == '' or verRam == '':

            mc.frameMotivo_2.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.topMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topService.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topRede.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topPro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topBoxGeracao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.topVerRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
            mc.topLabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
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
                mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def motiDesk():

        if mc.topRadioCompra.isChecked() == True:
            compra = mc.topRadioCompra.text()
            return compra

        elif mc.topRadioCadastro.isChecked() == True:
            cadastro = mc.topRadioCadastro.text()
            return cadastro

        elif mc.topRadioProvisorio.isChecked() == True:
            provisorio = mc.topRadioProvisorio.text()
            return provisorio

        elif mc.topRadioOutro.isChecked() == True:
            outros = mc.topRadioOutro.text()
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
                                    mc.topFrameWindows.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                    mc.topVerWin.setText(versao)
                                    mc.topCodWin.setText(str(id))

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
                                    mc.topFrameOffice.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                                    mc.topVerOff.setText(versao)
                                    mc.topCodOff.setText(str(id))

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
        mc.topIMB.clear()
        mc.topMarca.clear()
        mc.topModelo.clear()
        mc.topCondicao.clear()
        mc.topAno.clear()
        mc.topPreco.clear()
        mc.topService.clear()
        mc.topRede.clear()
        mc.topTeam.clear()
        mc.topBoxAntevirus.setCurrentIndex(0)
        mc.topBoxMonitor.setCurrentIndex(0)
        mc.topPro.clear()
        mc.topMarcaPro.clear()
        mc.topFrePro.clear()
        mc.topBoxGeracao.setCurrentIndex(0)
        mc.topBoxSSD.setCurrentIndex(0)
        mc.topBoxExp.setCurrentIndex(0)
        mc.topRam.clear()
        mc.topVerRam.clear()
        mc.topFreRam.clear()
        mc.topBoxExpRam.setCurrentIndex(0)
        mc.frameMotivo_2.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.topMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topService.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topRede.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topPro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topBoxGeracao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.topVerRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

        mc.topFrameWindows.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.topCodWin.setText('------------')
        mc.topVerWin.setText('------------')

        mc.topFrameOffice.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.topCodOff.setText('------------')
        mc.topVerOff.setText('------------')

        mc.topFrameLocal.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.topCodLocal.setText('------------')
        mc.topSetorLocal.setText('------------')

        mc.topFrameUser.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.topCodUser.setText('------------')
        mc.topCarUser.setText('------------')
        mc.topLabelUser.setText('USER')

        mc.topLabelDialog.clear()

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
                            mc.topFrameUser.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mc.topLabelUser.setText(nome)
                            mc.topCarUser.setText(cargo)
                            mc.topCodUser.setText(str(idu))

                            Positive.show()
                            opd.topLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opDesk.close()

                        else:
                            texto = 'Colaborador Já Possue Notebook\nDeseja Subistituir?'
                            DialogiConditional.show()
                            di.LabelDialogMsg.setText(texto)

                            def simDesk():
                                mc.topFrameUser.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')
                                mc.topLabelUser.setText(nome)
                                mc.topCarUser.setText(cargo)
                                mc.topCodUser.setText(str(idu))
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
            mc.topFrameLocal.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mc.topSetorLocal.setText(local)
            mc.topCodLocal.setText('01')

            Positive.show()
            opd.topLineUser.clear()
            po.LabelDialog.setText(texto)
            opDesk.close()

        opd.topButtonLocal.clicked.connect(local)

    def cancelDesk():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
        cleanNote()

    mc.topButtonCancelar.clicked.connect(cancelDesk)
    mc.topButtonLocal.clicked.connect(placeDesk)
    mc.topButtonUser.clicked.connect(userDesk)
    mc.topButtonWin.clicked.connect(winDesk)
    mc.topButtonOff.clicked.connect(offDesk)
    mc.topButtonLimpar.clicked.connect(cleanDesk)
    mc.topButtonConfirmar.clicked.connect(cadDesk)

    # TRATAMENTO CELULAR # <<< ------------------------------------------
    def cadCell():
        marca = mc.celMarca.text()
        modelo = mc.celModelo.text()
        condicao = mc.celEstado.text()
        ano = mc.celAnoFab.text()
        cor = mc.celCor.text()
        preco = mc.celPreco.text()
        pro = mc.celPro.text()
        modPro = mc.celModPro.text()
        frePro = mc.celFrePro.text()
        ram = mc.celRam.text()
        bateria = mc.celbat.text()
        sistema = mc.celBoxSistema.currentText()
        micro = mc.celBoxMicro.currentText()
        memo = mc.celMemo.text()
        dual = mc.celBoxDual.currentText()
        chipOne = mc.celBoxChipOne.currentText()
        numOne = mc.celNumeroOne.text()
        chipTwe = mc.celBoxChipTwo.currentText()
        numTwe = mc.celNumeroTwo.text()

        motivo = motiCell()
        email = mc.celEndEmail.text()
        tipo = 'Celular'
        local = mc.celSetorLocal.text()

        data = datAT()

        user = mc.celCodUser.text()
        imeiOne = mc.celImeiOne.text()
        imeiTwo = mc.celImeiTwe.text()

        # print(marca, modelo, condicao, ano, preco, ano, cor, pro, modPro, frePro, ram, bateria, sistema, micro, memo,
        #         dual, chipOne, numOne, chipTwe, numTwe,  user, imeiOne, imeiTwo, motivo, tipo, local, data)

        if marca == '' or modelo == '' or cor == '' or pro == '' or frePro == '' or ram == '' or memo == '':

            mc.frameMotivo_3.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.celMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.celModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.celCor.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.celPro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.celFrePro.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.celRam.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.celMemo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mensage = 'Favor verifique se todos os campos obrigatórios foram preenchidos'
            mc.celLabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO celular (IMEI, IMEI2, MARCA, MODELO, CONDICAO, ANOFAB, COR, PRECO,
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
                mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def motiCell():

        if mc.celRadioCompra.isChecked() == True:
            compra = mc.celRadioCompra.text()
            return compra

        elif mc.celRadioCadastro.isChecked() == True:
            cadastro = mc.celRadioCadastro.text()
            return cadastro

        elif mc.celRadioProvisorio.isChecked() == True:
            provisorio = mc.celRadioProvisorio.text()
            return provisorio

        elif mc.celRadioOutro.isChecked() == True:
            outros = mc.celRadioOutro.text()
            return outros

        else:
            return 'Motivo Não Selecionado'

    def cleanCell():
        mc.celMarca.clear()
        mc.celModelo.clear()
        mc.celEstado.clear()
        mc.celAnoFab.clear()
        mc.celCor.clear()
        mc.celPreco.clear()
        mc.celPro.clear()
        mc.celModPro.clear()
        mc.celFrePro.clear()
        mc.celRam.clear()
        mc.celbat.clear()
        mc.celBoxSistema.setCurrentIndex(0)
        mc.celBoxMicro.setCurrentIndex(0)
        mc.celMemo.clear()
        mc.celBoxDual.setCurrentIndex(0)
        mc.celNumeroOne.clear()
        mc.celNumeroTwo.clear()
        mc.celBoxChipOne.setCurrentIndex(0)
        mc.celBoxChipTwo.setCurrentIndex(0)

        mc.frameMotivo_3.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')

        mc.celMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.celModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.celCor.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.celPro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.celFrePro.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.celRam.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.celMemo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

        mc.celFrameImei.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.celImeiOne.setText('------------')
        mc.celImeiTwe.setText('------------')

        mc.celFrameEmail.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.celEndEmail.setText('------------')
        mc.celCodEmail.setText('------------')

        mc.celFrameLocal.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.celCodLocal.setText('------------')
        mc.celSetorLocal.setText('------------')

        mc.celFrameUser.setStyleSheet('background-color: rgb(7, 183, 168); border: 1px; border-radius: 10px;')
        mc.celCodUser.setText('------------')
        mc.celCarUser.setText('------------')
        mc.celLabelUser.setText('USER')

        mc.celLabelDialog.clear()

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
                            mc.celFrameUser.setStyleSheet(
                                'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                            mc.celLabelUser.setText(nome)
                            mc.celCarUser.setText(cargo)
                            mc.celCodUser.setText(str(idu))

                            Positive.show()
                            opc.opLineUser.clear()
                            po.LabelDialog.setText(texto)
                            opCell.close()

                        else:
                            texto = 'Colaborador Já Possue Notebook\nDeseja Subistituir?'
                            DialogiConditional.show()
                            di.LabelDialogMsg.setText(texto)

                            def simCell():
                                mc.celFrameUser.setStyleSheet(
                                    'background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')
                                mc.celLabelUser.setText(nome)
                                mc.celCarUser.setText(cargo)
                                mc.celCodUser.setText(str(idu))
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
            mc.celFrameLocal.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mc.celSetorLocal.setText(local)
            mc.celCodLocal.setText('01')

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
                mc.celFrameImei.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

                mc.celImeiOne.setText(imeiOne)
                mc.celImeiTwe.setText(imeiTwe)

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
            mc.celFrameEmail.setStyleSheet('background-color: rgb(199, 211, 0); border: 1px; border-radius: 10px;')

            mc.celEndEmail.setText(email)
            mc.celCodEmail.setText('01')

            Positive.show()
            po.LabelDialog.setText(texto)
            opCell.close()

        opc.opButtonEmail.clicked.connect(regEmail)

    def cancelCell():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
        cleanCell()

    mc.celButtonCancelar.clicked.connect(cancelCell)
    mc.celButtonLocal.clicked.connect(placeCell)
    mc.celButtonUser.clicked.connect(userCell)
    mc.celButtonImei.clicked.connect(imei)
    mc.celButtonEmail.clicked.connect(email)
    mc.celButtonLimpar.clicked.connect(cleanCell)
    mc.celButtonConfirmar.clicked.connect(cadCell)

    # TRATAMENTO MONITOR # <<< ------------------------------------------

    def cadMonitor():
        modelo = mc.moModelo.text()
        marca = mc.moMarca.text()
        condicao = mc.moCondicao.text()
        valor = mc.moValor.text()
        tamanho = mc.moBoxTamanho.currentText()

        motivo = motivoMonitor()
        tipo = 'Monitor'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tamanho == '' or motivo == None:

            mc.moFrameMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.moModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.moMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.moBoxTamanho.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)

            except pymysql.Error as erro:
                print(str(erro))

    def clearMonitor():
        mc.moMarca.clear()
        mc.moModelo.clear()
        mc.moCondicao.clear()
        mc.moValor.clear()
        mc.moBoxTamanho.setCurrentIndex(0)

        mc.moFrameMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.moModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.moMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.moBoxTamanho.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoMonitor():
        if mc.moRadioCompra.isChecked() == True:
            compra = mc.moRadioCompra.text()
            return compra

        elif mc.moRadioCadastro.isChecked() == True:
            cadastro = mc.moRadioCadastro.text()
            return cadastro

        elif mc.moRadioProvisorio.isChecked() == True:
            provisorio = mc.moRadioProvisorio.text()
            return provisorio

        elif mc.moRadioOutros.isChecked() == True:
            outros = mc.moRadioOutros.text()
            return outros

    def cancelMonitor():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
        clearMonitor()

    mc.moButtonConfirmar.clicked.connect(cadMonitor)
    mc.moButtonCancelar.clicked.connect(cancelMonitor)
    mc.moButtonLimpar.clicked.connect(clearMonitor)

    # TRATAMENTO WINDOWS # <<< ------------------------------------------

    def cadWindows():
        chave = mc.winCod.text().upper()
        verPro = mc.winVersao.text()
        valor = mc.winValor.text()
        versao = mc.winBoxVersao.currentText()

        motivo = motivoWin()
        tipo = 'windows'
        local = 'ESTOQUE'
        data = datAT()

        if chave == '' or verPro == '' or versao == '' or motivo == None:

            mc.winMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.winVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.winBoxVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.winCod.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)

            except pymysql.Error as erro:
                trat = str(erro)
                print(trat)
                codigo = trat[1:5]

                if trat.count('1062'):
                    texto = f'CHAVE INFORMADA JÁ CADASTRADA\n CODIGO MYSQL{codigo}'
                    Dialog.show()
                    dg.LabelDialog.setText(texto)

    def clearWin():
        mc.winCod.clear()
        mc.winVersao.clear()
        mc.winValor.clear()
        mc.winBoxVersao.setCurrentIndex(0)

        mc.winMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.winVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.winBoxVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.winCod.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoWin():
        if mc.winRadioCompra.isChecked() == True:
            compra = mc.winRadioCompra.text()
            return compra

        elif mc.winRadioCadastro.isChecked() == True:
            cadastro = mc.winRadioCadastro.text()
            return cadastro

        elif mc.winRadioProvisorio.isChecked() == True:
            provisorio = mc.winRadioProvisorio.text()
            return provisorio

        elif mc.winRadioOutro.isChecked() == True:
            outros = mc.winRadioOutro.text()
            return outros

    def cancelWin():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
        clearWin()

    mc.winButtonConfirmar.clicked.connect(cadWindows)
    mc.winButtonCancelar.clicked.connect(cancelWin)
    mc.winButtonLimpar.clicked.connect(clearWin)

    # TRATAMENTO OFFICE # <<< ------------------------------------------

    def cadOffice():
        chave = mc.offCod.text().upper()
        verPro = mc.offVersao.text()
        valor = mc.offValor.text()
        versao = mc.offBoxVersao.currentText()

        motivo = motivoOff()
        tipo = 'Office'
        local = 'ESTOQUE'
        data = datAT()

        if chave == '' or verPro == '' or versao == '' or motivo == None:

            mc.offMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.offVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.offBoxVersao.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.offCod.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)

            except pymysql.Error as erro:
                trat = str(erro)
                print(trat)
                codigo = trat[1:5]

                if trat.count('1062'):
                    texto = f'CHAVE INFORMADA JÁ CADASTRADA\n CODIGO MYSQL{codigo}'
                    Dialog.show()
                    dg.LabelDialog.setText(texto)

    def clearOff():
        mc.offCod.clear()
        mc.offVersao.clear()
        mc.offValor.clear()
        mc.offBoxVersao.setCurrentIndex(0)

        mc.offMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.offVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.offBoxVersao.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.offCod.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoOff():
        if mc.offRadioCompra.isChecked() == True:
            compra = mc.offRadioCompra.text()
            return compra

        elif mc.offRadioCadastro.isChecked() == True:
            cadastro = mc.offRadioCadastro.text()
            return cadastro

        elif mc.offRadioProvisorio.isChecked() == True:
            provisorio = mc.offRadioProvisorio.text()
            return provisorio

        elif mc.offRadioOutro.isChecked() == True:
            outros = mc.offRadioOutro.text()
            return outros

    def cancelOff():
        mc.stackedWidget.setCurrentWidget(mc.pageNovoCad)
        clearOff()

    mc.offButtonConfirmar.clicked.connect(cadOffice)
    mc.offButtonCancelar.clicked.connect(cancelOff)
    mc.offButtonLimpar.clicked.connect(clearOff)

    # TRATAMENTO MEMORIA # <<< ------------------------------------------

    def cadMemoria():
        modelo = mc.meBarramento.text()
        marca = mc.meMarca.text()
        condicao = mc.meCondicao.text()
        valor = mc.meValor.text()
        tamanho = mc.meBoxTamanho.currentText()
        plataforma = mc.meBoxPlataforma.currentText()

        motivo = motivoMemo()
        tipo = 'Memoria'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tamanho == '' or motivo == None or plataforma == '':

            mc.meMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.meBarramento.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.meMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.meBoxTamanho.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.meBoxPlataforma.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearMemo():
        mc.meMarca.clear()
        mc.meBarramento.clear()
        mc.meCondicao.clear()
        mc.meBoxTamanho.setCurrentIndex(0)
        mc.meBoxPlataforma.setCurrentIndex(0)
        mc.meValor.clear()

        mc.meMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.meBarramento.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.meMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.meBoxTamanho.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.meBoxPlataforma.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoMemo():
        if mc.meRadioCompra.isChecked() == True:
            compra = mc.meRadioCompra.text()
            return compra

        elif mc.meRadioCadastro.isChecked() == True:
            cadastro = mc.meRadioCadastro.text()
            return cadastro

        elif mc.meRadioProvisorio.isChecked() == True:
            provisorio = mc.meRadioProvisorio.text()
            return provisorio

        elif mc.meRadioOutro.isChecked() == True:
            outros = mc.meRadioOutro.text()
            return outros

    def cancelMemo():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearMemo()

    mc.meButtonConfirmar.clicked.connect(cadMemoria)
    mc.meButtonCancelar.clicked.connect(cancelMemo)
    mc.meButtonLimpar.clicked.connect(clearMemo)

    # TRATAMENTO DISCO # <<< ------------------------------------------

    def cadDisco():
        modelo = mc.disModelo.text()
        marca = mc.disMarca.text()
        condicao = mc.disCondicao.text()
        valor = mc.disValor.text()
        tamanho = mc.disBoxTamanho.currentText()
        tipo = mc.disBoxTipo.currentText()

        motivo = motivoDis()

        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tamanho == '' or motivo == None or tipo == '':

            mc.disMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.disModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.disMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.disBoxTamanho.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.disBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearDis():
        mc.disMarca.clear()
        mc.disModelo.clear()
        mc.disCondicao.clear()
        mc.disBoxTamanho.setCurrentIndex(0)
        mc.disBoxTipo.setCurrentIndex(0)
        mc.disValor.clear()

        mc.disMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.disModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.disMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.disBoxTamanho.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.disBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoDis():
        if mc.disRadioCompra.isChecked() == True:
            compra = mc.disRadioCompra.text()
            return compra

        elif mc.disRadioCadastro.isChecked() == True:
            cadastro = mc.disRadioCadastro.text()
            return cadastro

        elif mc.disRadioProvisorio.isChecked() == True:
            provisorio = mc.disRadioProvisorio.text()
            return provisorio

        elif mc.disRadioOutro.isChecked() == True:
            outros = mc.disRadioOutro.text()
            return outros

    def cancelDis():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearDis()

    mc.disButtonConfirmar.clicked.connect(cadDisco)
    mc.disButtonCancelar.clicked.connect(cancelDis)
    mc.disButtonLimpar.clicked.connect(clearDis)

    # TRATAMENTO MOUSE # <<< ------------------------------------------

    def cadMouse():
        modelo = mc.mouModelo.text()
        marca = mc.mouMarca.text()
        condicao = mc.mouCondicao.text()
        valor = mc.mouValor.text()
        tipo = mc.mouBoxTipo.currentText()

        motivo = motivoMou()
        tipo = 'MOUSE: ' + tipo
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or motivo == None or tipo == '':

            mc.mouMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.mouModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.mouMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.mouBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearMou():
        mc.mouMarca.clear()
        mc.mouModelo.clear()
        mc.mouCondicao.clear()
        mc.mouBoxTipo.setCurrentIndex(0)
        mc.mouValor.clear()

        mc.mouMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.mouModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.mouMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.mouBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoMou():
        if mc.mouRadioCompra.isChecked() == True:
            compra = mc.mouRadioCompra.text()
            return compra

        elif mc.mouRadioCadastro.isChecked() == True:
            cadastro = mc.mouRadioCadastro.text()
            return cadastro

        elif mc.mouRadioProvisorio.isChecked() == True:
            provisorio = mc.mouRadioProvisorio.text()
            return provisorio

        elif mc.mouRadioOutro.isChecked() == True:
            outros = mc.mouRadioOutro.text()
            return outros

    def cancelMou():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearMou()

    mc.mouButtonConfirmar.clicked.connect(cadMouse)
    mc.mouButtonCancelar.clicked.connect(cancelMou)
    mc.mouButtonLimpar.clicked.connect(clearMou)

    # TRATAMENTO OUTROS # <<< ------------------------------------------

    def cadOutros():
        nome = mc.ouNome.text()
        modelo = mc.ouModelo.text()
        marca = mc.ouMarca.text()
        condicao = mc.ouCondicao.text()
        valor = mc.ouValor.text()

        motivo = motivoOutros()
        tipo = 'Outros'
        local = 'ESTOQUE'
        data = datAT()

        if nome == '' or motivo == None:

            mc.ouMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.ouNome.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearOutros():
        mc.ouNome.clear()
        mc.ouMarca.clear()
        mc.ouModelo.clear()
        mc.ouCondicao.clear()
        mc.ouValor.clear()

        mc.ouMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.ouNome.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoOutros():
        if mc.ouRadioCompra.isChecked() == True:
            compra = mc.ouRadioCompra.text()
            return compra

        elif mc.ouRadioCadastro.isChecked() == True:
            cadastro = mc.ouRadioCadastro.text()
            return cadastro

        elif mc.ouRadioProvisorio.isChecked() == True:
            provisorio = mc.ouRadioProvisorio.text()
            return provisorio

        elif mc.ouRadioOutro.isChecked() == True:
            outros = mc.ouRadioOutro.text()
            return outros

    def cancelOutros():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearOutros()

    mc.ouButtonConfirmar.clicked.connect(cadOutros)
    mc.ouButtonCancelar.clicked.connect(cancelOutros)
    mc.ouButtonLimpar.clicked.connect(clearOutros)

    # TRATAMENTO PAD # <<< ------------------------------------------

    def cadPad():
        modelo = mc.padModelo.text()
        marca = mc.padMarca.text()
        condicao = mc.padCondicao.text()
        valor = mc.padPreco.text()

        motivo = motivoPad()
        tipo = 'Mouse Pad'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or motivo == None:

            mc.padMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.padMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.padModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearPad():
        mc.padMarca.clear()
        mc.padModelo.clear()
        mc.padCondicao.clear()
        mc.padPreco.clear()

        mc.padMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.padMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.padModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoPad():
        if mc.padRadioCompra.isChecked() == True:
            compra = mc.padRadioCompra.text()
            return compra

        elif mc.padRadioCadastro.isChecked() == True:
            cadastro = mc.padRadioCadastro.text()
            return cadastro

        elif mc.padRadioProvisorio.isChecked() == True:
            provisorio = mc.padRadioProvisorio.text()
            return provisorio

        elif mc.padRadioOutro.isChecked() == True:
            outros = mc.padRadioOutro.text()
            return outros

    def cancelPad():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearPad()

    mc.padButtonConfirmar.clicked.connect(cadPad)
    mc.padButtonCancelar.clicked.connect(cancelPad)
    mc.padButtonLimpar.clicked.connect(clearPad)

    # TRATAMENTO PAD # <<< ------------------------------------------

    def cadTeclado():
        modelo = mc.telModelo.text()
        marca = mc.telMarca.text()
        condicao = mc.telCondicao.text()
        valor = mc.telValor.text()
        tipo = mc.telBoxTipo.currentText()

        motivo = motivoTec()
        tipo = 'Teclado: ' + tipo
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or tipo == '' or motivo == None:

            mc.telMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.telMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.telModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.telBoxTipo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearTec():
        mc.telMarca.clear()
        mc.telModelo.clear()
        mc.telCondicao.clear()
        mc.telValor.clear()

        mc.telMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.telMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.telModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.telBoxTipo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoTec():
        if mc.telRadioCompra.isChecked() == True:
            compra = mc.telRadioCompra.text()
            return compra

        elif mc.telRadioCadastro.isChecked() == True:
            cadastro = mc.telRadioCadastro.text()
            return cadastro

        elif mc.telRadioProvisorio.isChecked() == True:
            provisorio = mc.telRadioProvisorio.text()
            return provisorio

        elif mc.telRadioOutro.isChecked() == True:
            outros = mc.telRadioOutro.text()
            return outros

    def cancelTec():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearTec()

    mc.telButtonConfirmar.clicked.connect(cadTeclado)
    mc.telButtonCancelar.clicked.connect(cancelTec)
    mc.telButtonLimpar.clicked.connect(clearTec)

    # TRATAMENTO SUPORTE # <<< ------------------------------------------

    def cadSuport():
        modelo = mc.supModelo.text()
        marca = mc.supMarca.text()
        condicao = mc.supCondicao.text()
        valor = mc.supValor.text()

        motivo = motivoSup()
        tipo = 'Suporte'
        local = 'ESTOQUE'
        data = datAT()

        if marca == '' or modelo == '' or motivo == None:

            mc.supMotivo.setStyleSheet('border: 2px solid;border-color: rgb(243, 76, 79);border-radius: 10px;')
            mc.supMarca.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')
            mc.supModelo.setStyleSheet('background-color: rgb(255, 192, 193); border: 1px; border-radius: 5px')


            mensage = 'Campos Obrigatórios\nNão preenchidos'
            Dialog.show()
            dg.LabelDialog.setText(mensage)

        else:
            try:
                cur = db.conMySQL()
                cur.execute(
                    f"""INSERT INTO suporte (MARCA, MODELO, CONDICAO, TIPO, VALOR, LOCAL, DATA)
                                       VALUES ('{marca}','{modelo}','{condicao}','{valor}','{local}','{data}');""")

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
                mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)

            except pymysql.Error as erro:
                print(str(erro))

    def clearSup():
        mc.supMarca.clear()
        mc.supModelo.clear()
        mc.supCondicao.clear()
        mc.supValor.clear()

        mc.supMotivo.setStyleSheet('border: 2px solid; border-color: rgb(255, 255, 255);border-radius: 5px;')
        mc.supMarca.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')
        mc.supModelo.setStyleSheet('background-color: rgb(255, 255, 255); border: 1px; border-radius: 5px')

    def motivoSup():
        if mc.supRadioCompra.isChecked() == True:
            compra = mc.supRadioCompra.text()
            return compra

        elif mc.supRadioCadastro.isChecked() == True:
            cadastro = mc.supRadioCadastro.text()
            return cadastro

        elif mc.supRadioProvisorio.isChecked() == True:
            provisorio = mc.supRadioProvisorio.text()
            return provisorio

        elif mc.supRadioOutro.isChecked() == True:
            outros = mc.supRadioOutro.text()
            return outros

    def cancelSup():
        mc.stackedWidget.setCurrentWidget(mc.pagePerifericos)
        clearSup()

    mc.supButtonConfirmar.clicked.connect(cadSuport)
    mc.supButtonCancelar.clicked.connect(cancelSup)
    mc.supButtonLimpar.clicked.connect(clearSup)

########################################################################################################################
      ################################################ ESTOQUE TI ###############################################


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

    def ButtonControleTI():
        MainEstoque.close()
        MainControle.showMaximized()
        mc.stackedWidget.setCurrentWidget(mc.pageHome)
    mw.pushButtonControle.clicked.connect(ButtonControleTI)

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

    # def ButtonNovo():
    #     mw.stackedWidget.setCurrentWidget(mw.pageModulos)
    #     mw.stackedWidgetMenu.setCurrentWidget(mw.pageNovo)
    #     mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
    #     print('click')
    #
    # mw.pushButtonNovo.clicked.connect(ButtonNovo)
    #
    # def ButtonEntrada():
    #     mw.stackedWidget.setCurrentWidget(mw.pageModulos)
    #     mw.stackedWidgetMenu.setCurrentWidget(mw.pageEntrada)
    #     print('click')
    #
    # mw.pushButtonEntrada.clicked.connect(ButtonEntrada)
    #
    # def ButtonSaida():
    #     mw.stackedWidget.setCurrentWidget(mw.pageModulos)
    #     mw.stackedWidgetMenu.setCurrentWidget(mw.pageSaida)
    #     mw.stackedWidgetSaida.setCurrentWidget(mw.pagSaida)
    #     print('click')
    #
    # mw.pushButtonSaida.clicked.connect(ButtonSaida)

    #  Acionamento Botões PAGE NOVO-----------------------------------------------------------------------------------
    # def ButtonNote():
    #     mw.stackedWidgetNovo.setCurrentWidget(mw.pageNovoNote)
    #
    # mw.pushNote.clicked.connect(ButtonNote)
    #
    # def ButtonCelu():
    #     mw.stackedWidgetNovo.setCurrentWidget(mw.pageNovoCelu)
    #
    # mw.pushCelular.clicked.connect(ButtonCelu)
    #
    # def ButtonPeri():
    #     MainEEstoque.show()
    #
    # mw.pushPerifericos.clicked.connect(ButtonPeri)
    #
    # def ButtonMon():
    #     mw.stackedWidgetNovo.setCurrentWidget(mw.pageNovoMonitor)
    #
    # mw.pushMonitor.clicked.connect(ButtonMon)


    ##  pré visualização de quantidade ----------------------------------------------------------------------------------

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

        cursor.execute(f"""SELECT * FROM monitor;""")
        monitor = len(cursor.fetchall())
        mw.labelEmail.setText(str(monitor))
        mw.labelTotalEmail.setText(str(monitor))

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
    mw.ButtonEmail.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.pageMonitor))
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

        con.execute("""SELECT * FROM monitor""")
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

        con.execute("""select * from historico order by data desc LIMIT 20;""")
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

    # BOTÕES DE PESQUISA -----------------------------------------------------------------------------------------------
    def pesOffice():
        pesquisa = mw.officePes.text()

        con = db.conMySQL()
        con.execute(f"""SELECT * FROM office WHERE chave like '%{pesquisa}%';""")
        result = con.fetchall()

        mw.tableWidgetOffice.clearContents()
        header = mw.tableWidgetOffice.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        mw.tableWidgetOffice.setRowCount(len(result))  # <---------- Numeros de linhas conforme quantidade da tabela

        for row, text in enumerate(result):
            for column, data in enumerate(text):
                mw.tableWidgetOffice.setItem(row, column, QtWidgets.QTableWidgetItem(str(data)))

    mw.officePesButton.clicked.connect(pesOffice)



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

    MainControle = QtWidgets.QMainWindow()
    mc = Ui_MainControle()
    mc.setupUi(MainControle)

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
    sys.exit(app.exec_())
