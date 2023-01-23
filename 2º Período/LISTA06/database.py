from __future__ import annotations
from sqlite3 import connect
from datetime import date

conn = connect("agenda.db")
cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS contato (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT NOT NULL,
    nascimento TIMESTAMP NOT NULL,
    cadastro TIMESTAMP NOT NULL DEFAULT (DATETIME('NOW', 'LOCALTIME'))
);
"""
)
conn.commit()


def adicionar_contato(nome: str, email: str, telefone: str, nascimento: date) -> None:
    """Cadastrar novo contato na agenda

    Args:
        nome (str): Nome do contato
        email (text): E-mail do contato
        telefone (str): telefone do contato
        nascimento (str): data de nascimento da pessoa cadastrada
        cadastro (datetime): data de cadastro na agenda
    """
    cursor.execute(
    """
    INSERT INTO contato (nome, email, telefone, nascimento) VALUES (?, ?, ?, ?)
    """,
        (nome.lower().strip(), email.lower().strip(), telefone.strip(), nascimento),
    )
    conn.commit()

    return True if cursor.rowcount >= 1 else False


def checar_email(email: str) -> bool:
    """Verifica se o endereço de email já existe na base de dados

    Args:
        email (str): Endereço de email

    Returns:
        bool: True se o email existe
    """
    cursor.execute(
    """
    SELECT email FROM contato WHERE email = ?
    """,
        (email,),
    )

    return True if cursor.fetchone() else False


def deletar_contato(email: str) -> tuple:
    """Deletar produto através do nome exato

    Args:
        nome (str): Nome exato

    Returns:
        boolean: True para deletado com sucesso e False para não deletado
    """
    cursor.execute(
    """
    DELETE FROM contato WHERE email = ?
    """,
        (email.lower().strip(),),
    )
    conn.commit()

    return True if cursor.rowcount >= 1 else False


def atualizar_conatato(email: str, novo_telefone: str) -> bool:
    """Atualizar numero de contato já existente na base de dados

    Args:
        email (str): Endereço de email
        novo_telefone (str): Novo numero de telefone

    Returns:
        bool: True para numero atualizado
    """
    cursor.execute(
    """
    UPDATE contato SET telefone = ? WHERE email = ?
    """,
        (novo_telefone.strip(), email.lower().strip()),
    )

    conn.commit()

    return True if cursor.rowcount >= 1 else False


def dados_contato() -> list[list] | False:
    """Retorna todos os dados do contato cadastrado

    Returns:
        list[list] | False: lista para sucesso
    """
    cursor.execute(
    """
    SELECT * FROM contato
    """
    )

    contatos = cursor.fetchall()
    return contatos if contatos else False


def busca_contato(nome: str) -> list[list] | False:
    """buscar nome na lista de contatos

    Args:
        nome (str): nome do contato

    Returns:
        list[list] | False: List para contatos encontrados
    """
    cursor.execute(
        """
        SELECT * FROM contato WHERE nome LIKE ?
        """,
        ("%" + nome + "%",),
    )

    resultado = cursor.fetchall()
    return resultado if resultado else False


def buscar_email(email: str) -> tuple[str] | False:
    """buscar email na lista de contatos

    Args:
        nome (str): nome do contato

    Returns:
        tuple[str] | False: tuple para contato encontrado.
    """
    cursor.execute(
        """
        SELECT * FROM contato WHERE email = ?
        """,
        (email,),
    )

    resultado = cursor.fetchall()
    return resultado if resultado else False
