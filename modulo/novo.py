

    #################################################-- BASE --#########################################################
    #################################################-- DADOS --########################################################
    ''' ================================ Cadastro de Items do estoque no banco ======================================'''

    # mudar o comboBox seletor dos items de cadastro
    ee.stackedWidgetCadastro.setCurrentIndex(0)
    ee.comboBoxSeletorGeral.activated['int'].connect(ee.stackedWidgetCadastro.setCurrentIndex)
    QtCore.QMetaObject.connectSlotsByName(MainEEstoque)

    ################################################--NOTEBOOK--########################################################
    def cadastrarNote():
        motivo = mw.notBoxMotivo.currentText()
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

        data = date.today()
        serviceTag = mw.notService.text().upper()
        teamViewer = mw.notTeam.text().upper()
        anteVirus = mw.notBoxAntevirus.currentText()
        nomeRede = mw.notRede.text().upper()
        tipo = 'NOTEBOOK'
        local = mw.notBoxLocal.currentText()
        windows = mw.notWindows.text().upper()
        office = mw.notOffice.text().upper()

        idWindows = mw.labelViewerWin.text().upper()
        idOffice = mw.labelViwerOff.text().upper()

        '''Essa condicional é responsavel por verificar e tratar se tiver campos obrigatoris vazios'''
        if motivo == '' or marca == '' or modelo == '' or serviceTag == '' or nomeRede == '' or \
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
                   ANTEVIRUS, LOCAL, DATA, idWindows, idOffice)

                   VALUES ('{imb}','{marca}','{modelo}','{condicao}','{anoFab}','{tela}','{preco}',
                   '{serviceTag}','{teamViewer}','{nomeRede}','{disco}','{DiscoExp}','{carregador}',
                   '{processador}','{marcaPro}','{frePro}','{geracaoPro}','{ram}','{ramMod}','{freRam}',
                   '{ramExp}','{windows}','{office}','{anteVirus}','{local}','{data}','{idWindows}','{idOffice}');""")

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
        mw.BoxNoteMotivo.setCurrentIndex(0)
        mw.BoxNoteItem.setCurrentIndex(0)
        mw.notBoxAntevirus.setCurrentIndex(0)
        mw.notBoxTela.setCurrentIndex(0)
        mw.notBoxCarregador.setCurrentIndex(0)
        mw.notBoxGeracao.setCurrentIndex(0)
        mw.notBoxSSD.setCurrentIndex(0)
        mw.notBoxExpRam.setCurrentIndex(0)
        mw.notBoxExp.setCurrentIndex(0)

    def cancelarCadNote():
        limparCampsNote()
        mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)

    mw.limWindows.clicked.connect(limWin)
    mw.limOffice.clicked.connect(limOff)
    mw.PesWindows.clicked.connect(verWin)
    mw.PesOffice.clicked.connect(verOff)
    mw.pushButtonCancelarNote.clicked.connect(cancelarCadNote)
    mw.pushButtonSalvarNote.clicked.connect(cadastrarNote)

    ################################################--DESKTOP--########################################################
    # def cadastrarTop():
    #     motivo = mw.topBoxMotivo.currentText()
    #     imb = mw.topIMB.text()
    #     marca = mw.topMarca.text().upper()
    #     modelo = mw.topModelo.text().upper()
    #     condicao = mw.topCondicao.text().upper()
    #     anoFab = mw.topAno.text()
    #     disco = mw.topBoxSSD.currentText()
    #     DiscoExp = mw.topBoxExp.currentText()
    #     preco = mw.topPreco.text()
    #     processador = mw.topPro.text().upper()
    #     marcaPro = mw.topMarcaPro.text().upper()
    #     frePro = mw.topFrePro.text().upper()
    #     geracaoPro = mw.topBoxGeracao.currentText()
    #     ram = mw.topRam.text().upper()
    #     ramMod = mw.topVerRam.text().upper()
    #     freRam = mw.topFreRam.text()
    #     ramExp = mw.topBoxExpRam.currentText()
    #
    #     data = date.today()
    #     serviceTag = mw.topService.text().upper()
    #     teamViewer = mw.topTeam.text().upper()
    #     anteVirus = mw.topBoxAntevirus.currentText()
    #     nomeRede = mw.topRede.text().upper()
    #     tipo = 'DESKTOP'
    #     local = mw.topBoxLocal.currentText()
    #     windows = mw.topWindows.text().upper()
    #     office = mw.topOffice.text().upper()
    #
    #     idWindows = mw.labeltopViewerWin.text().upper()
    #     idOffice = mw.labeltopViwerOff.text().upper()
    #
    #     '''Essa condicional é responsavel por verificar e tratar se tiver campos obrigatoris vazios'''
    #     if motivo == '' or marca == '' or modelo == '' or serviceTag == '' or nomeRede == '' or \
    #         processador == '' or geracaoPro == '' or ram == '' or ramMod == '':
    #         mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
    #         mw.BoxNoteMotivo.setStyleSheet("border: 1px solid rgb(255, 0, 0);")
    #         mw.BoxNoteItem.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notService.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notRede.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notBoxCarregador.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notBoxGeracao.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.notVerRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
    #         mw.labelNoteMensage.setText(mensagem)
    #
    #     ## TRATAMENTO DE SAVE NO BANCO:
    #
    #     else:
    #         try:
    #             cursor = db.conMySQL()
    #             cursor.execute(
    #                 f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, PRECO,
    #                    SERVICETAG, TEAMVIEWER,REDE, SSD, EXPANCIVEL, PROCESSADOR, MARCAPRO,
    #                    FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, LICENCAWINDOWS, LICENCAOFFICE,
    #                    ANTEVIRUS, LOCAL, DATA, idWindows, idOffice)
    #
    #                    VALUES ('{imb}','{marca}','{modelo}','{condicao}','{anoFab}','{preco}',
    #                    '{serviceTag}','{teamViewer}','{nomeRede}','{disco}','{DiscoExp}',
    #                    '{processador}','{marcaPro}','{frePro}','{geracaoPro}','{ram}','{ramMod}','{freRam}',
    #                    '{ramExp}','{windows}','{office}','{anteVirus}','{local}','{data}','{idWindows}','{idOffice}');""")
    #
    #             cursor.execute(f"""SELECT MAX(idComputer) FROM computer;""")
    #             cur = cursor.fetchall()
    #             id_computer = cur[0][0]
    #             print(id_computer)
    #
    #             cursor.execute(
    #                 f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id_computer}','{marca}','{modelo}',
    #                     '{motivo}','{local}','{data}');""")
    #
    #             cursor.close()
    #
    #             mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
    #             dg.LabelDialog.setText('CADASTRADO COM SUCESSO')
    #             Dialog.show()
    #             limparCampsNote()
    #             quantiTable()
    #             carregarDados()
    #
    #         except pymysql.Error as erro:
    #             dg.LabelDialog.setText('ITEM NÃO CADASTRADO\n' + str(erro))
    #             Dialog.show()
    #             print(erro)
    #
    # def limparCampsTop():
    #     mw.notIMB.clear()
    #     mw.notMarca.clear()
    #     mw.notModelo.clear()
    #     mw.notCondicao.clear()
    #     mw.notAno.clear()
    #     mw.notPreco.clear()
    #     mw.notService.clear()
    #     mw.notTeam.clear()
    #     mw.notRede.clear()
    #     mw.notPro.clear()
    #     mw.notMarcaPro.clear()
    #     mw.notFrePro.clear()
    #     mw.notRam.clear()
    #     mw.notVerRam.clear()
    #     mw.notFreRam.clear()
    #     mw.notWindows.clear()
    #     mw.notOffice.clear()
    #     mw.notDecricao.clear()
    #     mw.labelNotebook.clear()
    #     mw.labelViwerOff.clear()
    #     mw.labelNoteMensage.clear()
    #     mw.notOffice.clear()
    #     mw.labelViewerWin.clear()
    #     mw.labelNoteMensage.clear()
    #     mw.notWindows.clear()
    #     mw.BoxNoteMotivo.setCurrentIndex(0)
    #     mw.BoxNoteItem.setCurrentIndex(0)
    #     mw.notBoxAntevirus.setCurrentIndex(0)
    #     mw.notBoxTela.setCurrentIndex(0)
    #     mw.notBoxCarregador.setCurrentIndex(0)
    #     mw.notBoxGeracao.setCurrentIndex(0)
    #     mw.notBoxSSD.setCurrentIndex(0)
    #     mw.notBoxExpRam.setCurrentIndex(0)
    #     mw.notBoxExp.setCurrentIndex(0)
    #
    # def cancelarCadTop():
    #     limparCampsTop()
    #     mw.stackedWidgetNovo.setCurrentWidget(mw.pageHomeNovo)
    #
    # mw.toplimWindows.clicked.connect(limWin)
    # mw.toplimOffice.clicked.connect(limOff)
    # mw.topPesWindows.clicked.connect(verWin)
    # mw.topPesOffice.clicked.connect(verOff)
    # mw.pushButtonCancelarTop.clicked.connect(cancelarCadTop)
    # mw.pushButtonSalvarTop.clicked.connect(cadastrarTop)

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
        sistema = mw.celBoxSistema.currentText()
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

        if imei == '' or marca == '' or modelo == '' or condicao == '' or cor == '' or ram == '' or memoria == '' \
                or motivo == '' or sistema == '' or processador == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            mw.celMeiOne.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celEstado.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celCor.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celRam.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celMemo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celPro.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.BoxCelMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.celBoxSistema.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
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
        mw.BoxCelMotivo.setCurrentIndex(0)
        mw.celBoxDual.setCurrentIndex(0)
        mw.celBoxChipTwo.setCurrentIndex(0)
        mw.celBoxChipOne.setCurrentIndex(0)
        mw.celBoxMicro.setCurrentIndex(0)
        mw.celBoxSistema.setCurrentIndex(0)

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
    def cadOutros():
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
                cursor.execute(f"""INSERT INTO outros (nome,marca,modelo,condicao,valor,descricao,local,data)
                    VALUES ('{nome}','{marca}','{modelo}','{condicao}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idOutros) FROM outros;""")
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
        ee.BoxOutrosMotivo.setCurrentIndex(0)

    def cancelarCadOutros():
        limparCampsOutros()
        MainEEstoque.close()

    ee.ButtonCadastraOutro.clicked.connect(cadOutros)
    ee.ButtonCancelarOutro.clicked.connect(cancelarCadOutros)

    ################################################-- MONITOR --#######################################################
    def cadastrarMonitor():
        print('certo')
        marca = mw.MonMarca.text()
        modelo = mw.MonModelo.text()
        condicao = mw.MonCondicao.text()
        tamanho = mw.MonBoxTela.currentText()
        valor = mw.MonValor.text()
        descricao = mw.MonDescricao.text()
        motivo = mw.BoxMoMotivo.currentText()
        tipo = 'MONITOR'
        local = 'ESTOQUE'
        data = date.today()

        if marca == '' or modelo == '' or tamanho == '' or motivo == '':
            mensagem = 'Por favor verifique se todos os campos obrigatórios estão\ndevidamente preenchidos'
            mw.MonMarca.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.MonModelo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.MonBoxTela.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.BoxMoMotivo.setStyleSheet(" border: 1px solid rgb(255, 0, 0);")
            mw.label_Mon.setText(mensagem)

        else:
            try:
                cursor = db.conMySQL()
                cursor.execute(
                    f"""INSERT INTO monitor (marca,modelo,condicao,tamanho,valor,descricao,local,data)
                        VALUES ('{marca}','{modelo}','{condicao}','{tamanho}','{valor}','{descricao}','{local}','{data}');""")

                cursor.execute(f"""SELECT MAX(idMonitor) FROM monitor;""")
                cur = cursor.fetchall()
                id = cur[0][0]
                print(id)

                cursor.execute(f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{id}','{marca}','{modelo}',
                                    '{motivo}','{local}','{data}');""")

                cursor.close()
                limparCampsMonitor()

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

    def limparCampsMonitor():
        mw.MonMarca.clear()
        mw.MonModelo.clear()
        mw.MonCondicao.clear()
        mw.MonValor.clear()
        mw.MonDescricao.clear()
        mw.label_Mon.clear()
        mw.BoxMoMotivo.setCurrentIndex(0)
        mw.MonBoxTela.setCurrentIndex(0)

    def cancelarCadMonitor():
        limparCampsMonitor()
        mw.stackedWidget.setCurrentWidget(mw.PageGestao)

    mw.pushButtonCadastraMon.clicked.connect(cadastrarMonitor)
    mw.pushButtonCancelarMon.clicked.connect(cancelarCadMonitor)