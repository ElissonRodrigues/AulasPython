from sqlite3 import connect
from json import dumps
from typing import Union

conn = connect("vendas.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
    "CREATE TABLE IF NOT EXISTS vendas (codigo_vendas INT, dados_venda JSON)"
)


def cadastrar_venda(codigo_vendas: int, dados_vendas: dumps) -> bool:
    cursor.execute("SELECT * FROM vendas WHERE codigo_vendas = ?", (codigo_vendas,))
    if cursor.fetchone():
        return False
    else:
        cursor.execute(
            "INSERT INTO vendas (codigo_vendas, dados_venda) VALUES (?, ?)",
            (codigo_vendas, dados_vendas),
        )
        conn.commit()
        return True


def consultar_venda(codigo: int) -> tuple:
    cursor.execute("SELECT * FROM vendas WHERE codigo_vendas = ?", (codigo,))
    resultado = cursor.fetchone()

    if resultado:
        return resultado
    else:
        return False
