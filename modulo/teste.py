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


except pymysql.Error as erro:
    dg.LabelDialog.setText('ITEM NÃO CADASTRADO\n' + str(erro))
    Dialog.show()
    print(erro)