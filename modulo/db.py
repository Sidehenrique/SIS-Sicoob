import pymysql
import pandas as pd

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

def conPandasSQL():
    conx = pymysql.connect(
        host='10.6.32.24',
        database='bdsister',
        user='admin',
        password='S1coob4155@@',
        autocommit=True,
    )
    return conx





# conx = conPandasSQL()
# df = pd.read_sql("SELECT * FROM historico", conx)
#
# # print(df.head(5))
# print(df)
# print(df[df['status'] == 'NOVO'])  # <---------- expressão booleana simples
#
# print(df[(df['status'] == 'NOVO') & (df['local'] == 'ESTOQUE')].describe())  # <---------- expressão booleana mais avançada
#
# result = df[(df['status'] == 'NOVO') & (df['local'] == 'ESTOQUE')].shape[0]
#
# print(result)
