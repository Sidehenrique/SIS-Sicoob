import pymysql


# MANIPULANDO BANCO DE DADOS SQL ---------------------------------------------------

def conMySQL():
    conx = pymysql.connect(
        host='10.6.32.24',
        database='sisdb',
        user='admin',
        password='S1coob4155@@',
        autocommit=True,
    )

    cur = conx.cursor()
    return cur






