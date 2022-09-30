import pymysql
from Dialog import *
from DialogCondicional import *
from entradaEstoque import *


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

# cur = conMySQL()
# cur.execute("""INSERT INTO computer (IMB, MARCA, MODELO, CONDICAO, ANOFAB, TELA, PRECO,
#                    SERVICETAG, TEAMVIEWER,REDE, SSD, EXPANCIVEL, CARREGADOR, PROCESSADOR, MARCAPRO,
#                    FREPRO, GERACAO, RAM, MODELORAM, FRERAM, EXPRAM, LICENCAWINDOWS, LICENCAOFFICE,
#                    ANTEVIRUS, DESCRICAO, LOCAL, DATA, idWindows, idOffice)
#
# VALUES (16000,'ACER','NITRO','NOVO', 2022, 15, 5000, 'SADA12', 'ASD1231', 'SIDE4155', 'SIM', 'SIM',
# 'SIM', 'I3','INTEL', 3.3, '8 GERACAO', 8,'DDR4', 1600,'SIM','nmfdmnfmdnfmfmdnmfn','fnmfndmfnmdnfmndfmnm','ATUALIZADO',
# '','ESTOQUE','22-07-2022',null,null)""")
#
