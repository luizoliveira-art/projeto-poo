class Curso:
    def __init__(self, codigo, nome, carga_horaria, pre_requisitos=None):
        self._codigo = str(codigo)
        self._nome = str(nome)
        self.carga_horaria = carga_horaria
        self.pre_requisitos = pre_requisitos or []

    @property
    def codigo(self):
        return self._codigo

    @property
    def nome(self):
        return self._nome

    @property
    def carga_horaria(self):
        return self._carga_horaria

    @carga_horaria.setter
    def carga_horaria(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("Carga horária deve ser positiva.")
        self._carga_horaria = valor

    def __str__(self):
        return f"[{self.codigo}] {self.nome} ({self.carga_horaria}h)"

    def __repr__(self):
        return f"Curso('{self.codigo}')"
