class Pessoa:
    def __init__(self, nome, email):
        self._nome = str(nome)
        self._email = str(email)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not valor:
            raise ValueError('O nome não pode estar vazio.')
        self._nome = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if '@' not in valor:
            raise ValueError('E-mail inválido.')
        self._email = valor

    def __str__(self):
        return f'{self.nome} ({self.email})'
