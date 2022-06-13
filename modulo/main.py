from Login import *
from Home import *
from HomeTI import *
import mod


# TRATAMENTO LOGIN ========================================================================
def main(ui):
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
            MainWindow.showMaximized()

        else:
            texto3 = 'A senha esta incorreta'
            mensage(texto3)

    ui.ENTER.clicked.connect(checkPassword)


# TRATAMENTO HOME ======================================================================


def home(mw):
    MainWindow.setWindowTitle('HOME')
    # Acionamento Botão sair -----------------------------------------------------------
    def callLogin():
        MainWindow.close()
        ui.frame_erro.close()
        ui.lineEdit.clear()
        ui.lineEdit_3.clear()
        MainLogin.showMaximized()

    mw.pushButton_sair.clicked.connect(callLogin)

    # Acionamento Botão TI -------------------------------------------------------------
    def callti():
        MainWindow.close()
        MainTI.showMaximized()

    mw.pushButton_TI.clicked.connect(callti)


#
# TRATAMENTO HOME TI =====================================================================


def homeTi(mt):
    MainTI.setWindowTitle('HOME TECNOLOGIA')

    # Acionamento Botão sair -------------------------------------------------------------
    def ButtonSair():
        MainTI.close()
        MainWindow.showMaximized()

    mt.pushButton_sair.clicked.connect(ButtonSair)

    # tratamento de informações com o BANCO DE DADOS ------------------------------------







if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainLogin = QtWidgets.QMainWindow()
    MainWindow = QtWidgets.QMainWindow()
    MainTI = QtWidgets.QMainWindow()
    ui = Ui_MainLogin()
    mw = Ui_MainWindow()
    mt = Ui_MainTI()
    mw.setupUi(MainWindow)
    ui.setupUi(MainLogin)
    mt.setupUi(MainTI)
    MainLogin.showMaximized()
    main(ui)
    home(mw)
    homeTi(mt)
    sys.exit(app.exec_())
