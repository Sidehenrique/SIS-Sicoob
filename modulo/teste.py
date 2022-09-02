# else:
# if chaveO != '' and chaveW == '':  # <---------------------------------- CHECA A CHVES OFFICE E SALVA
#     print('"ENTREI NA CONDICIONAL DO OFFICE"')
#     try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
#         cur = db.conMySQL()
#         cur.execute(f"""SELECT * FROM office WHERE CHAVE = '{chaveO}';""")  # ------ Que Contenha
#         idOff_db = cur.fetchall()
#         print(chaveO + '<--- Este é oque o usuario digitou')
#         print(idOff_db)
#
#         if idOff_db == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
#             print('Esta chave não esta cadastrada')
#             texto = 'CHAVE OFFICE NÃO CADASTRADA! \nDeseja cadastrar a chave?'
#             DialogiConditional.show()
#             di.LabelDialogMsg.setText(texto)
#
#
#             def simCad():
#                 MainEEstoque.show()
#                 ee.stackedWidgetCadastro.setCurrentWidget(ee.pageOffice)
#                 DialogiConditional.close()
#
#
#             di.pushButtonSim.clicked.connect(simCad)
#
#
#             def naoCad():
#                 DialogiConditional.close()
#
#
#             di.pushButtonNao.clicked.connect(naoCad)
#
#         if idOff_db != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
#             chave = idOff_db[0][1]
#             id = idOff_db[0][0]  # <-------------------------- pega só o primeiro campo da tupla (ID OFFICE) int
#             print(chave)
#             print(id)
#
#             try:  # <---------- vai pesquisar na tabela computer se essa (ID OFFICE) esta vinculada com alguma maquina
#                 cur.execute(f"""SELECT * FROM computer WHERE idOffice = {id};""")
#                 idNote = cur.fetchall()
#                 print(idNote)
#                 cur.close()
#
#                 if idNote == ():  # <--------- se retornar tupla vazia não achou (ID WINDOWS) vinculado a alguma maquina
#                     texto = f'ESTA CHAVE ID {id} ESTA DISPONIVEL\nDeseja VINCULAR a esta maquina?'
#                     chaveW = ''
#                     office = chave
#                     mw.labelViwerOff.setText(str(chave))
#                     print(texto)
#
#                     di1.LabelDialogMsg.setText(texto)
#                     DialogiConditionalOne.show()
#
#
#                     def simVin():
#                         try:
#                             cursor = db.conMySQL()
#                             cursor.execute(
#                                 f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
#                                        SERVICETAG, TEAMVIEWER,REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO,
#                                        FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, LICENCAWINDOWS, LICENCAOFFICE,
#                                        ANTEVIRUS, DESCRICAO, LOCAL, DATA, idOffice)
#
#                                        VALUES ('{imb}','{marca}','{modelo}','{condicao}','{anoFab}','{tela}','{preco}',
#                                        '{serviceTag}','{teamViewer}','{nomeRede}','{disco}','{DiscoExp}','{carregador}',
#                                        '{processador}','{marcaPro}','{frePro}','{geracaoPro}','{ram}','{ramMod}','{freRam}',
#                                        '{ramExp}','{chaveW}','{office}','{anteVirus}','{descricao}','{local}','{data}',
#                                        '{id}');""")
#
#                             cursor.execute(
#                                 f"""SELECT MAX(idComputer) FROM computer;""")
#                             cur = cursor.fetchall()
#                             idNF = cur[0][0]
#                             print(idNF)
#
#                             cursor.execute(
#                                 f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{idNF}',
#                                            '{marca}','{modelo}','{motivo}','{local}','{data}');"""
#                             )
#
#                             cursor.close()
#                             DialogiConditionalOne.close()
#                             dg.LabelDialog.setText('CADASTRADO COM SUCESSO!')
#                             Dialog.show()
#                             print('"SIM" Cadastrou, puchou ultima id e gerou historico')
#
#                         except pymysql.Error as erro:
#                             dg.LabelDialog.setText('ITEM NÃO CADASTRADO')
#                             Dialog.show()
#                             print(erro)
#                             mensageErro = str(erro)
#                             mw.labelNoteMensage.setStyleSheet("rgb(255, 0, 0);")
#                             mw.labelNoteMensage.setText(mensageErro)
#
#
#                     di1.pushButtonSim.clicked.connect(simVin)
#
#
#                     def naoVin():
#                         DialogiConditionalOne.close()
#                         texto = 'CADASTRAR SEM CHAVE?'
#                         di2.LabelDialogMsg.setText(texto)
#                         DialogiConditionalTwe.show()
#
#                         def sim():
#                             windows = ''
#                             office = ''
#
#                             try:
#                                 cursor = db.conMySQL()
#                                 cursor.execute(
#                                     f"""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
#                                            SERVICETAG, TEAMVIEWER,REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO,
#                                            FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, LICENCAWINDOWS, LICENCAOFFICE,
#                                            ANTEVIRUS, DESCRICAO, LOCAL, DATA)
#
#                                            VALUES ('{imb}','{marca}','{modelo}','{condicao}','{anoFab}','{tela}','{preco}',
#                                            '{serviceTag}','{teamViewer}','{nomeRede}','{disco}','{DiscoExp}','{carregador}',
#                                            '{processador}','{marcaPro}','{frePro}','{geracaoPro}','{ram}','{ramMod}','{freRam}',
#                                            '{ramExp}','{windows}','{office}','{anteVirus}','{descricao}','{local}','{data}');""")
#
#                                 cursor.execute(
#                                     f"""SELECT MAX(idComputer) FROM computer;""")
#                                 cur = cursor.fetchall()
#                                 idNF = cur[0][0]
#                                 print(idNF)
#
#                                 cursor.execute(
#                                     f"""INSERT INTO historico VALUES ('{Usuario}','NOVO','{tipo}','{idNF}',
#                                                '{marca}','{modelo}',
#                                                '{motivo}','{local}','{data}');"""
#                                 )
#
#                                 cursor.close()
#                                 DialogiConditionalTwe.close()
#                                 dg.LabelDialog.setText('CADASTRADO COM SUCESSO!')
#                                 Dialog.show()
#                                 print('"NÃO VINCULAR" Cadastrou, buscou ultima ID, gerou historico')
#
#                             except pymysql.Error as erro:
#                                 dg.LabelDialog.setText('ITEM NÃO CADASTRADO')
#                                 Dialog.show()
#                                 print(erro)
#                                 mensageErro = str(erro)
#                                 mw.labelNoteMensage.setStyleSheet("rgb(255, 0, 0);")
#                                 mw.labelNoteMensage.setText(mensageErro)
#
#                         def nao():
#                             DialogiConditionalTwe.close()
#                             mw.labelNoteMensage.setText('NÃO CADASTRADO')
#                             print('"NÃO VINCULAR" Op Não')
#
#                         di2.pushButtonSim.clicked.connect(sim)
#                         di2.pushButtonNao.clicked.connect(nao)
#
#
#                     di1.pushButtonNao.clicked.connect(naoVin)
#
#                 else:  # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
#                     print(f'ID COMPUTER {idNote[0][0]} ID WINDOWS {idNote[0][30]}')
#                     texto = f'ESTA ID WINDOWS {idNote[0][30]}\nJA ESTA EM USO NO COMPUTER {idNote[0][0]}'
#                     dg.LabelDialog.setText(texto)
#                     mw.labelNoteMensage.setText('NÃO CADASTRADO\nTente uma chave que não esteja em uso!')
#                     Dialog.show()
#
#             except:
#                 print('ALGO DEU ERRADO')
#                 dg.LabelDialog.setText('ALGO DEU ERRADO')
#
#     except:
#         texto = 'ALGO DEU MUITO ERRADO'
#         dg.LabelDialog.setText(texto)
#         Dialog.show()
#
# print('PASSEI ATE AQUI')