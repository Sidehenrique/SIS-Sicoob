from login import *
from estoqueTI import *
import mod


# TRATAMENTO LOGIN ========================================================================
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
        print(usuario, password)

        try:
            cursor = mod.conectar_mssql()
            cursor.execute(f"""SELECT senha FROM cadastro WHERE usuario = '{usuario}';""")
            senha_bd = cursor.fetchall()
            print(senha_bd[0][0])
            cursor.close()

        except:
            texto1 = 'Usuário ou senha incorreto'
            mensage(texto1)
            return

        if password == senha_bd[0][0]:
            texto2 = 'Login efetuado com sucesso'
            mensage(texto2)
            print('Sucesso!!!')
            MainLogin.close()
            MainEstoque.showMaximized()

        else:
            texto3 = 'A senha esta incorreta'
            mensage(texto3)

    ui.ENTER.clicked.connect(checkPassword)


# # TRATAMENTO HOME ======================================================================
#
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


#  TRATAMENTO ESTOQUE TI ==================================================================

def estoqueTi(mw):
    MainEstoque.setWindowTitle('ESTOQUE')

    #  Acionamento Botões menu ------------------------------------------------------------
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

    #  Acionamento Botões Submenu ---------------------------------------------------------
    def ButtonInicio():
        mw.lineEdit_pesquisarTable_3.clear()
        mw.stackedWidget.setCurrentWidget(mw.pageHome)
    mw.pushButton_Inicio.clicked.connect(ButtonInicio)

    mw.ButtonnNotebook.clicked.connect(lambda: mw.stackedWidget.setCurrentWidget(mw.page))

    nome = 'henrique'
    sobrenome = 'silva'
    telefone = 'tres'
    endereco = 'q10'

    coluna = nome, sobrenome, telefone, endereco
    linhas = ['um', 'dois', 'tres', 'quatro', 'cinco']

    mw.tableWidgetCelular.setColumnCount(15)
    mw.tableWidgetCelular.setRowCount(30)






if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    MainEstoque = QtWidgets.QMainWindow()

    ui = Ui_MainLogin()
    mw = Ui_MainEstoque()

    ui.setupUi(MainLogin)
    mw.setupUi(MainEstoque)

    MainLogin.showMaximized()

    login(ui)
    estoqueTi(mw)

    sys.exit(app.exec_())
