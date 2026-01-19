class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor or len(str(valor).strip()) < 3:
            raise ValueError("Nome inválido.")
        self._nome = str(valor)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if "@" not in str(valor):
            raise ValueError("E-mail inválido.")
        self._email = str(valor)

    def __str__(self):
        return f"{self.nome} ({self.email})"
