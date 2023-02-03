from __future__ import annotations
from sqlite3 import connect
from datetime import date


conn = connect("agenda.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute(
"""
CREATE TABLE IF NOT EXISTS contato (
    id INTEGER PRIMARY KEY NOT NULL,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    telefone TEXT NOT NULL,
    nascimento TIMESTAMP NOT NULL
)
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

def checar_id(id_: int) -> bool:
    cursor.execute(
    """
    SELECT id FROM contato WHERE id = ?
    """,
    (id_,),
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


def atualizar_contato(id_: int, nome: str, email: str, telefone: str, nascimento: date) -> bool:      
    """Cadastrar novo contato na agenda

    Args:
        nome (str): Nome do contato
        email (text): E-mail do contato
        telefone (str): telefone do contato
        nascimento (str): data de nascimento da pessoa cadastrada
        cadastro (datetime): data de cadastro na agenda

    Returns:
        bool: True para atualizado com sucesso e False para não deletado
    """  
    cursor.execute(
    """
    UPDATE contato SET nome = ?, email = ?, telefone = ?, nascimento = ? WHERE id = ?
    """,
        (nome, email, telefone, nascimento, id_),
    )

    conn.commit()

    return True if cursor.rowcount >= 1 else False


def listar_contato() -> list[list] | False:
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


def buscar_id(id_: int) -> tuple[str, int] | False:    
    """buscar por id na lista de contatos

    Args:
        id (int): id do contato

    Returns:
        tuple[str, int] | False: tuple para contato encontrado.
    """
    cursor.execute(
        """
        SELECT * FROM contato WHERE id = ?
        """,
        (id_,),
    )

    resultado = cursor.fetchone()
    return resultado if resultado else False
