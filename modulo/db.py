import datetime

import pymysql
from Dialog import *
from DialogCondicional import *
from entradaEstoque import *
import datetime

# MANIPULANDO BANCO DE DADOS SQL ---------------------------------------------------
def conMySQL():
    conx = pymysql.connect(
        host='10.6.32.24',
        database='bdsister',
        user='admin',
        password='S1coob4155@@',
        autocommit=True,
    )

    cur = conx.cursor()
    return cur

