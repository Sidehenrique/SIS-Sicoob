import MySQLdb
import pymysql
from Dialog import *
from DialogCondicional import *


# MANIPULANDO BANCO DE DADOS SQL ---------------------------------------------------
def conMySQL():
    conx = pymysql.connect(
        host='10.6.32.24',
        database='basesis',
        user='admin',
        password='S1coob4155@@',
        autocommit=True,
    )

    cur = conx.cursor()
    return cur

def checkWin(ui):

    try:  # <------------------------------------------------ verifica na tabela windows se existe ou não a id informada
        cur = conMySQL()
        cur.execute(f"""SELECT * FROM windows WHERE idWindows = {3} or CHAVE = '{''}';""")  # ------------- Que Contenha
        idwin_db = cur.fetchall()

        print(idwin_db)

        if idwin_db == ():  # <-------------------------------------------- verifica se a pesquisa voltou vazia em tupla
            print('Esta chave não esta cadastrada')
            texto = 'CHAVE NÃO CADASTRADA'
            ui.LabelDialog.setText(texto)
            Dialog.show()

        elif idwin_db != ():  # <--------------------------- verifica se o a pesquisa voltou diferente de vazia em tupla
            idwin_db = idwin_db[0][0]   # <-------------------------- pega só o primeiro campo da tupla (ID WINDOWS) int

            try:   # <---------- vai pesquisar na tabela computer se essa (ID WINDOWS) esta vinculada com alguma maquina
                cur.execute(f"""SELECT * FROM computer WHERE idWindows = {idwin_db};""")
                idNote = cur.fetchall()
                cur.close()
                print(idNote)

                if idNote == ():  # <--------- se retornar tupla vazia não achou (ID WINDOWS) vinculado a alguma maquina
                    print('Esta chave não esta vinculada a nunhum dispositivo')
                    print('CHAVE DISPONIVEL')
                    return False

                else:   # <------------ se retornar diferente de tupla vazia tem (ID WINDOWS) vinculado a alguma maquina
                    print(f'ID COMPUTER {idNote[0][0]} ID WINDOWS {idNote[0][27]}')
                    print('Esta chave já esta em uso em outra maquina')
                    return True

            except pymysql.Error as erro:
                ui.LabelDialog.setText(erro)
                print(str(erro))

    except pymysql.Error as erro:
        ui.LabelDialog.setText(erro)
        print(str(erro))




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    checkWin(ui)
    sys.exit(app.exec_())

