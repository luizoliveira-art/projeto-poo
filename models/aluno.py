from models.pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, matricula, nome, email):
        super().__init__(nome, email)
        self._matricula = str(matricula)
        self.historico = []

    @property
    def matricula(self):
        return self._matricula

    @property
    def cr(self):
        disciplinas_concluidas = [m for m in self.historico if m.situacao != "CURSANDO"]
        if not disciplinas_concluidas:
            return 0.0
        soma_notas = sum(m.nota for m in disciplinas_concluidas)
        return round(soma_notas / len(disciplinas_concluidas), 2)

    def __lt__(self, outro):
        return self.cr < outro.cr

    def __str__(self):
        return f"[{self.matricula}] {self.nome} - CR: {self.cr}"
