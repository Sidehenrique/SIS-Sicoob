from PyQt5 import QtCore, QtGui, QtWidgets
from CREAT import Ui_MainWindow


def creacao(nome, sobrenome, idade):
    nome = nome
    sobrenome = sobrenome
    idade = idade

    for



        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setMinimumSize(QtCore.QSize(420, 80))
        self.frame.setMaximumSize(QtCore.QSize(420, 80))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


























# import pandas as pd
# import db
#
# dataframe_funcionarios = pd.read_excel('D:\PROJETOS\SICOOB\outros\Funcionários e Membros Estatutários.xlsx')
#
# print(dataframe_funcionarios)
#
# for i, dados in enumerate(dataframe_funcionarios['Nome']):
#     nome = dataframe_funcionarios.loc[i, 'Nome']
#     sexo = dataframe_funcionarios.loc[i, 'SEXO']
#     situacao = dataframe_funcionarios.loc[i, 'Situação']
#     empregador = dataframe_funcionarios.loc[i, 'Empregador']
#     colaborador = dataframe_funcionarios.loc[i, 'Colaborador']
#     cpf = dataframe_funcionarios.loc[i, 'CPF']
#     rg = dataframe_funcionarios.loc[i, 'RG']
#     orgao_expedidor = dataframe_funcionarios.loc[i, 'Órgão Expedidor']
#     matricula = dataframe_funcionarios.loc[i, 'Matrícula']
#     sisbr = dataframe_funcionarios.loc[i, 'Login Sisbr']
#     unidade = dataframe_funcionarios.loc[i, 'PA / Unidade']
#     area_atuacao = dataframe_funcionarios.loc[i, 'Seções']
#     setor = dataframe_funcionarios.loc[i, 'Setor']
#     cargo = dataframe_funcionarios.loc[i, 'Cargo']
#     superior = dataframe_funcionarios.loc[i, 'Superior Imediato']
#     admissao = dataframe_funcionarios.loc[i, 'Admissão']
#     desligamento = dataframe_funcionarios.loc[i, 'Data de desligamento']
#     entrada = dataframe_funcionarios.loc[i, 'Horário Entrada']
#     saida = dataframe_funcionarios.loc[i, 'Horário Saída']
#     nascimento = dataframe_funcionarios.loc[i, 'Data de Nascimento']
#     civil = dataframe_funcionarios.loc[i, 'Estado Civil']
#     idade = dataframe_funcionarios.loc[i, 'Idade']
#     camiseta = dataframe_funcionarios.loc[i, 'Tamanho Camiseta']
#     email = dataframe_funcionarios.loc[i, 'E-mail Corporativo']
#     endereco = dataframe_funcionarios.loc[i, 'ENDEREÇO']
#     bairro = dataframe_funcionarios.loc[i, 'Bairro']
#     cidade = dataframe_funcionarios.loc[i, 'CIDADE']
#     estado = dataframe_funcionarios.loc[i, 'ESTADO']
#     cep = dataframe_funcionarios.loc[i, 'CEP']
#     pis = dataframe_funcionarios.loc[i, 'PIS']
#     ctps = dataframe_funcionarios.loc[i, 'CTPS']
#     data_ctps = dataframe_funcionarios.loc[i, 'Data de Emissão da CTPS']
#     serie = dataframe_funcionarios.loc[i, 'Série']
#     pld = dataframe_funcionarios.loc[i, 'PLD']
#     vencimento_pld = dataframe_funcionarios.loc[i, 'Vencimento - PLD']
#     fone_pessoal = dataframe_funcionarios.loc[i, 'Telefone Pessoal']
#     fone_coop = dataframe_funcionarios.loc[i, 'Telefone Corporativo']
#     cel_coop = dataframe_funcionarios.loc[i, 'Celular Corporativo']
#     certidao_nascimento = dataframe_funcionarios.loc[i, 'Certidão de Nascimento ou Casamento']
#     certidao_casamento = dataframe_funcionarios.loc[i, 'Certidão de Nascimento ou Casamento']
#     contrato_trabalho = dataframe_funcionarios.loc[i, 'Contrato de Trabalho']
#     declaracao_dependente = dataframe_funcionarios.loc[i, 'Declaração de Dependentes']
#     declaracao_transporte = dataframe_funcionarios.loc[i, 'Declaração de Vale Transp.']
#     copia_clt = dataframe_funcionarios.loc[i, 'Copia da Carteira de Trabalho']
#     termo_compromisso = dataframe_funcionarios.loc[i, 'Termo de Compromisso']
#     comprovante_residencia = dataframe_funcionarios.loc[i, 'Comprovande de Residência']
#     atestado_admissional = dataframe_funcionarios.loc[i, 'Atestado Admisional ou Periódico']
#     atestado_periodico = dataframe_funcionarios.loc[i, 'Atestado Admisional ou Periódico']
#
#     print(dados)
#     try:
#         con = db.conMySQL()
#         con.execute(f"""INSERT INTO colaborador (NOME, CPF, RG, EXPEDIDOR, SEXO, NASCIMENTO, IDADE, CIVIL, PIS,
#         CTPS, SERIE, CERTNASCIMENTO, CERTCASAMENTO, ENDERECO, BAIRRO, CIDADE, ESTADO, CEP, EMAIL, FONEPESSOAL, FONECORPORATIVO,
#         CELCORPORATIVO, COMP_RESIDENCIA, CARGO, SETOR, SECOES, COLABORADOR,
#         PA_UNIDADE, MATRICULA, EMPREGADOR, SUPERIOR, ADMISSAO, DESLIGAMENTO, SITUACAO, HORARIOENT, HORARIOSAI,
#         ATESTADO_ADMISSIONAL, ATESTADO_PERIODICO, COPIA_CLT, CARTEIRA_TRABALHO, DATA_TRANSPORTE, DECLARACAO_DEPENDENTES,
#         TERMO_COMPROMISSO, PLD, VENCIMENTO_PLD, T_CAMISETA)
#         VALUES ('{nome}','{cpf}','{rg}','{orgao_expedidor}','{sexo}','{nascimento}','{idade}','{civil}',
#                 '{pis}','{ctps}','{serie}','{certidao_nascimento}','{certidao_casamento}','{endereco}','{bairro}',
#                 '{cidade}','{estado}','{cep}','{email}','{fone_pessoal}','{fone_coop}','{cel_coop}',
#                 '{comprovante_residencia}','{cargo}','{setor}','{area_atuacao}','{colaborador}','{unidade}',
#                 '{matricula}','{empregador}','{superior}','{admissao}','{desligamento}','{situacao}','{entrada}',
#                 '{saida}','{atestado_admissional}','{atestado_periodico}','{copia_clt}','{contrato_trabalho}',
#                 '{declaracao_transporte}','{declaracao_dependente}','{termo_compromisso}','{pld}','{vencimento_pld}',
#                 '{camiseta}');""")
#
#     except:
#         continue
#
# con.close()
#
#
#
#
#
#
#
#
# #
# # try:
# #     con = db.conMySQL()
# #     con.execute(f"""INSERT INTO colaborador (NOME, CPF, RG, EXPEDIDOR, SEXO, NASCIMENTO, IDADE, CIVIL, PAI, MAE, PIS
# #        , CTPS, SERIE, CERTNASCIMENTO, CERTCASAMENTO, ENDERECO, BAIRRO, CIDADE, ESTADO, CEP, EMAIL, FONEPESSOAL, FONECORPORATIVO,
# #        CELCORPORATIVO, COMP_RESIDENCIA, ESCOLARIDADE, ENTIDADE, AREA, DATACONCLUSAO, CERTIFICACAO1, DATACONCLUSAO1,
# #        CERTIFICACAO2, DATACONCLUSAO2, IDIOMAPRIMARIO, IDIOMASECUNDARIO, NIVEL, CARGO, SETOR, SECOES, COLABORADOR,
# #        PA_UNIDADE, MATRICULA, EMPREGADOR, SUPERIOR, SALARIO, ADMISSAO, DESLIGAMENTO, SITUACAO, HORARIOENT, HORARIOSAI,
# #        ATESTADO_ADMISSIONAL, ATESTADO_PERIODICO, COPIA_CLT, CARTEIRA_TRABALHO, DATA_TRANSPORTE, DECLARACAO_DEPENDENTES,
# #        TERMO_COMPROMISSO, PLANO_SAUDE, SEGURO_VIDA, GYMPASS, VALE_ALIMENTACAO, VALE_TRANSPORTE, PLD, VENCIMENTO_PLD,
# #        T_CAMISETA)
# #        VALUES ('{nome}','{cpf}','{rg}','{orgao_expedidor}','{sexo}','{nascimento}','{idade}','{civil}','{pai}','{mae}',
# #                '{pis}','{ctps}','{serie}','{certidao_nascimento}','{certidao_casamento}','{endereco}','{bairro}','{cidade}','{estado}','{cep}',
# #                '{email}','{fone_pessoal}','{fone_coop}','{cel_coop}','{comprovante_residencia}','{escolaridade}','{entidade}','{area}','{data_conclusao}','{certificacao1}',
# #                '{data_conclusao1}','{certificacao2}','{data_conclusao2}','{idioma_primario}','{idioma_secundario}','{nivel}','{cargo}','{setor}','{area_atuacao}','{colaborador}',
# #                '{unidade}','{matricula}','{empregador}','{superior}','{salario}','{admissao}','{desligamento}','{situacao}','{entrada}','{saida}',
# #                '{atestado_admissional}','{atestado_periodico}','{copia_clt}','{contrato_trabalho}','{declaracao_transporte}','{declaracao_dependente}','{termo_compromisso}','{plano_saude}','{seguro_vida}','{gympass}',
# #                '{vale_alimentacao}','{vale_transporte}','{pld}','{vencimento_pld}','{camiseta}');""")
# #
# # except:
# #     continue