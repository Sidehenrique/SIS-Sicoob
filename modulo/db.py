import pyodbc


# MANIPULANDO BANCO DE DADOS SQL ---------------------------------------------------

def conectar_mssql():
    con = pyodbc.connect(
        # Driver que será utilizado na conexão
        'DRIVER={ODBC Driver 17 for SQL Server};'
        # IP ou nome do servidor.
        'SERVER=10.6.32.24;'
        # Porta
        'PORT=1433;'
        # Banco que será utilizado.
        'DATABASE=SISBD;'
        # Nome de usuário.
        f'UID=sa;'
        # Senha.
        f'PWD=sicoob;')

    # Criando o cursor que irá executar os comandos SQL (instruções DML, DDL, etc).
    cur = con.cursor()
    return cur






