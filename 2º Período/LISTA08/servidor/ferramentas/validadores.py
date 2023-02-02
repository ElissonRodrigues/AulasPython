from __future__ import annotations
from re import search
from datetime import datetime


class Validar:
    def __init__(self):
        pass

    def email(self, email: str) -> bool:
        """Validador de email

        Args:
            email (str): endereço de email

        Returns:
            bool: True para válido
        """
        email = search("([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+", email)
        return True if email else False

    def telefone(self, telefone: str) -> bool:
        """Validador de telefone

        Args:
            telefone (str): Número de telefone nesse formato: (DDD) 91234-4455

        Returns:
            bool: True para válido
        """
        telefone = search("^\([1-9]{2}\) (?:[2-8]|9[1-9])[0-9]{3}\-[0-9]{4}$", telefone)
        return True if telefone else False

    def nascimento(self, nascimento: str) -> bool:
        """Validador de nascimento

        Args:
            nascimento (str): data de nascimento no seguite formato: DDD/MM/AAAA

        Returns:
            bool: True para válido
        """
        try:
            nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        except ValueError:
            nascimento = False

        return True if nascimento else False

    def todos(self, email: str, telefone: str, nascimento: str) -> tuple[bool, None | str]:
        """Validar e-mail, telefone e nascimento ao mesmo tempo

        Args:
            email (str): Endereço de E-mail
            telefone (str): numero de telefone
            nascimento (str): data de nascimento

        Returns:
            tuple[bool, None | str]: Tupla contendo os dados com os resultados da validação
        """
        if all([self.email(email), self.telefone(telefone), self.nascimento(nascimento)]):
            return (True, None)
        else:
            if not self.email(email):
                return (False, "email")
            elif not self.telefone(telefone):
                return (False, "telefone")
            elif not self.nascimento(nascimento):
                return (False, "nascimento")
